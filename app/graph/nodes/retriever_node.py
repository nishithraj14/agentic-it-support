from app.rag.hybrid_retriever import hybrid_search

def retrieve(state):
    ticket = state["ticket"]
    category = state.get("category")

    context = hybrid_search(ticket, category)

    return {"context": context}