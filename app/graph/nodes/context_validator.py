import logging

logging.basicConfig(level=logging.INFO)


def validate_context(state):
    context = state.get("context", "")
    score = state.get("context_score", 0)

    logging.info(f"[VALIDATOR] length={len(context)}, score={score:.2f}")

    # Add signal only (no decision override)
    if not context or len(context) < 50:
        logging.warning("[VALIDATOR] Weak context detected")
        state["context_flag"] = "weak"

    elif score < 0.3:
        logging.warning("[VALIDATOR] Low relevance detected")
        state["context_flag"] = "low_score"

    else:
        state["context_flag"] = "good"

    return state