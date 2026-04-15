# app/tools/vpn.py

from datetime import datetime

def vpn_restart(user: str) -> dict:
    return {
        "status": "success",
        "tool": "vpn_service",
        "action": "restart",
        "input": {"user": user},
        "output": {"message": "VPN session restarted"},
        "confidence": 0.90,
        "timestamp": datetime.utcnow().isoformat()
    }


def vpn_reconfigure(user: str) -> dict:
    return {
        "status": "success",
        "tool": "vpn_service",
        "action": "reconfigure",
        "input": {"user": user},
        "output": {"message": "VPN reconfigured successfully"},
        "confidence": 0.88,
        "timestamp": datetime.utcnow().isoformat()
    }