from dataclasses import dataclass

from starlette.responses import JSONResponse

from domain import DeleteUser


@dataclass
class DeleteUserHandler:
    delete_user: DeleteUser

    def __call__(self, email: str):
        self.delete_user(email)
        return JSONResponse(status_code=204)
