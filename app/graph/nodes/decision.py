import logging

logging.basicConfig(level=logging.INFO)

LOW_RISK = [
    "password_reset",
    "vpn_issue",
    "email_issue",
    "device_issue",
    "network_issue"
]

HIGH_RISK = [
    "access_request",
    "account_unlock"
]


def decide(state):
    category = state.get("category")
    confidence = state.get("confidence", 0)
    context_score = state.get("context_score", 0)

    logging.info(
        f"[DECISION] category={category}, confidence={confidence:.2f}, context_score={context_score:.2f}"
    )

    # 🔴 Unknown
    if category == "unknown":
        state["decision"] = "escalate"
        return state

    # 🔴 High-risk
    if category in HIGH_RISK:
        state["decision"] = "escalate"
        return state

    # 🔴 Weak signals
    if confidence < 0.6 or context_score < 0.3:
        state["decision"] = "escalate"
        return state

    # ✅ Resolve
    if category in LOW_RISK:
        state["decision"] = "resolve"
        logging.info("[DECISION] → resolve")
        return state

    # fallback
    state["decision"] = "escalate"
    return state