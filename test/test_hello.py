from starlette.testclient import TestClient

from main import app


def test_create_a_user():
    client = TestClient(app)

    response = _create_user(client, "luis.s@gmail.com", "Luís Soares", "password")

    assert response.status_code == 201
    assert _list_users(client).json() == [
        {"name": "Luís Soares", "email": "luis.s@gmail.com"}
    ]


def _create_user(client, email, name, password):
    return client.post(
        url="/users",
        json={"email": email, "name": name, "password": password}
    )


def _list_users(client):
    return client.get(url="/users")
