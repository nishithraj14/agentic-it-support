import logging

def validate_context(state):
    context = state.get("context", "")

    if not context or "No relevant policy" in context:
        logging.info("[VALIDATOR] No valid context")
        return {
            "context_valid": False,
            "context_score": 0.0
        }

    length = len(context)

    # Heuristic scoring
    if length > 800:
        score = 0.9
    elif length > 300:
        score = 0.7
    else:
        score = 0.5

    logging.info(f"[VALIDATOR] length={length}, score={score}")

    return {
        "context_valid": True,
        "context_score": score
    }