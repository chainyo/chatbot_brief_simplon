import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse
from query import DB

app = FastAPI()

@app.get("/", tags=["Root"])
async def read_root():
    return RedirectResponse("/docs")

@app.get("/find_one", tags=['1document'])
async def find_one(tag):
    response = await DB.find_answer(tag)
    return response
