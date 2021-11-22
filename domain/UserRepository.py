from abc import ABC, abstractmethod
from typing import List

from domain.User import User


class UserRepository(ABC):
    @abstractmethod
    def find_all(self) -> List[User]:
        pass

    @abstractmethod
    def save(self, user: User):
        pass
