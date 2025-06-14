import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    MILVUS_ENDPOINT = f"https://{os.getenv('MILVUS_ENDPOINT')}"
    MILVUS_API_KEY = os.getenv("MILVUS_API_KEY")
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    COLLECTION_NAME = "llm_paper"


settings = Settings()
