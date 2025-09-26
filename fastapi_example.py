from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()  # service created


class Item(BaseModel):  # model to handle data/payloads
    name: str  # has to be a string
    description: str | None = None  # can be a string or null, if not given, is null
    price: float
    tax: float | None = None


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/items/")  # name of the endpoint
async def create_item(item: Item):
    # actions that can happen in endpoint call
    # limpiar el texto que envia el usuario
    # comunicar con el llm
    # se genera un archivo pdf (el informe)
    # se sube el archivo a la DB de archivos
    # guardar lo que escribio el usuario al historial del chat (DB)
    return (
        item  # respuesta del LLM, con la indicacion de que puede descargar un archivo
    )
