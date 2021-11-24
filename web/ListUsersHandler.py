from dataclasses import dataclass
from starlette.responses import JSONResponse
from domain import ListUsers


@dataclass
class ListUsersHandler:
    list_users: ListUsers

    async def handle(self):
        return JSONResponse(content=list(map(
            lambda u: {"name": u.email, "email": u.name},
            self.list_users.invoke()
        )))
