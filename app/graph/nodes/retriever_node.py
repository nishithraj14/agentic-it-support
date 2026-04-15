from app.rag.hybrid_retriever import hybrid_search
import logging

def retrieve(state):
    ticket = state["ticket"]
    category = state.get("category")

    context = hybrid_search(ticket, category)

    logging.info(f"[RETRIEVER] category={category}, context_length={len(context)}")

    return {
        "context": context
    }