from fastapi import FastAPI
from starlette.responses import RedirectResponse
from query import DB

app = FastAPI(
    title="API ChatBot Brief Simplon",
    description="Cette API est utilisé par notre Chatbot pour pouvoir communiquer.",
    version="1.0",
    openapi_url="/api/v1/openapi.json"
)

@app.get("/", include_in_schema=False)
async def home():
    return RedirectResponse("/docs")

@app.get("/api/v1/find_one", tags=['Réponse'])
async def find_one(tag):
    response = await DB.find_answer(tag)
    return response
