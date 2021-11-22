from typing import List

from domain.User import User
from domain.UserRepository import UserRepository


class UserRepositoryInMemory(UserRepository):
    store: List[User] = []

    def find_all(self) -> List[User]:
        return self.store.copy()

    def save(self, user: User):
        self.store.append(user)
