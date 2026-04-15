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

# ---------------- CATEGORY MAP ----------------
CATEGORY_FILE_MAP = {
    "vpn_issue": ["vpn"],
    "network_issue": ["network", "wifi"],
    "password_reset": ["password"],
    "device_issue": ["device", "disk", "performance"],
    "email_issue": ["email"],
    "access_request": ["access", "database"]
}


# ---------------- FILTER ----------------
def filter_by_category(category):
    if not category:
        return []

    keywords = CATEGORY_FILE_MAP.get(category, [])

    filtered = [
        doc for doc in corpus
        if any(k in doc["name"] for k in keywords)
    ]

    return filtered


# ---------------- HYBRID SEARCH ----------------
def hybrid_search(query: str, category: str = None):

    # 🔴 STRICT FILTER
    filtered_docs = filter_by_category(category)

    if not filtered_docs:
        return "No relevant policy found"

    texts = [doc["text"] for doc in filtered_docs]

    tokenized = [doc.split() for doc in texts]
    bm25 = BM25Okapi(tokenized)

    scores = bm25.get_scores(query.split())

    top_idx = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:2]

    results = [texts[i] for i in top_idx]

    return "\n\n".join(results)