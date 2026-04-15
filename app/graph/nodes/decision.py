import logging

HIGH_RISK = ["access_request"]

AUTO_RESOLVE = [
    "vpn_issue",
    "email_issue",
    "password_reset",
    "account_unlock",
    "device_issue",
    "network_issue"
]

def decide(state):
    category = state.get("category")
    confidence = state.get("confidence", 0)
    context = state.get("context", "")

    logging.info(f"[DECISION] category={category}, confidence={confidence}")

    # 🔴 High-risk always escalate
    if category in HIGH_RISK:
        logging.info("[DECISION] → escalate (high-risk)")
        return {"decision": "escalate"}

    # 🔴 No context → escalate
    if not context or "No relevant policy" in context:
        logging.info("[DECISION] → escalate (no context)")
        return {"decision": "escalate"}

    # 🔥 Auto-resolve categories
    if category in AUTO_RESOLVE and confidence >= 0.7:
        logging.info("[DECISION] → resolve")
        return {"decision": "resolve"}

    # fallback
    logging.info("[DECISION] → escalate (fallback)")
    return {"decision": "escalate"}