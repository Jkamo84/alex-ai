from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from models import User
from pydantic import BaseModel
from tortoise import Tortoise, generate_config
from tortoise.contrib.fastapi import RegisterTortoise, tortoise_exception_handlers


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    config = generate_config(
        "sqlite://data/alex.db",
        app_modules={"models": ["models"]},
        testing=True,
        connection_label="models",
    )
    async with RegisterTortoise(
        app=app,
        config=config,
        generate_schemas=True,
        _create_db=True,
    ):
        # db connected
        yield
        # app teardown
    # db connections closed
    await Tortoise._drop_databases()


app = FastAPI(
    title="Tortoise ORM FastAPI example",
    lifespan=lifespan,
    exception_handlers=tortoise_exception_handlers(),
)


class UserIn(BaseModel):
    username: str
    email: str
    password: str


@app.post("/users/")
async def create_user(user_in: UserIn):
    user = await User.create(
        username=user_in.username,
        email=user_in.email,
        password_hash=user_in.password,  # In a real app, hash this password
    )
    return {"id": user.id, "username": user.username, "email": user.email}


@app.get("/users/{user_id}")
async def read_user(user_id: int):
    user = await User.get_or_none(id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user.id, "username": user.username, "email": user.email}
