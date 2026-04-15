from datetime import datetime

def run_diagnostics(user: str) -> dict:
    return {
        "status": "success",
        "tool": "device_service",
        "action": "run_diagnostics",
        "input": {"user": user},
        "output": {"message": "Diagnostics completed"},
        "confidence": 0.87,
        "timestamp": datetime.utcnow().isoformat()
    }


def reboot_device(user: str) -> dict:
    return {
        "status": "success",
        "tool": "device_service",
        "action": "reboot",
        "input": {"user": user},
        "output": {"message": "Device rebooted"},
        "confidence": 0.89,
        "timestamp": datetime.utcnow().isoformat()
    }