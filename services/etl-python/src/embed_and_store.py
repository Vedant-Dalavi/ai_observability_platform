import requests
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
import pandas as pd
import uuid

client = QdrantClient(host="localhost", port=6333)

EMBED_URL = "http://localhost:8001/embed"

def embed(text: str):
    res = requests.post(EMBED_URL, json = {"text":text})
    return res.json()["embedding"]

def process_parquet():
    df = pd.read_parquet("D:/ml_projects/ai_observability_platform/services/storage/bronze/logs.parquet")

    points = []

    for _, row in df.iterrows():
        vector = embed(row["message"])
        print("row:", row)
        point = PointStruct(
            id = str(uuid.uuid4()),
            vector = {"embedding":list(vector)},
            payload = {
                "service": row["service"],
                "level":row["level"],
                "message": row["message"],
                "timestamp": row["timestamp"]
            }
        )

        points.append(point)

    client.upsert(collection_name = "logs", points = points)
    print(f"Inserted {len(points)} vecotrs into Qdrant")


process_parquet()