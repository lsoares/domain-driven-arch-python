from dataclasses import dataclass

from domain import UserRepository


@dataclass
class DeleteUser:
    user_repository: UserRepository

    def __call__(self, email: str):
        self.user_repository.delete(email)
