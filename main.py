
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Clasificador de commits con IA")


class CommitRequest(BaseModel):
    mensaje: str


@app.get("/")
def inicio():
    return {"mensaje": "API del clasificador de commits funcionando"}


@app.post("/clasificar")
def clasificar_commit(datos: CommitRequest):
    mensaje = datos.mensaje.lower()

    if mensaje.startswith("feat"):
        categoria = "feat"
    elif mensaje.startswith("fix"):
        categoria = "fix"
    elif mensaje.startswith("docs"):
        categoria = "docs"
    elif mensaje.startswith("test"):
        categoria = "test"
    elif mensaje.startswith("refactor"):
        categoria = "refactor"
    else:
        categoria = "chore"

    return {
        "mensaje": datos.mensaje,
        "categoria": categoria
    }
