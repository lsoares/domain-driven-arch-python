from typing import Any

from fastapi import FastAPI

from adapters.UserRepositoryInMemory import UserRepositoryInMemory
from domain.CreateUser import CreateUser
from domain.ListUsers import ListUsers
from domain.UserRepository import UserRepository
from web.CreateUserHandler import CreateUserHandler
from web.ListUsersHandler import ListUsersHandler


class WebApp(FastAPI):
    def __init__(self, user_repository: UserRepository, **extra: Any):
        super().__init__(**extra)

        create_user = CreateUserHandler(create_user=CreateUser(user_repository))
        list_users = ListUsersHandler(list_users=ListUsers(user_repository))

        self.add_api_route(path="/users", methods=['POST'], endpoint=create_user.handle)
        self.add_api_route(path="/users", methods=['GET'], endpoint=list_users.handle)


app = WebApp(user_repository=UserRepositoryInMemory())
