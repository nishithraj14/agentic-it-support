from datetime import datetime

def grant_access(user: str, system: str) -> dict:
    return {
        "status": "success",
        "tool": "access_service",
        "action": "grant_access",
        "input": {"user": user, "system": system},
        "output": {"message": f"{user} granted access to {system}"},
        "confidence": 0.93,
        "timestamp": datetime.utcnow().isoformat()
    }


def revoke_access(user: str, system: str) -> dict:
    return {
        "status": "success",
        "tool": "access_service",
        "action": "revoke_access",
        "input": {"user": user, "system": system},
        "output": {"message": f"{user} access revoked from {system}"},
        "confidence": 0.90,
        "timestamp": datetime.utcnow().isoformat()
    }