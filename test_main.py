from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_crear_cliente():
    respuesta = client.post("/cliente", json={
        "nombre": "Juan Pérez",
        "telefono": "3101234567",
        "localidad": "Bosa",
        "activo": True
    })
    assert respuesta.status_code == 200
    assert respuesta.json()["nombre"] == "Juan Pérez"

def test_listar_clientes():
    respuesta = client.get("/cliente")
    assert respuesta.status_code == 200
    assert isinstance(respuesta.json(), list)

def test_buscar_cliente_existente():
    respuesta = client.get("/cliente/1")
    assert respuesta.status_code == 200

def test_cliente_no_existe():
    respuesta = client.get("/cliente/99999")
    assert respuesta.status_code == 404

def test_modificar_cliente():
    respuesta = client.patch("/cliente/1", json={
        "telefono": "3209999999"
    })
    assert respuesta.status_code == 200
    assert respuesta.json()["telefono"] == "3209999999"

def test_crear_solicitud_cliente_inexistente():
    respuesta = client.post("/solicitud", json={
        "tipo_ayuda": "kit_visual",
        "observaciones": "Prueba",
        "cliente_id": 99999
    })
    assert respuesta.status_code == 404

def test_solicitud_no_existe():
    respuesta = client.get("/solicitud/99999")
    assert respuesta.status_code == 404