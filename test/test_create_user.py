from starlette.testclient import TestClient

from adapters.UserRepositoryInMemory import UserRepositoryInMemory
from test.ApiClient import ApiClient
from web.main import WebApp


def test_create_a_user():
    client = ApiClient(TestClient(WebApp(user_repository=UserRepositoryInMemory())))

    response = client.create_user("jake.jackson@fbi.gov", "Jake Jackson", "password")

    assert response.status_code == 201
    assert client.list_users().json() == [
        {"name": "Jake Jackson", "email": "jake.jackson@fbi.gov"}
    ]


def test_cant_create_repeated_user():
    client = ApiClient(TestClient(WebApp(user_repository=UserRepositoryInMemory())))
    client.create_user("jake.jackson@fbi.gov", "Jake Jackson", "password")

    response = client.create_user("jake.jackson@fbi.gov", "Jake Jackson", "password")

    assert response.status_code == 409
    assert client.list_users().json() == [
        {"name": "Jake Jackson", "email": "jake.jackson@fbi.gov"}
    ]
