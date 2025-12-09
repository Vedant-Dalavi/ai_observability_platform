from fastapi import FastAPI
from embed_and_store import router as search_router
from pydantic import BaseModel
from rag import run_rag



app = FastAPI()
app.include_router(search_router)

class RAGRequest(BaseModel):
    query: str

@app.post("/rag/query")
def rag_query(req: RAGRequest):
    return run_rag(req.query)