import traceback
import requests
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from qdrant_client import QdrantClient

router = APIRouter()

client = QdrantClient(host="localhost", port=6333, check_compatibility=False)
EMBED_URL = "http://localhost:8001/embed"
COLLECTION_NAME = "logs"
VECTOR_NAME = "embedding"  # matches your vectors_config

class SearchRequest(BaseModel):
    query: str
    top_k: int = 5

@router.post("/search")
def semantic_search(req: SearchRequest):
    try:
        emb_resp = requests.post(EMBED_URL, json={"text": req.query}, timeout=10)
        emb_resp.raise_for_status()
        vector = emb_resp.json()["embedding"]

        results = client.query_points(
            collection_name=COLLECTION_NAME,
            query=vector,
            using=VECTOR_NAME,
            limit=req.top_k,
            with_payload=True,
            with_vectors=False,
        )
        points = results.points  # list[ScoredPoint]

        matches = []
        for p in points:
            payload = p.payload or {}
            matches.append({
                "score": p.score,
                "service": payload.get("service"),
                "message": payload.get("message"),
                "level": payload.get("level"),
                "timestamp": payload.get("timestamp"),
            })

        return {"matches": matches}

    except requests.RequestException as e:
        traceback.print_exc()
        raise HTTPException(status_code=502, detail=f"Embedding service error: {e}")
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
