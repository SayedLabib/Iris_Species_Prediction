from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_predict_endpoint():
    response = client.post("/predict", json={"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2})
    assert response.status_code == 200
    assert "species" in response.json()

def test_invalid_predict_endpoint():
    response = client.post("/predict", json={"sepal_length": "invalid", "sepal_width": 3.5})
    assert response.status_code == 422