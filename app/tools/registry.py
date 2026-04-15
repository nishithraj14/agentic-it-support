# app/tools/registry.py

from .password import reset_password, unlock_account
from .vpn import vpn_restart, vpn_reconfigure
from .access import grant_access, revoke_access
from .email import restart_email_service, clear_mailbox
from .device import run_diagnostics, reboot_device
from .network import restart_router, check_bandwidth

TOOL_REGISTRY = {
    "password_reset": reset_password,
    "account_unlock": unlock_account,
    "vpn_issue": vpn_restart,
    "vpn_config": vpn_reconfigure,
    "access_request": grant_access,
    "access_revoke": revoke_access,
    "email_issue": restart_email_service,
    "device_issue": run_diagnostics,
    "network_issue": restart_router,
}