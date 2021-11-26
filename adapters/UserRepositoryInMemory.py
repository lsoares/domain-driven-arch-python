from typing import List, Dict

from domain.User import User
from domain.UserRepository import UserRepository, EmailAlreadyExists


class UserRepositoryInMemory(UserRepository):
    _store: Dict[str, User] = {}

    def find_all(self) -> List[User]:
        return list(self._store.values()).copy()

    def save(self, user: User):
        if user.email in self._store.keys():
            raise EmailAlreadyExists()
        self._store[user.email] = user

    def delete(self, email: str):
        self._store.pop(email)
