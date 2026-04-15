from langgraph.graph import StateGraph, END
from app.graph.state import AgentState

from app.graph.nodes.classifier import classify
from app.graph.nodes.retriever_node import retrieve
from app.graph.nodes.context_validator import validate_context
from app.graph.nodes.decision import decide
from app.graph.nodes.tool_selector import select_tool
from app.graph.nodes.resolver import resolve
from app.graph.nodes.escalation import escalate


def build_graph():
    graph = StateGraph(AgentState)

    # Nodes
    graph.add_node("classify", classify)
    graph.add_node("retrieve", retrieve)
    graph.add_node("validate", validate_context)
    graph.add_node("decide", decide)
    graph.add_node("tool", select_tool)
    graph.add_node("resolve", resolve)
    graph.add_node("escalate", escalate)

    # Entry
    graph.set_entry_point("classify")

    # Flow
    graph.add_edge("classify", "retrieve")
    graph.add_edge("retrieve", "validate")
    graph.add_edge("validate", "decide")

    # Decision routing
    graph.add_conditional_edges(
        "decide",
        lambda state: state["decision"],
        {
            "resolve": "tool",
            "escalate": "escalate"
        }
    )

    # Resolution path
    graph.add_edge("tool", "resolve")
    graph.add_edge("resolve", END)

    # Escalation path
    graph.add_edge("escalate", END)

    return graph.compile()