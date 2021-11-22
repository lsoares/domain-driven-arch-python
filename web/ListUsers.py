from starlette.responses import JSONResponse

from domain.UserRepository import UserRepository


class ListUsers:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def handle(self):
        return JSONResponse(content=list(map(
            lambda u: {"name": u.name, "email": u.email},
            self.user_repository.find_all()
        )))
