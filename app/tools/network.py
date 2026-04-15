from datetime import datetime

def restart_router(user: str) -> dict:
    return {
        "status": "success",
        "tool": "network_service",
        "action": "restart_router",
        "input": {"user": user},
        "output": {"message": "Router restarted"},
        "confidence": 0.86,
        "timestamp": datetime.utcnow().isoformat()
    }


def check_bandwidth(user: str) -> dict:
    return {
        "status": "success",
        "tool": "network_service",
        "action": "check_bandwidth",
        "input": {"user": user},
        "output": {"message": "Bandwidth within normal range"},
        "confidence": 0.84,
        "timestamp": datetime.utcnow().isoformat()
    }