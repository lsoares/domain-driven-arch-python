from typing import List

from domain.User import User
from domain.UserRepository import UserRepository, EmailAlreadyExists


class UserRepositoryInMemory(UserRepository):
    _store: List[User] = []

    def find_all(self) -> List[User]:
        return self._store.copy()

    def save(self, user: User):
        for u in self._store:
            if u.email == user.email:
                raise EmailAlreadyExists()
        self._store.append(user)

    def delete(self, email: str):
        self._store.remove(next(user for user in self._store if user.email == email))
