from pymilvus import MilvusClient
from app.config.settings import settings


class VectorStore:
    def __init__(self):
        self.client = MilvusClient(
            uri=settings.MILVUS_ENDPOINT,
            token=settings.MILVUS_API_KEY
        )

    async def search(self, embedding: list, limit: int = 5):
        return self.client.search(
            collection_name=settings.COLLECTION_NAME,
            anns_field="embeddings",
            data=[embedding],
            limit=limit,
            output_fields=["document_name", "chunk"]
        )


vector_store = VectorStore()
