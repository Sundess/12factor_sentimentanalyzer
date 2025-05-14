from fastapi.testclient import TestClient
from app.main import app  # Adjust path if your app is elsewhere

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Homepage"}
