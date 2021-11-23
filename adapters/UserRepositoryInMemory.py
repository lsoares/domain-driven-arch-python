from typing import List

from domain.User import User
from domain.UserRepository import UserRepository


class UserRepositoryInMemory(UserRepository):
    _store: List[User] = []

    def find_all(self) -> List[User]:
        return self._store.copy()

    def save(self, user: User):
        self._store.append(user)
