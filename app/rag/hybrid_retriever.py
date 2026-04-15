from app.rag.retriever import get_retriever
from rank_bm25 import BM25Okapi
import os

# ---------------- LOAD CORPUS ----------------
def load_corpus():
    docs = []
    path = "data/policies"

    for file in os.listdir(path):
        if file.endswith(".md"):
            with open(os.path.join(path, file), encoding="utf-8") as f:
                docs.append({
                    "text": f.read(),
                    "name": file.lower()
                })

    return docs


corpus = load_corpus()
tokenized = [doc["text"].split() for doc in corpus]

bm25 = BM25Okapi(tokenized)
dense = get_retriever()

# ---------------- CATEGORY → FILE FILTER ----------------
CATEGORY_FILE_MAP = {
    "vpn_issue": ["vpn"],
    "network_issue": ["network", "wifi"],
    "password_reset": ["password"],
    "device_issue": ["device", "bsod", "hardware"],
    "email_issue": ["email"],
    "access_request": ["access"]
}


# ---------------- FILTER FUNCTION ----------------
def filter_by_category(category):
    if not category:
        return corpus

    keywords = CATEGORY_FILE_MAP.get(category, [])

    filtered = [
        doc for doc in corpus
        if any(k in doc["name"] for k in keywords)
    ]

    return filtered if filtered else corpus


# ---------------- HYBRID SEARCH ----------------
def hybrid_search(query: str, category: str = None):

    # 🔴 STRICT FILTER FIRST
    filtered_docs = filter_by_category(category)

    texts = [doc["text"] for doc in filtered_docs]
    tokenized_local = [doc.split() for doc in texts]

    bm25_local = BM25Okapi(tokenized_local)

    # BM25
    scores = bm25_local.get_scores(query.split())
    top_idx = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:3]

    bm25_docs = [texts[i] for i in top_idx]

    # Dense
    dense_docs = dense.invoke(query)
    dense_texts = [doc.page_content for doc in dense_docs]

    # Merge
    combined = bm25_docs + dense_texts

    # Remove duplicates
    seen = set()
    final = []

    for doc in combined:
        if doc not in seen:
            seen.add(doc)
            final.append(doc[:400])

    return "\n\n".join(final[:3])