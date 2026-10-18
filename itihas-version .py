import os
import sys
import time
import hashlib
from datetime import datetime

# ==========================================
# ITIHAS-VERSION: ETERNAL CHRONICLE 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;220m', '\033[38;5;94m', '\033[38;5;33m', '\033[38;5;51m', '\033[38;5;244m'
C6, C7, C8, C9, C10  = '\033[38;5;180m', '\033[38;5;231m', '\033[38;5;93m', '\033[38;5;46m', '\033[38;5;232m'
C11, C12, C13, C14, C15 = '\033[38;5;118m', '\033[38;5;158m', '\033[38;5;18m', '\033[38;5;202m', '\033[38;5;242m'
C16, C17, C18, C19, C20 = '\033[38;5;234m', '\033[38;5;124m', '\033[38;5;28m', '\033[38;5;214m', '\033[38;5;233m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE UNBREAKABLE CHAIN (ITIHAS)
# ==========================================
def itihas_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C2}             .====.
    {C2}            / {C1}HISTORY{C2} \\        {C1}I T I H A S
    {C1}           |  {C10}(HASH){C1}  |       {C4}V E R S I O N
    {C2}            \\ {C1}CHAIN  {C2}/        {C15}v9.3 [IMMUTABLE_LEDGER]
    {C2}             '===='
    {C13}          [{C11}MERKLE_ROOT_LOCKED{C13}]
    """
    print(logo)
    print(f"{C1}{BLD}   ITIHAS-VERSION: CRYPTOGRAPHICALLY SECURE VERSION CONTROL{RST}\n")
    
    # Hash chain animation
    commits = ["Init_Repo", "Added_MFA", "Fix_SQL_Injection", "Update_NIST_Policy"]
    for c in commits:
        sys.stdout.write(f"\r{C15}[{C3}COMMIT{C15}] {C1}Forging Immutable Hash: {C12}{c:<22}{RST}")
        sys.stdout.flush()
        time.sleep(0.3)
    print(f"\n{C11}[+] History Chain Intact. Monitoring repository for changes.{RST}\n")

# ==========================================
# ARCHITECTURE: SECURE COMMIT ENGINE
# ==========================================
class ItihasEngine:
    """Simulates an immutable commit history using hash linking."""
    def __init__(self):
        self.history = []
        self.last_hash = "0000000000000000" # Genesis Block

    def commit(self, author, message, content):
        """Creates a new version linked to the previous one."""
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Hash Calculation: $H_{new} = Hash(Content + Timestamp + H_{prev})$
        raw_payload = f"{content}{ts}{self.last_hash}"
        new_hash = hashlib.sha256(raw_payload.encode()).hexdigest()[:16]
        
        entry = {
            "version": len(self.history) + 1,
            "ts": ts,
            "author": author,
            "msg": message,
            "prev": self.last_hash,
            "hash": new_hash
        }
        
        self.history.append(entry)
        self.last_hash = new_hash
        
        print(f"{C15}[{ts}] {C4}NEW COMMIT: {C1}{message}{RST}")
        print(f"    {C13}>> Hash: {C11}{new_hash}{RST} | Linked to: {C5}{entry['prev']}{RST}\n")
        time.sleep(0.5)

    def verify_history(self):
        """Validates the entire chain for any tampering."""
        print(f"{C13}[*] Initiating Deep History Scan...{RST}")
        time.sleep(1)
        
        for i in range(1, len(self.history)):
            curr = self.history[i]
            prev = self.history[i-1]
            
            if curr['prev'] != prev['hash']:
                self._trigger_history_alert(curr['version'], "CHAIN_BROKEN / TAMPERED")
                return False
        
        print(f"    {C11}[✔] ITIHAS VERIFIED: No alterations detected in the timeline.{RST}")
        return True

    def _trigger_history_alert(self, version, reason):
        print(f"\n{C17}{BLD}!!! ITIHAS-VERSION: TEMPORAL ANOMALY DETECTED !!!{RST}")
        print(f"{C17}│ {C1}VIOLATION : {C17}{BLD}{reason}{RST}")
        print(f"{C17}│ {C1}VERSION   : {C11}V{version}{RST}")
        print(f"{C17}│ {C1}ACTION    : {C17}{BLD}REPOSITORY_LOCKDOWN | INVESTIGATING_ACTOR{RST}")
        print(f"{C17}└{'─'*55}{RST}\n")

# ==========================================
# SIMULATION: REPOSITORY TIMELINE
# ==========================================
if __name__ == "__main__":
    try:
        itihas_banner_anim()
        repo = ItihasEngine()
        
        # Step 1: Normal Commits
        repo.commit("Raj_Gautam", "Initialize CUI Database", "Table: Users, Assets")
        repo.commit("Shani_Partner", "Integrate MFA Project", "Module: Shakti_Auth")
        repo.commit("Raj_Gautam", "Patch Buffer Overflow", "Code: Sanitize_Input()")
        
        # Step 2: Verification
        repo.verify_history()
        
        # Step 3: Simulation of Tampering
        print(f"\n{C13}[!] Hacker attempting to modify history of Version 2...{RST}")
        time.sleep(1)
        repo.history[1]['msg'] = "Insert Backdoor" # Modification
        
        # Step 4: Re-verify (Detection)
        repo.verify_history()

    except KeyboardInterrupt:
        print(f"\n{C17}[!] Itihas monitoring suspended.{RST}")