import datetime
from dataclasses import dataclass

from domain import UserRepository
from domain.User import User


@dataclass
class CreateUser:
    user_repository: UserRepository

    def __call__(self, email: str, name: str, password: str):
        self.user_repository.save(User(
            id=str(datetime.date.today()),
            email=email,
            name=name,
            password=password,
        ))
