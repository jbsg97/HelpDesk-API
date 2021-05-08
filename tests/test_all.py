import pytest
import json
from app.main import app
from async_asgi_testclient import TestClient


@pytest.fixture
async def client():
    async with TestClient(app) as client:
        yield client


@pytest.mark.asyncio
async def test_health_check(client):
    response = await client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Api working fine.."}


@pytest.mark.asyncio
async def test_fetch_clients(client):
    response = await client.get("/v1/ticket")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_fetch_client(client):
    response = await client.get("/v1/ticket/2")
    assert response.status_code == 200
    assert response.json() == {
        "title": "Fallo con el teclado",
        "body": "Tengo problemas con la tecla del espacio, ya que aveces no agarra.",
        "urgency": "Media",
        "status": "No visto"
    }
    
@pytest.mark.asyncio
async def test_fetch_client_fail(client):
    response = await client.get("/v1/ticket/1")
    assert response.status_code == 404
    assert response.json() == {"detail": "Ticket no encontrado."}


@pytest.mark.asyncio
async def test_insert_client(client):
    body = {
        "title": "test",
        "body": "test",
        "urgency": "test",
        "status": "test"
    }
    response = await client.post("/v1/ticket", data=json.dumps(body))
    assert response.status_code == 201
    assert response.json() == {"message": "Ticket creado con exito"}
    

@pytest.mark.asyncio
async def test_insert_client_fail(client):
    body = {
        "title": "test",
        "urgency": "test",
        "status": "test"
    }
    response = await client.post("/v1/ticket", data=json.dumps(body))
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
            "loc": [
                "body",
                "body"
            ],
            "msg": "field required",
            "type": "value_error.missing"
            }
        ]
    }
    
@pytest.mark.asyncio
async def test_update_client(client):
    body = {
        "title": "test-edit",
        "body": "test-edit",
        "urgency": "test-edit",
        "status": "test-edit"
    }
    response = await client.put("/v1/ticket/16", data=json.dumps(body))
    assert response.status_code == 200
    assert response.json() == body
    
    
@pytest.mark.asyncio
async def test_update_client_fail(client):
    body = {
        "title": "test-edit",
        "urgency": "test-edit",
        "status": "test-edit"
    }
    response = await client.put("/v1/ticket/16", data=json.dumps(body))
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
            "loc": [
                "body",
                "body"
            ],
            "msg": "field required",
            "type": "value_error.missing"
            }
        ]
    }
    

@pytest.mark.asyncio
async def test_delete_client_fail(client):
    response = await client.delete("/v1/ticket/1")
    assert response.status_code == 404
    assert response.json() == {"detail": "Error al eliminar ticket."}
    

@pytest.mark.asyncio
async def test_fetch_users(client):
    response = await client.get("/v1/user")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_fetch_user(client):
    response = await client.get("/v1/user/1")
    assert response.status_code == 200
    assert response.json() == {
        "id_user": 1,
        "username": "jbsg97",
        "password": "1793",
        "email": "jbsg@gmail.com",
        "name": "Jose Bryan",
        "last_name": "Sosa",
        "register_date": "2021-05-07",
        "disabled": 0
    }
    
@pytest.mark.asyncio
async def test_fetch_user_fail(client):
    response = await client.get("/v1/user/0")
    assert response.status_code == 404
    assert response.json() == {"detail": "Usuario no encontrado."}


@pytest.mark.asyncio
async def test_insert_user(client):
    body = {
        "username": "test",
        "password": "test",
        "email": "test@test.com",
        "name": "test",
        "last_name": "test",
        "disabled": 0
    }
    response = await client.post("/v1/user", data=json.dumps(body))
    assert response.status_code == 201
    assert response.json() == {"message": "Usuario creado con exito"}
    

@pytest.mark.asyncio
async def test_insert_user_fail(client):
    body = {
        "password": "test",
        "email": "test@test.com",
        "name": "test",
        "last_name": "test",
        "disabled": 0
    }
    response = await client.post("/v1/user", data=json.dumps(body))
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
            "loc": [
                "body",
                "username"
            ],
            "msg": "field required",
            "type": "value_error.missing"
            }
        ]
    }
    
@pytest.mark.asyncio
async def test_update_user(client):
    body = {
        "id_user": 3,
        "username": "test",
        "password": "test",
        "email": "test",
        "name": "test",
        "last_name": "test",
        "register_date": "2021-05-07",
        "disabled": 0
    }
    response = await client.put("/v1/user/3", data=json.dumps(body))
    assert response.status_code == 200
    assert response.json() == body
    
    
@pytest.mark.asyncio
async def test_update_user_fail(client):
    body = {
        "password": "test",
        "email": "test@test.com",
        "name": "test",
        "last_name": "test",
        "disabled": False
    }
    response = await client.put("/v1/user/3", data=json.dumps(body))
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
            "loc": [
                "body",
                "username"
            ],
            "msg": "field required",
            "type": "value_error.missing"
            }
        ]
    }
    

@pytest.mark.asyncio
async def test_delete_user_fail(client):
    response = await client.delete("/v1/user/0")
    assert response.status_code == 404
    assert response.json() == {"detail": "Error al eliminar al usuario."}
