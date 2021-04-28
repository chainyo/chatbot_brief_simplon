from fastapi import FastAPI
import motor.motor_tornado
import motor.motor_asyncio
from server.query import DB
import pprint

app = FastAPI()

@app.get("/", tags=["Root"])
async def read_root():
    return ("MS_IA_ChatBot!")

@app.get("/find_answer", tags=['1document'])
async def find_answer(tag):
    response = await DB.find_answer(tag)
    return response


