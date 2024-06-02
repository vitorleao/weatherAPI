from fastapi.testclient import TestClient
from app.main import app, db

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Status": "Online"}

def test_read_city_valid():
    response = client.get("/city/Sao_Paulo")
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()["city"]["coord"]["lat"] is not None
    assert response.json()["city"]["coord"]["lon"] is not None
    assert db["external_data"].find_one() is not None

def test_read_city_invalid():
    response = client.get("/city/InvalidCity")
    assert response.status_code == 400
    assert response.json() == {"Error": "Please, inform a valid city name."}