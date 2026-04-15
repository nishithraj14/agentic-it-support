import logging

HIGH_RISK = ["access_request"]

def decide(state):
    category = state.get("category")
    confidence = state.get("confidence", 0)
    context_valid = state.get("context_valid", False)
    context_score = state.get("context_score", 0)

    logging.info(
        f"[DECISION] category={category}, confidence={confidence}, context_score={context_score}"
    )

    # 🔴 Always escalate high-risk actions
    if category in HIGH_RISK:
        logging.info("[DECISION] → escalate (high-risk category)")
        return {"decision": "escalate"}

    # ✅ Strong auto-resolution condition
    if confidence >= 0.75 and context_valid and context_score >= 0.6:
        logging.info("[DECISION] → resolve")
        return {"decision": "resolve"}

    # fallback
    logging.info("[DECISION] → escalate (low confidence/context)")
    return {"decision": "escalate"}