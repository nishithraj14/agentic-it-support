import os
from dotenv import load_dotenv

# ✅ Load environment variables
load_dotenv()

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.rag.vector_store import get_vector_store

DATA_PATH = "data/policies"


def load_documents():
    docs = []

    if not os.path.exists(DATA_PATH):
        print(f"[ERROR] Data path not found: {DATA_PATH}")
        return docs

    for file in os.listdir(DATA_PATH):
        if file.endswith(".md"):
            file_path = os.path.join(DATA_PATH, file)

            try:
                # ✅ UTF-8 fix for encoding issues
                loader = TextLoader(file_path, encoding="utf-8")
                loaded_docs = loader.load()

                for doc in loaded_docs:
                    doc.metadata["source"] = file

                docs.extend(loaded_docs)

            except Exception as e:
                print(f"[ERROR] Failed to load {file}: {e}")

    return docs


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    return splitter.split_documents(documents)


def ingest():
    print("[INFO] Starting ingestion...")

    docs = load_documents()

    if not docs:
        print("[ERROR] No documents loaded.")
        return

    print(f"[INFO] Loaded {len(docs)} documents")

    chunks = split_documents(docs)

    if not chunks:
        print("[ERROR] No chunks created.")
        return

    print(f"[INFO] Split into {len(chunks)} chunks")

    try:
        vector_store = get_vector_store()
        vector_store.add_documents(chunks)

        print("[SUCCESS] Data successfully ingested into Neon DB")

    except Exception as e:
        print(f"[ERROR] Failed to store embeddings: {e}")


if __name__ == "__main__":
    ingest()