from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

class Items(BaseModel):
    nombre: str
    edad: int

app = FastAPI()

@app.post("/tests")
async def read_item(items: Items):
    return {"nombre": items.nombre, "edad": items.edad}

app.mount("/", StaticFiles(directory="static",html = True), name="static")