from fastapi import FastAPI
from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from app.query import DB
from app.stemmer import Stemmer

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

@app.get("/api/v1/stemming", tags=['Preprocessing'])
async def get_stemming(input):
    return {'data': Stemmer.get_stemming(input)}