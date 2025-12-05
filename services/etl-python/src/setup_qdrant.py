from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

client = QdrantClient(host="localhost", port=6333)

client.recreate_collection(
    collection_name="logs",
    vectors_config={
        "embedding": VectorParams(size=384, distance=Distance.COSINE)
    }
)

print("Created collection 'logs'")