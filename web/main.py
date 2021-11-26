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

        create_user = CreateUserHandler(create_user=CreateUser(user_repository))
        list_users = ListUsersHandler(list_users=ListUsers(user_repository))
        delete_user = DeleteUserHandler(delete_user=DeleteUser(user_repository))

        self.add_api_route(path="/users", methods=['POST'], endpoint=create_user.handle)
        self.add_api_route(path="/users", methods=['GET'], endpoint=list_users.handle)
        self.add_api_route(path="/users/{email}", methods=['DELETE'], endpoint=delete_user.handle)


app = WebApp(user_repository=UserRepositoryInMemory())
