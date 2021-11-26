from dataclasses import dataclass

from starlette.testclient import TestClient


@dataclass
class ApiClient:
    client: TestClient

    def delete_user(self, email: str):
        return self.client.delete(url=f"/users/{email}")

    def create_user(self, email: str, name: str, password: str):
        return self.client.post(
            url="/users",
            json={"email": email, "name": name, "password": password}
        )

    def list_users(self):
        return self.client.get(url="/users")
