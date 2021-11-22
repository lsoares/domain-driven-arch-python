import datetime
from abc import abstractmethod, ABC
from dataclasses import dataclass
from typing import List, Any

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import JSONResponse


@dataclass
class User:
    id: str
    email: str
    name: str
    password: str


class UserRepository(ABC):
    @abstractmethod
    def find_all(self) -> List[User]:
        pass

    @abstractmethod
    def save(self, user: User):
        pass


class CreateUserRequest(BaseModel):
    email: str
    name: str
    password: str


class CreateUser:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def handle(self, user: CreateUserRequest):
        self.user_repository.save(
            User(id=str(datetime.date.today()), email=user.email, name=user.name, password=user.password))
        return JSONResponse(
            status_code=201
        )


class ListUsers:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def handle(self):
        return JSONResponse(content=list(map(
            lambda u: {"name": u.name, "email": u.email},
            self.user_repository.find_all()
        )))


class WebApp(FastAPI):
    def __init__(self, user_repository: UserRepository, **extra: Any):
        super().__init__(**extra)
        self.create_user = CreateUser(user_repository=user_repository)
        self.list_users = ListUsers(user_repository=user_repository)

        super().add_api_route(path="/users", methods=['POST'],
                              endpoint=self.create_user.handle)
        super().add_api_route(path="/users", methods=['GET'],
                              endpoint=self.list_users.handle)


class UserRepositoryInMemory(UserRepository):
    store: List[User] = []

    def find_all(self) -> List[User]:
        return self.store.copy()

    def save(self, user: User):
        self.store.append(user)


app = WebApp(user_repository=UserRepositoryInMemory())
