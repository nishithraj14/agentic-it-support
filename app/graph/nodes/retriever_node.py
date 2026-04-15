from app.rag.hybrid_retriever import hybrid_search
import logging

logging.basicConfig(level=logging.INFO)

def retrieve(state):
    ticket = state["ticket"]

    context, score = hybrid_search(ticket)

    if not context:
        score = 0.0

    logging.info(f"[RETRIEVER] score={score:.2f}")

    return {
        "context": context,
        "context_score": float(score)
    }