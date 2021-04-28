from fastapi import FastAPI
import motor.motor_tornado
import motor.motor_asyncio
from server.query import DB
import pprint

app = FastAPI()

@app.get("/", tags=["Root"])
async def read_root():
    return ("MS_IA_ChatBot!")

@app.get("/find_one", tags=['1document'])
async def find_one(tag):
    response = await DB.find_one(tag)
    return response