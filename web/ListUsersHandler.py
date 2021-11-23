from dataclasses import dataclass
from starlette.responses import JSONResponse
from domain import ListUsers


@dataclass
class ListUsersHandler:
    list_users: ListUsers

    async def handle(self):
        return JSONResponse(content=list(map(
            lambda u: {"name": u.name, "email": u.email},
            self.list_users.invoke()
        )))
