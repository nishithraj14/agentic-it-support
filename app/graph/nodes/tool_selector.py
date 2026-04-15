def select_tool(state):
    from app.tools.registry import TOOL_REGISTRY

    category = state.get("category")
    tool = TOOL_REGISTRY.get(category)

    state["tool"] = tool
    return state