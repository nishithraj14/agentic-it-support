import os
import logging
from rank_bm25 import BM25Okapi
from app.rag.retriever import get_retriever

logging.basicConfig(level=logging.INFO)


# 📦 Load policy corpus
def load_corpus():
    docs = []
    path = "data/policies"

    for file in os.listdir(path):
        if file.endswith(".md"):
            with open(os.path.join(path, file), encoding="utf-8") as f:
                docs.append(f.read())

    logging.info(f"[BM25] Loaded {len(docs)} documents")
    return docs


corpus = load_corpus()
tokenized_corpus = [doc.split() for doc in corpus]

bm25 = BM25Okapi(tokenized_corpus)

# 🔍 Dense retriever (Neon DB)
dense_retriever = get_retriever()


# 🚀 FINAL HYBRID SEARCH
def hybrid_search(query: str):
    logging.info(f"[HYBRID] Query: {query}")

    # 🔹 1. Dense retrieval
    try:
        dense_docs = dense_retriever.invoke(query)
        dense_texts = [doc.page_content for doc in dense_docs]
    except Exception as e:
        logging.error(f"[HYBRID] Dense retrieval failed: {e}")
        dense_texts = []

    # 🔹 2. BM25 retrieval
    tokenized_query = query.split()
    bm25_scores = bm25.get_scores(tokenized_query)

    top_indices = sorted(
        range(len(bm25_scores)),
        key=lambda i: bm25_scores[i],
        reverse=True
    )[:3]

    bm25_docs = [corpus[i] for i in top_indices]

    # 🔹 3. Combine results
    combined = dense_texts + bm25_docs

    # 🔹 4. Remove duplicates
    seen = set()
    unique_docs = []

    for doc in combined:
        if doc not in seen:
            seen.add(doc)
            unique_docs.append(doc)

    # 🔹 5. Simple ranking (NO LLM → fast)
    final_docs = unique_docs[:2]

    # 🔹 6. Build context
    context = "\n\n".join(final_docs)

    # 🔹 7. Score (simple heuristic)
    context_score = min(len(context) / 500, 1.0)

    logging.info(f"[HYBRID] Retrieved {len(final_docs)} docs, score={context_score:.2f}")

    return context, context_score