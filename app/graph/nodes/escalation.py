def escalate(state):
    return {
        "response": {
            "status": "escalated",
            "reason": "low confidence or high risk",
            "ticket": state.get("ticket")
        }
    }