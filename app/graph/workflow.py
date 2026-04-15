from langgraph.graph import StateGraph
from app.graph.state import AgentState

from app.graph.nodes.classifier import classify
from app.graph.nodes.retriever_node import retrieve
from app.graph.nodes.context_validator import validate_context
from app.graph.nodes.decision import decide
from app.graph.nodes.resolver import resolve
from app.graph.nodes.escalation import escalate


def build_graph():
    builder = StateGraph(AgentState)

    builder.add_node("classifier", classify)
    builder.add_node("retriever", retrieve)
    builder.add_node("validator", validate_context)
    builder.add_node("decision", decide)
    builder.add_node("resolver", resolve)
    builder.add_node("escalation", escalate)

    builder.set_entry_point("classifier")

    builder.add_edge("classifier", "retriever")
    builder.add_edge("retriever", "validator")
    builder.add_edge("validator", "decision")

    builder.add_conditional_edges(
        "decision",
        lambda state: state["decision"],
        {
            "resolve": "resolver",
            "escalate": "escalation"
        }
    )

    builder.set_finish_point("resolver")
    builder.set_finish_point("escalation")

    return builder.compile()