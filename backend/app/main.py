from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from starlette.responses import RedirectResponse
from json import load
from pydantic import BaseModel

from app.query import DB
from app.model.preprocessing import Preprocessing

import urllib.parse

class StemmingItem(BaseModel):
    item_content: str
    item_class: str
    item_id: int

app = FastAPI(
    title="API ChatBot Brief Simplon",
    description="Cette API est utilisé par notre Chatbot pour pouvoir communiquer.",
    version="1.0",
    openapi_url="/api/v1/openapi.json"
)

# Gestion des CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", include_in_schema=False)
async def home():
    return RedirectResponse("/docs")

@app.get("/api/v1/find_one", tags=['Réponse'])
async def find_one(tag):
    response = await DB.find_answer(tag)
    return response

@app.post("/api/v1/stemming", tags=['Preprocessing'])
async def get_stemming(input: StemmingItem):
    return {'data': Preprocessing.bag_of_words(input)}

@app.get("/api/v1/model", tags=['Model'])
async def get_model():
    with open(f"./app/model/tfjsmodel/model.json") as f:
        model = load(f)
    return model

@app.get("/api/v1/group1-shard1of1.bin", tags=['Model'])
async def get_shards():
    return FileResponse(path="./app/model/tfjsmodel/group1-shard1of1.bin")