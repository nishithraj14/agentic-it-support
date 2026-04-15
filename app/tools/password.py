# app/tools/password.py

from datetime import datetime

def reset_password(user: str) -> dict:
    return {
        "status": "success",
        "tool": "password_service",
        "action": "reset_password",
        "input": {"user": user},
        "output": {"message": f"Reset link sent to {user}"},
        "confidence": 0.95,
        "timestamp": datetime.utcnow().isoformat()
    }


def unlock_account(user: str) -> dict:
    return {
        "status": "success",
        "tool": "password_service",
        "action": "unlock_account",
        "input": {"user": user},
        "output": {"message": f"Account unlocked for {user}"},
        "confidence": 0.92,
        "timestamp": datetime.utcnow().isoformat()
    }