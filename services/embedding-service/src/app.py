from fastapi import FastAPI
from pydantic import BaseModel
from embedder import embed_text

app = FastAPI()

class EmbedRequest(BaseModel):
    text: str

class EmbedResponse(BaseModel):
    embedding: list[float]
    dimensions: int

@app.post("/embed", response_model=EmbedResponse)
def embed_endpoint(req:EmbedRequest):
    vector = embed_text(req.text)
    return {"embedding":vector, "dimensions": len(vector)}