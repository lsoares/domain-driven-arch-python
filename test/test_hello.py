from starlette.testclient import TestClient

from main import app


def test_hello_world():
    client = TestClient(app)

    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"hello": "dear"}
