import os
import sys
import time
import hashlib
from datetime import datetime

# ==========================================
# SANVIDHAN-UPDATE: SUPREME MANDATE 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;220m', '\033[38;5;231m', '\033[38;5;33m', '\033[38;5;93m', '\033[38;5;244m'
C6, C7, C8, C9, C10  = '\033[38;5;180m', '\033[38;5;160m', '\033[38;5;252m', '\033[38;5;34m', '\033[38;5;232m'
C11, C12, C13, C14, C15 = '\033[38;5;121m', '\033[38;5;158m', '\033[38;5;18m', '\033[38;5;202m', '\033[38;5;242m'
C16, C17, C18, C19, C20 = '\033[38;5;234m', '\033[38;5;124m', '\033[38;5;28m', '\033[38;5;214m', '\033[38;5;233m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE SUPREME SCRIPT (SANVIDHAN)
# ==========================================
def sanvidhan_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C1}             __________
    {C1}            | {C2}संविधान{C1} |
    {C3}          __|__________|__      {C1}S A N V I D H A N
    {C3}         |  {C10}[{C1}UPDATE{C10}]{C3}  |     {C2}U P D A T E
    {C13}         |___________|     {C15}v8.8 [ATOMIC_SYNC]
    """
    print(logo)
    print(f"{C1}{BLD}   SANVIDHAN-UPDATE: SECURE POLICY PROPAGATION BUS{RST}\n")
    
    # Synchronization animation
    nodes = ["Gateway_Alpha", "Vault_Node_01", "Audit_Relay", "BCA_Inventory_Server"]
    for node in nodes:
        sys.stdout.write(f"\r{C15}[{C3}SYNC{C15}] {C1}Propagating Mandate to: {C12}{node:<20}{RST}")
        sys.stdout.flush()
        time.sleep(0.3)
    print(f"\n{C11}[+] Broadcast complete. All nodes acknowledging new policy baseline.{RST}\n")

# ==========================================
# ARCHITECTURE: POLICY DISTRIBUTION BUS
# ==========================================
class SanvidhanUpdateBus:
    """Simulates a secure bus for distributing signed policy updates."""
    def __init__(self):
        self.current_version = 1.0
        self.master_policy = {"MIN_PASS_LEN": 12, "MFA_ENABLED": "YES"}
        self.signing_secret = "VBSPU_POLICY_SECRET_2026"

    def create_update(self, new_rules):
        """Creates a signed update package."""
        self.current_version += 0.1
        self.master_policy.update(new_rules)
        
        # Create Update Fingerprint (Hash)
        package = f"v{self.current_version}|{self.master_policy}"
        signature = hashlib.sha256(f"{package}{self.signing_secret}".encode()).hexdigest()[:16]
        
        ts = datetime.now().strftime("%H:%M:%S")
        print(f"{C15}[{ts}] {C4}NEW_MANDATE: {C1}v{self.current_version:.1f}{RST} | {C9}Signing update...{RST}")
        return {"version": self.current_version, "data": self.master_policy, "sig": signature}

    def node_receive(self, node_name, update_pkg):
        """Simulates a remote node receiving and verifying the update."""
        time.sleep(0.5)
        print(f"{C13}[*] NODE {node_name}: {C2}Verifying incoming Sanvidhan-Update...{RST}")
        
        # Integrity Check
        package = f"v{update_pkg['version']}|{update_pkg['data']}"
        expected_sig = hashlib.sha256(f"{package}{self.signing_secret}".encode()).hexdigest()[:16]
        
        if update_pkg['sig'] == expected_sig:
            print(f"    {C11}[✔] Signature Valid. Applying Version {update_pkg['version']:.1f} to local core.{RST}")
            return True
        else:
            print(f"    {C7}[!] SIGNATURE MISMATCH! Possible Tampering. Rejecting update.{RST}")
            return False

# ==========================================
# SIMULATION: GLOBAL POLICY ROLLOUT
# ==========================================
if __name__ == "__main__":
    try:
        sanvidhan_banner_anim()
        bus = SanvidhanUpdateBus()
        
        # Step 1: Admin defines a new policy update
        new_mandate = {"MIN_PASS_LEN": 16, "IDLE_TIMEOUT": "300s"}
        pkg = bus.create_update(new_mandate)
        print("")

        # Step 2: Propagate to nodes
        bus.node_receive("GATEWAY_01", pkg)
        bus.node_receive("VAULT_SERVER", pkg)
        
        # Step 3: Simulation of a Tampered Update (Cyber Attack)
        time.sleep(1)
        print(f"\n{C7}[!] ALERT: Man-in-the-Middle attempting to inject malicious policy...{RST}")
        fake_pkg = pkg.copy()
        fake_pkg['data'] = {"MFA_ENABLED": "NO"} # Attacker tries to disable MFA
        bus.node_receive("REMOTE_NODE_X", fake_pkg)

    except KeyboardInterrupt:
        print(f"\n{C7}[!] Synchronization Interrupted.{RST}")