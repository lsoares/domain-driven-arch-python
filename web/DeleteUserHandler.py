from dataclasses import dataclass

from starlette.responses import JSONResponse

from domain import DeleteUser


@dataclass
class DeleteUserHandler:
    delete_user: DeleteUser

    async def handle(self, email: str):
        self.delete_user.invoke(email)
        return JSONResponse(status_code=204)
