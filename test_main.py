from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Bored API.  Get your random activity by calling /types, /price  or /participants ."
    }


def test_read_types():
    response = client.get("/types/education")
    # print(response.status_code)
    assert response.status_code == 200
    full_payload = response.json()
    # print(full_payload)
    assert full_payload["result"]["type"] == "education"
