import datetime

from pydantic import BaseModel
from starlette.responses import JSONResponse

from domain.User import User
from domain.UserRepository import UserRepository


class CreateUser:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    class CreateRepresenter(BaseModel):
        email: str
        name: str
        password: str

    async def handle(self, user: CreateRepresenter):
        self.user_repository.save(User(
            id=str(datetime.date.today()),
            email=user.email, name=user.name,
            password=user.password,
        ))
        return JSONResponse(
            status_code=201
        )
