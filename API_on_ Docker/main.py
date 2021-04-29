import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse
from query import DB

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


app = FastAPI()

@app.get("/", tags=["Root"])
async def read_root():
    return RedirectResponse("/docs")

@app.get("/find_one", tags=['1document'])
async def find_one(tag):
    response = await DB.find_answer(tag)
    return response