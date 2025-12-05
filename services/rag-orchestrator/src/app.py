from fastapi import FastAPI
from embed_and_store import router as search_router


app = FastAPI()
app.include_router(search_router)