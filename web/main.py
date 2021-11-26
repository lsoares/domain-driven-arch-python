from typing import Any

from fastapi import FastAPI

from adapters.UserRepositoryInMemory import UserRepositoryInMemory
from domain.CreateUser import CreateUser
from domain.DeleteUser import DeleteUser
from domain.ListUsers import ListUsers
from domain.UserRepository import UserRepository
from web.CreateUserHandler import CreateUserHandler
from web.DeleteUserHandler import DeleteUserHandler
from web.ListUsersHandler import ListUsersHandler


class WebApp(FastAPI):
    def __init__(self, user_repository: UserRepository, **extra: Any):
        super().__init__(**extra)

        self.add_api_route(
            path="/users", methods=['POST'],
            endpoint=CreateUserHandler(CreateUser(user_repository)),
        )
        self.add_api_route(
            path="/users", methods=['GET'],
            endpoint=ListUsersHandler(ListUsers(user_repository)),
        )
        self.add_api_route(
            path="/users/{email}", methods=['DELETE'],
            endpoint=DeleteUserHandler(DeleteUser(user_repository)),
        )


app = WebApp(user_repository=UserRepositoryInMemory())
