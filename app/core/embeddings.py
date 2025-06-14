from pymilvus import model
from app.config.settings import settings

class EmbeddingService:
    def __init__(self):
        self.model = model.dense.GeminiEmbeddingFunction(
            model_name="text-embedding-004",
            api_key=settings.GOOGLE_API_KEY,
        )

    def encode(self, text: str) -> list:
        return self.model.encode_documents([text])[0]

embedding_service = EmbeddingService()