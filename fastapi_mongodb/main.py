from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel

# MongoDB connection details
MONGO_DETAILS = "mongodb://localhost:27017"  # Replace with your connection string


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    app.mongodb_client = AsyncIOMotorClient(MONGO_DETAILS)
    app.mongodb = app.mongodb_client.local
    yield
    app.mongodb_client.close()


app = FastAPI(
    title="MongoDB FastAPI example",
    lifespan=lifespan,
)


class Item(BaseModel):
    name: str


@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    new_item = await app.mongodb.alex.insert_one(item.dict())
    return item


@app.get("/items/{name}", response_model=Item)
async def get_item_by_name(name: str):
    # item = await app.mongodb.alex.find_one({"_id": item_id})
    item = await app.mongodb.alex.find_one({"name": name})

    return Item(**item)
