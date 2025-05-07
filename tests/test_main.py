from fastapi.testclient import TestClient
from app.main import app
from app.auth import create_jwt

client = TestClient(app)

headers = {
    "X-Parse-REST-API-Key": "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c",
    "X-JWT-KWY": create_jwt()
}

def test_post_success():
    response = client.post("/DevOps", json={
    "message": "This is a test",
    "to": "Juan Perez",
    "from": "Rita Asturia",
    "timeToLifeSec": 45
}, headers=headers)

    assert response.status_code == 200
    assert "message" in response.json()
    assert "Juan Perez" in response.json()["message"]

def test_missing_api_key():
    response = client.post("/DevOps", json={
        "message": "This is a test",
        "to": "Juan Perez",
        "from": "Rita Asturia",
        "timeToLifeSec": 45
    }, headers={"X-JWT-KWY": create_jwt()})

    assert response.status_code == 422 or response.status_code == 401

def test_invalid_method():
    response = client.get("/DevOps", headers=headers)
    assert response.status_code == 405
    assert response.json() == {"error": "ERROR"}

