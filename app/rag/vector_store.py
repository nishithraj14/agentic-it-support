import os
from dotenv import load_dotenv
from langchain_community.vectorstores import PGVector
from app.rag.embeddings import get_embeddings

# ✅ LOAD ENV HERE (CRITICAL)
load_dotenv()

def get_vector_store():
    connection_string = os.getenv("DATABASE_URL")

    if not connection_string:
        raise ValueError("❌ DATABASE_URL not found. Check your .env file")

    return PGVector(
        connection_string=connection_string,
        embedding_function=get_embeddings(),
        collection_name="it_support_docs"
    )