from typing import List

from domain.User import User
from domain.UserRepository import UserRepository
from web.CreateUserHandler import EmailAlreadyExists


class UserRepositoryInMemory(UserRepository):
    store: List[User] = []

    def find_all(self) -> List[User]:
        return self.store.copy()

    def save(self, user: User):
        for u in self.store:
            if u.email == user.email:
                raise EmailAlreadyExists()

        self.store.append(user)
