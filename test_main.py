from fastapi.testclient import TestClient

import main


client = TestClient(main.app)


class RespuestaFalsa:
    def __init__(self, categoria):
        self.categoria = categoria

    def raise_for_status(self):
        return None

    def json(self):
        return {"response": self.categoria}


def test_inicio():
    respuesta = client.get("/")
    assert respuesta.status_code == 200
    assert "funcionando" in respuesta.json()["mensaje"]


def test_health():
    respuesta = client.get("/health")
    assert respuesta.status_code == 200
    assert respuesta.json()["estado"] == "ok"


def test_clasificar_feat(monkeypatch):
    monkeypatch.setattr(
        main.requests,
        "post",
        lambda *args, **kwargs: RespuestaFalsa("feat"),
    )
    respuesta = client.post(
        "/clasificar",
        json={"mensaje": "feat: agregar inicio de sesión"},
    )
    assert respuesta.status_code == 200
    assert respuesta.json()["categoria"] == "feat"


def test_clasificar_fix(monkeypatch):
    monkeypatch.setattr(
        main.requests,
        "post",
        lambda *args, **kwargs: RespuestaFalsa("fix"),
    )
    respuesta = client.post(
        "/clasificar",
        json={"mensaje": "fix: corregir error de acceso"},
    )
    assert respuesta.status_code == 200
    assert respuesta.json()["categoria"] == "fix"


def test_rechaza_mensaje_vacio():
    respuesta = client.post("/clasificar", json={"mensaje": ""})
    assert respuesta.status_code == 422


def test_ollama_no_disponible(monkeypatch):
    def fallo_conexion(*args, **kwargs):
        raise main.requests.ConnectionError("sin conexión")

    monkeypatch.setattr(main.requests, "post", fallo_conexion)
    respuesta = client.post(
        "/clasificar",
        json={"mensaje": "fix: corregir error"},
    )
    assert respuesta.status_code == 503
