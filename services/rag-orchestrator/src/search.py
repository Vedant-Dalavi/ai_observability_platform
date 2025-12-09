import requests
from qdrant_client import QdrantClient

client = QdrantClient(host="localhost", port=6333)

EMBED_URL = "http://localhost:8001/embed"
COLLECTION_NAME = "logs"
VECTOR_NAME = "embedding"

def retrieve_logs(query: str, top_k: int = 5):
    emb_resp = requests.post(EMBED_URL, json={"text": query}, timeout=10)
    emb_resp.raise_for_status()
    vector = emb_resp.json()["embedding"]

    results = client.query_points(
        collection_name = COLLECTION_NAME,
        query=vector,
        using = VECTOR_NAME,
        limit=top_k,
        with_payload=True,
        with_vectors=False,
    )

    results = results.points

    context = []
    for r in results:
        log = r.payload
        log["score"] = r.score
        context.append(log)

    return context
