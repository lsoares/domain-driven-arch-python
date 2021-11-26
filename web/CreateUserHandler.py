from dataclasses import dataclass

from pydantic import BaseModel
from starlette.responses import JSONResponse

from domain.CreateUser import CreateUser
from domain.UserRepository import EmailAlreadyExists


@dataclass
class CreateUserHandler:
    create_user: CreateUser

    class CreateRepresenter(BaseModel):
        email: str
        name: str
        password: str

    async def handle(self, user: CreateRepresenter):
        try:
            self.create_user.invoke(
                email=user.email,
                name=user.name,
                password=user.password,
            )
            return JSONResponse(status_code=201)
        except EmailAlreadyExists:
            return JSONResponse(status_code=409)
