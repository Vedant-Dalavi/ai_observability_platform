from fastapi import APIRouter
from pydantic import BaseModel
from qdrant_client import QdrantClient
import requests
import traceback
router = APIRouter()
client = QdrantClient(host="localhost", port=6333)

EMBED_URL = "http://localhost:8001/embed"

class SearchRequest(BaseModel):
    query: str
    top_k: int = 5

@router.post("/search")
def semantic_search(req:SearchRequest):
    try:
        vector = requests.post(EMBED_URL,json={"text":req.query}).json()["embedding"]
        
        results = client.query_points(
            collection_name = "logs",
            query = vector,
            limit = req.top_k
        )

        return { "matches":[
            {
                "score": r.score,
                "service": r.payload["service"],
                "message": r.payload["message"],
                "level": r.payload["level"],
                "timestamp": r.payload["timestamp"]
            }
            for r in results
        ]
        }
    except Exception as e:
        traceback.print_exc()
        print("error: ",e)