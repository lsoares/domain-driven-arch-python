from dataclasses import dataclass

from starlette.testclient import TestClient

from adapters.UserRepositoryInMemory import UserRepositoryInMemory
from test.ApiClient import ApiClient
from web.main import WebApp


def test_delete_a_user():
    client = ApiClient(TestClient(WebApp(user_repository=UserRepositoryInMemory())))
    client.create_user("jake.jackson@fbi.gov", "Jake Jackson", "password")
    client.create_user("john.doe@gmail.com", "John Doe", "password")

    response = client.delete_user("jake.jackson@fbi.gov")

    assert response.status_code == 204
    assert client.list_users().json() == [
        {"name": "John Doe", "email": "john.doe@gmail.com"}
    ]
