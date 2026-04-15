import json
from openai import OpenAI

client = OpenAI()

CATEGORIES = [
    "password_reset",
    "account_unlock",
    "vpn_issue",
    "access_request",
    "email_issue",
    "device_issue",
    "network_issue",
    "unknown"
]

def classify(state):
    ticket = state["ticket"]

    prompt = f"""
Classify IT support ticket into ONE category:
{CATEGORIES}

Return JSON:
{{"category": "...", "confidence": 0-1}}

Ticket: {ticket}
"""

    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        response_format={"type": "json_object"}
    )

    result = json.loads(res.choices[0].message.content)

    if result["confidence"] < 0.6:
        result["category"] = "unknown"

    return result