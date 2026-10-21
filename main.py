
from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI(title="Clasificador de commits con IA")


class CommitRequest(BaseModel):
    mensaje: str


@app.get("/")
def inicio():
    return {"mensaje": "API del clasificador de commits funcionando"}


@app.post("/clasificar")
def clasificar_commit(datos: CommitRequest):
    prompt = f"""
    Clasifica este mensaje de commit en una sola categoría:
    feat, fix, docs, test, chore o refactor.

    Significado:
    feat: nueva funcionalidad
    fix: corrección de errores
    docs: documentación
    test: pruebas
    chore: tareas de mantenimiento
    refactor: mejora del código sin cambiar su funcionamiento

    Responde únicamente con el nombre de la categoría.

    Mensaje: {datos.mensaje}
    """

    respuesta = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "qwen2.5-coder:1.5b",
            "prompt": prompt,
            "stream": False
        },
        timeout=60
    )

    respuesta.raise_for_status()
    categoria = respuesta.json()["response"].strip().lower()

    categorias_validas = [
        "feat", "fix", "docs", "test", "chore", "refactor"
    ]

    if categoria not in categorias_validas:
        categoria = "chore"

    return {
        "mensaje": datos.mensaje,
        "categoria": categoria
    }
