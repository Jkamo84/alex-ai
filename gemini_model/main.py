from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from models import Chat
from pydantic import BaseModel
from tortoise import Tortoise, generate_config
from tortoise.contrib.fastapi import RegisterTortoise, tortoise_exception_handlers
from genai_handler import call_genai


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    config = generate_config(
        "sqlite://data/gemini.db",
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
    title="Gemini handler",
    lifespan=lifespan,
    exception_handlers=tortoise_exception_handlers(),
)


class ChatIn(BaseModel):
    name: str


@app.get("/chat/")
async def get_chat_by_id(id: str):
    chat = await Chat.get_or_none(id=id)
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")
    return {"id": chat.id, "name": chat.name}


@app.post("/chat/")
async def create_chat(chat_in: ChatIn):
    chat = await Chat.create(
        name=chat_in.username,
    )
    return {"id": chat.id}


@app.post("/message/")
async def execute_message(message: str):
    response = call_genai(message)
    return response
