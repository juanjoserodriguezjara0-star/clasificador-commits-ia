import os
from datetime import datetime
from typing import Any

import psycopg
import requests
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field

app = FastAPI(
    title="Clasificador de commits con IA",
    description="Clasifica mensajes de commit usando Ollama y guarda las inferencias en PostgreSQL.",
    version="1.0.0",
)

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434").rstrip("/")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5-coder:1.5b")
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://clasificador:clasificador@localhost:5432/clasificador",
)
CATEGORIAS_VALIDAS = {"feat", "fix", "docs", "test", "chore", "refactor"}


class CommitRequest(BaseModel):
    mensaje: str = Field(min_length=1, max_length=2000)


def conectar_db():
    """Abre una conexión a PostgreSQL usando DATABASE_URL."""
    return psycopg.connect(DATABASE_URL, connect_timeout=3)


def guardar_inferencia(mensaje: str, categoria: str) -> dict[str, Any]:
    """Guarda una clasificación y devuelve el registro creado."""
    with conectar_db() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO inferencias (mensaje, categoria)
                VALUES (%s, %s)
                RETURNING id, mensaje, categoria, creada_en
                """,
                (mensaje, categoria),
            )
            fila = cursor.fetchone()
    return {
        "id": fila[0],
        "mensaje": fila[1],
        "categoria": fila[2],
        "creada_en": fila[3].isoformat() if isinstance(fila[3], datetime) else str(fila[3]),
    }


def obtener_inferencias(limite: int) -> list[dict[str, Any]]:
    """Consulta las inferencias más recientes guardadas en PostgreSQL."""
    with conectar_db() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute(
                """
                SELECT id, mensaje, categoria, creada_en
                FROM inferencias
                ORDER BY creada_en DESC, id DESC
                LIMIT %s
                """,
                (limite,),
            )
            filas = cursor.fetchall()
    return [
        {
            "id": fila[0],
            "mensaje": fila[1],
            "categoria": fila[2],
            "creada_en": fila[3].isoformat() if isinstance(fila[3], datetime) else str(fila[3]),
        }
        for fila in filas
    ]


@app.get("/")
def inicio():
    return {"mensaje": "API del clasificador de commits funcionando", "version": app.version}


@app.get("/health")
def health():
    """Comprueba la API y las dependencias principales."""
    resultado = {"estado": "ok", "api": "ok", "ollama": "desconocido", "postgresql": "desconocido"}
    try:
        respuesta = requests.get(f"{OLLAMA_URL}/api/tags", timeout=3)
        respuesta.raise_for_status()
        resultado["ollama"] = "ok"
    except requests.RequestException:
        resultado["ollama"] = "no disponible"
        resultado["estado"] = "degradado"

    try:
        with conectar_db() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT 1")
                cursor.fetchone()
        resultado["postgresql"] = "ok"
    except psycopg.Error:
        resultado["postgresql"] = "no disponible"
        resultado["estado"] = "degradado"

    return resultado


@app.post("/clasificar")
def clasificar_commit(datos: CommitRequest):
    prompt = f"""
Clasifica el mensaje de commit en exactamente una de estas categorías:
feat, fix, docs, test, chore, refactor.

Definiciones:
feat: nueva funcionalidad.
fix: corrección de errores.
docs: cambios en documentación.
test: creación o modificación de pruebas.
chore: mantenimiento o tareas auxiliares.
refactor: reorganización del código sin cambiar su comportamiento.

Devuelve únicamente la categoría, sin explicación ni puntuación.

Mensaje de commit: {datos.mensaje}
"""

    try:
        respuesta = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False,
                "options": {"temperature": 0},
            },
            timeout=90,
        )
        respuesta.raise_for_status()
        contenido = respuesta.json().get("response", "").strip().lower()
    except requests.RequestException as exc:
        raise HTTPException(
            status_code=503,
            detail="No se pudo conectar con Ollama. Comprueba que esté ejecutándose y que el modelo esté instalado.",
        ) from exc
    except (ValueError, AttributeError) as exc:
        raise HTTPException(
            status_code=502,
            detail="Ollama devolvió una respuesta que no se pudo interpretar.",
        ) from exc

    categoria = next(
        (
            palabra.strip(".,:;!¿?()[]{}")
            for palabra in contenido.split()
            if palabra.strip(".,:;!¿?()[]{}") in CATEGORIAS_VALIDAS
        ),
        None,
    )
    if categoria is None:
        raise HTTPException(
            status_code=502,
            detail="El modelo no devolvió una categoría válida.",
        )

    try:
        registro = guardar_inferencia(datos.mensaje, categoria)
    except psycopg.Error as exc:
        raise HTTPException(
            status_code=503,
            detail="El commit se clasificó, pero no se pudo guardar porque PostgreSQL no está disponible.",
        ) from exc

    return registro


@app.get("/inferencias")
def listar_inferencias(limite: int = Query(default=20, ge=1, le=100)):
    """Devuelve las inferencias guardadas, de la más reciente a la más antigua."""
    try:
        return {"total": len(registros := obtener_inferencias(limite)), "inferencias": registros}
    except psycopg.Error as exc:
        raise HTTPException(
            status_code=503,
            detail="No se pudo consultar PostgreSQL. Comprueba la conexión y la inicialización de la base de datos.",
        ) from exc
