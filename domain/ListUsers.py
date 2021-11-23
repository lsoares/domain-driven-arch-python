from dataclasses import dataclass
from typing import List

from domain.User import User
from domain.UserRepository import UserRepository


@dataclass
class ListUsers:
    user_repository: UserRepository

    def invoke(self) -> List[User]:
        return self.user_repository.find_all()
