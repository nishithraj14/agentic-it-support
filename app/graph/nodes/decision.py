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
    context_valid = state.get("context_valid", False)
    context_score = state.get("context_score", 0)

    logging.info(
        f"[DECISION] category={category}, confidence={confidence}, context_score={context_score}"
    )

    # 🔴 Always escalate high-risk
    if category in HIGH_RISK:
        logging.info("[DECISION] → escalate (high-risk)")
        return {"decision": "escalate"}

    # 🔥 Strong auto-resolve rule
    if (
        category in AUTO_RESOLVE
        and confidence >= 0.7
        and context_valid
        and context_score >= 0.5
    ):
        logging.info("[DECISION] → resolve (auto-resolve category)")
        return {"decision": "resolve"}

    # fallback
    logging.info("[DECISION] → escalate (fallback)")
    return {"decision": "escalate"}