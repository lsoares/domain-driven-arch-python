from typing import Optional
from fastapi import FastAPI
from starlette.responses import JSONResponse


async def get_user():
    return JSONResponse(content={"hello": "dear"})


app = FastAPI()
app.add_api_route(path="/", endpoint=get_user, methods=['GET'])
