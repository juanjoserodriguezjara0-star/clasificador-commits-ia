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
    assert respuesta.json()["version"] == "1.0.0"


def test_health_informa_dependencias(monkeypatch):
    monkeypatch.setattr(main.requests, "get", lambda *args, **kwargs: type(
        "Respuesta", (), {"raise_for_status": lambda self: None}
    )())
    monkeypatch.setattr(main, "conectar_db", lambda: type(
        "Conexion", (), {
            "__enter__": lambda self: self,
            "__exit__": lambda self, *args: None,
            "cursor": lambda self: type(
                "Cursor", (), {
                    "__enter__": lambda self: self,
                    "__exit__": lambda self, *args: None,
                    "execute": lambda self, *args: None,
                    "fetchone": lambda self: (1,),
                }
            )(),
        }
    )())
    respuesta = client.get("/health")
    assert respuesta.status_code == 200
    assert respuesta.json()["estado"] == "ok"
    assert respuesta.json()["ollama"] == "ok"
    assert respuesta.json()["postgresql"] == "ok"


def test_clasificar_feat(monkeypatch):
    monkeypatch.setattr(
        main.requests,
        "post",
        lambda *args, **kwargs: RespuestaFalsa("feat"),
    )
    monkeypatch.setattr(
        main,
        "guardar_inferencia",
        lambda mensaje, categoria: {
            "id": 1,
            "mensaje": mensaje,
            "categoria": categoria,
            "creada_en": "2026-01-01T00:00:00+00:00",
        },
    )
    respuesta = client.post(
        "/clasificar",
        json={"mensaje": "feat: agregar inicio de sesión"},
    )
    assert respuesta.status_code == 200
    assert respuesta.json()["categoria"] == "feat"
    assert respuesta.json()["id"] == 1


def test_clasificar_fix(monkeypatch):
    monkeypatch.setattr(
        main.requests,
        "post",
        lambda *args, **kwargs: RespuestaFalsa("fix"),
    )
    monkeypatch.setattr(
        main,
        "guardar_inferencia",
        lambda mensaje, categoria: {
            "id": 2,
            "mensaje": mensaje,
            "categoria": categoria,
            "creada_en": "2026-01-01T00:00:00+00:00",
        },
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


def test_rechaza_mensaje_demasiado_largo():
    respuesta = client.post("/clasificar", json={"mensaje": "x" * 2001})
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


def test_postgresql_no_disponible_al_guardar(monkeypatch):
    monkeypatch.setattr(
        main.requests,
        "post",
        lambda *args, **kwargs: RespuestaFalsa("docs"),
    )

    def fallo_db(mensaje, categoria):
        raise main.psycopg.OperationalError("sin conexión")

    monkeypatch.setattr(main, "guardar_inferencia", fallo_db)
    respuesta = client.post(
        "/clasificar",
        json={"mensaje": "docs: actualizar manual"},
    )
    assert respuesta.status_code == 503


def test_listar_inferencias(monkeypatch):
    monkeypatch.setattr(
        main,
        "obtener_inferencias",
        lambda limite: [{"id": 1, "mensaje": "fix: corregir", "categoria": "fix",
                         "creada_en": "2026-01-01T00:00:00+00:00"}],
    )
    respuesta = client.get("/inferencias?limite=10")
    assert respuesta.status_code == 200
    assert respuesta.json()["total"] == 1
    assert respuesta.json()["inferencias"][0]["categoria"] == "fix"


def test_limite_inferencias_fuera_de_rango():
    respuesta = client.get("/inferencias?limite=101")
    assert respuesta.status_code == 422
