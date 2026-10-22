import os

import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Clasificador de commits con IA")

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5-coder:1.5b")
CATEGORIAS_VALIDAS = {"feat", "fix", "docs", "test", "chore", "refactor"}


class CommitRequest(BaseModel):
    mensaje: str = Field(min_length=1, max_length=2000)


@app.get("/")
def inicio():
    return {"mensaje": "API del clasificador de commits funcionando"}


@app.get("/health")
def health():
    """Comprueba que la API esté activa."""
    return {"estado": "ok"}


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
            },
            timeout=60,
        )
        respuesta.raise_for_status()
        contenido = respuesta.json().get("response", "").strip().lower()
    except requests.RequestException as exc:
        raise HTTPException(
            status_code=503,
            detail="No se pudo conectar con Ollama. Comprueba que esté ejecutándose.",
        ) from exc
    except (ValueError, AttributeError) as exc:
        raise HTTPException(
            status_code=502,
            detail="Ollama devolvió una respuesta que no se pudo interpretar.",
        ) from exc

    # Acepta respuestas como "Categoría: fix", pero solo devuelve una etiqueta válida.
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

    return {"mensaje": datos.mensaje, "categoria": categoria}
