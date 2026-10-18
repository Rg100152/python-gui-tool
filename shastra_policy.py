import os
import sys
import time
from datetime import datetime

# ==========================================
# SHASTRA-POLICY: DIVINE GOVERNANCE 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;220m', '\033[38;5;231m', '\033[38;5;33m', '\033[38;5;18m', '\033[38;5;93m'
C6, C7, C8, C9, C10  = '\033[38;5;232m', '\033[38;5;180m', '\033[38;5;160m', '\033[38;5;252m', '\033[38;5;34m'
C11, C12, C13, C14, C15 = '\033[38;5;254m', '\033[38;5;118m', '\033[38;5;136m', '\033[38;5;202m', '\033[38;5;244m'
C16, C17, C18, C19, C20 = '\033[38;5;233m', '\033[38;5;124m', '\033[38;5;28m', '\033[38;5;214m', '\033[38;5;234m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE SYMBOL OF AUTHORITY (SHASTRA)
# ==========================================
def shastra_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C1}             _________
    {C1}            / {C2}SHASTRA{C1} \\
    {C3}           |  {C10}/|||\\{C3}  |        {C1}S H A S T R A
    {C3}           |  {C10}\\|||/{C3}  |        {C5}P O L I C Y
    {C1}            \\_________/         {C15}v8.2 [ACTIVE_GOVERNANCE]
    {C13}          [{C11}ENFORCER_ACTIVE{C13}]
    """
    print(logo)
    print(f"{C1}{BLD}   SHASTRA-POLICY: ENTERPRISE-WIDE CUI HANDLING ENFORCEMENT{RST}\n")
    
    # Deployment cycle animation
    units = ["Identity_Governance", "Access_Orchestration", "Data_Protection", "Threat_Response"]
    for u in units:
        sys.stdout.write(f"\r{C15}[{C3}SHAS{C15}] {C1}Deploying Governance Unit: {C12}{u:<20}{RST}")
        sys.stdout.flush()
        time.sleep(0.3)
    print(f"\n{C10}[+] Governance baseline applied. Unauthorized actions will be intercepted.{RST}\n")

# ==========================================
# ARCHITECTURE: POLICY ENFORCEMENT ENGINE
# ==========================================
class ShastraEnforcer:
    """Intercepts and validates actions against organizational policies."""
    def __init__(self):
        # Master Policy Set (The 'Shastras')
        self.active_policies = {
            "DATA_EXFIL": {"action": "BLOCK", "scope": "EXT_NETWORK"},
            "USB_MOUNT": {"action": "BLOCK", "scope": "ANY_TERMINAL"},
            "CUI_ENCRYPT": {"action": "FORCE", "scope": "AT_REST"},
            "ADMIN_PRIV": {"action": "MFA_REQUIRED", "scope": "SUDO_CMD"}
        }

    def evaluate_action(self, user, requested_action, target):
        """Validates a user action against the active policy set."""
        ts = datetime.now().strftime("%H:%M:%S")
        print(f"{C15}[{ts}] {C4}EVALUATING: {C1}{user}{RST} -> {C11}{requested_action}{RST} on {C13}{target}{RST}")
        time.sleep(0.8)

        # Policy Mapping Logic
        for policy, rule in self.active_policies.items():
            if policy in requested_action or policy in target:
                if rule["action"] == "BLOCK":
                    self._trigger_policy_block(ts, user, requested_action, policy)
                    return False
                elif rule["action"] == "MFA_REQUIRED":
                    print(f"    {C12}[!] Policy Alert: Step-up authentication required for {policy}.{RST}")
                    return "MFA_PENDING"
        
        print(f"    {C10}[✔] Action Compliant with Shastra Baseline.{RST}\n")
        return True

    def _trigger_policy_block(self, ts, user, action, p_code):
        print(f"\n{C8}{BLD}!!! SHASTRA-POLICY: ACCESS DENIED BY GOVERNANCE ENGINE !!!{RST}")
        print(f"{C8}│ {C1}TIMESTAMP : {C10}{ts}{RST}")
        print(f"{C8}│ {C1}ACTOR     : {C15}{user}{RST}")
        print(f"{C8}│ {C1}VIOLATION : {C8}{BLD}{p_code}{RST}")
        print(f"{C8}│ {C1}REASON    : {C11}Organization-wide ban on {action}{RST}")
        print(f"{C8}│ {C1}ACTION    : {C8}{BLD}INTERCEPTED | EVENT_LOGGED | MANAGER_NOTIFIED{RST}")
        print(f"{C8}└{'─'*55}{RST}\n")
        time.sleep(0.5)

# ==========================================
# SIMULATION: GOVERNANCE IN ACTION
# ==========================================
if __name__ == "__main__":
    try:
        shastra_banner_anim()
        guard = ShastraEnforcer()
        
        # Scenario 1: Legitimate Compliant Action
        guard.evaluate_action("Raj_Gautam", "READ_FILE", "CUI_DOC_01.pdf")
        
        # Scenario 2: Policy Block (USB Mounting attempt)
        time.sleep(1)
        guard.evaluate_action("Intern_User", "MOUNT_DRIVE", "USB_PORT_02")
        
        # Scenario 3: Step-up Authentication (Sudo access)
        time.sleep(1)
        guard.evaluate_action("Admin_Raj", "SUDO_CMD", "NETWORK_CONFIG")

    except KeyboardInterrupt:
        print(f"\n{C8}[!] Governance Engine Shutdown. Security baseline compromised.{RST}")
        