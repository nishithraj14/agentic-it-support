from datetime import datetime

def restart_email_service(user: str) -> dict:
    return {
        "status": "success",
        "tool": "email_service",
        "action": "restart_service",
        "input": {"user": user},
        "output": {"message": "Email service restarted"},
        "confidence": 0.88,
        "timestamp": datetime.utcnow().isoformat()
    }


def clear_mailbox(user: str) -> dict:
    return {
        "status": "success",
        "tool": "email_service",
        "action": "clear_mailbox",
        "input": {"user": user},
        "output": {"message": f"Mailbox cleared for {user}"},
        "confidence": 0.85,
        "timestamp": datetime.utcnow().isoformat()
    }