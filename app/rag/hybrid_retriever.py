import os
from rank_bm25 import BM25Okapi

# ---------------- LOAD CORPUS ----------------
def load_corpus():
    docs = []
    base_path = "data/policies"

    for file in os.listdir(base_path):
        if file.endswith(".md"):
            with open(os.path.join(base_path, file), encoding="utf-8") as f:
                docs.append({
                    "text": f.read(),
                    "name": file.lower()
                })

    return docs


corpus = load_corpus()

# ---------------- CATEGORY MAPPING ----------------
CATEGORY_FILE_MAP = {
    "vpn_issue": ["vpn"],
    "network_issue": ["network", "wifi"],
    "password_reset": ["password"],
    "account_unlock": ["account", "password"],
    "device_issue": ["device", "disk", "performance"],
    "email_issue": ["email"],
    "access_request": ["access", "software", "database", "jira"]
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

    # Controlled fallback (domain-safe)
    if not filtered and category == "account_unlock":
        filtered = [
            doc for doc in corpus
            if "password" in doc["name"]
        ]

    return filtered


# ---------------- RETRIEVAL ----------------
def hybrid_search(query: str, category: str = None):

    filtered_docs = filter_by_category(category)

    if not filtered_docs:
        return "No relevant policy found"

    texts = [doc["text"] for doc in filtered_docs]

    # BM25
    tokenized = [doc.split() for doc in texts]
    bm25 = BM25Okapi(tokenized)

    scores = bm25.get_scores(query.lower().split())

    top_idx = sorted(
        range(len(scores)),
        key=lambda i: scores[i],
        reverse=True
    )[:3]

    results = [texts[i] for i in top_idx]

    # Lightweight semantic rerank (keyword density)
    results = sorted(
        results,
        key=lambda d: sum(word in d.lower() for word in query.lower().split()),
        reverse=True
    )

    return "\n\n".join(results[:2])