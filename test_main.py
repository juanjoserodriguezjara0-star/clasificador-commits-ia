
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_inicio():
    respuesta = client.get("/")
    assert respuesta.status_code == 200


def test_clasificar_feat():
    respuesta = client.post(
        "/clasificar",
        json={"mensaje": "feat: agregar inicio de sesión"}
    )
    assert respuesta.status_code == 200
    assert respuesta.json()["categoria"] == "feat"


def test_clasificar_fix():
    respuesta = client.post(
        "/clasificar",
        json={"mensaje": "fix: corregir error de acceso"}
    )
    assert respuesta.status_code == 200
    assert respuesta.json()["categoria"] == "fix"
