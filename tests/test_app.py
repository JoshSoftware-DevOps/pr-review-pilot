import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_get_existing_user(client):
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.get_json()["name"] == "Alice"

def test_get_missing_user(client):
    response = client.get("/users/999")
    assert response.status_code == 404
