from app.tools.registry import TOOL_REGISTRY
import logging

logging.basicConfig(level=logging.INFO)


def resolve(state):
    category = state.get("category")
    ticket = state.get("ticket")

    tool = TOOL_REGISTRY.get(category)

    if not tool:
        state["response"] = "No automation available. Escalating."
        state["decision"] = "escalate"
        return state

    try:
        result = tool(user="employee123")

        clean_response = f"""
✅ Issue Resolved

Category: {category}

Action Taken: {result.get("action")}

Message: {result.get("output", {}).get("message")}

Recommended Steps:
{state.get('context', '')[:300]}
"""

        state["response"] = clean_response.strip()
        state["status"] = "resolved"

        return state

    except Exception as e:
        state["response"] = f"Tool execution failed: {str(e)}"
        state["decision"] = "escalate"
        return state