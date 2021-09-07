# Author: CptR3dBeard
# put is modifier
# get is reciveing input
# post is sending

# imported Libraries

from fastapi import FastAPI
from main import *
import asyncio
import pydantic

app = FastAPI()


@app.get("/")
def home():
    return {"Data": "Wow!"}

@app.delete("/delete/{column}/{entry}")
async def delete(column: str, entry: str):
    await remove(column, entry)
    return {"test": "test"}


@app.post("/add/{value1}/{value2}")
async def add(value1: str, value2: str):
    await insert(value1, value2)
    return {"test": "test"}


@app.post("/update/{col}/{old}/{new}")
async def modify(col, old, new):
    await update(col, old, new)
    return {"test": "test"}
