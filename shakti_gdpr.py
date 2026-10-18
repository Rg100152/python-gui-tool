import os
import sys
import time
from datetime import datetime

# ==========================================
# SHAKTI-GDPR: SOVEREIGN RIGHTS 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;220m', '\033[38;5;33m', '\033[38;5;231m', '\033[38;5;46m', '\033[38;5;160m'
C6, C7, C8, C9, C10  = '\033[38;5;93m', '\033[38;5;244m', '\033[38;5;51m', '\033[38;5;232m', '\033[38;5;252m'
C11, C12, C13, C14, C15 = '\033[38;5;121m', '\033[38;5;158m', '\033[38;5;18m', '\033[38;5;202m', '\033[38;5;242m'
C16, C17, C18, C19, C20 = '\033[38;5;234m', '\033[38;5;124m', '\033[38;5;28m', '\033[38;5;214m', '\033[38;5;233m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE SYMBOL OF EMPOWERMENT (SHAKTI)
# ==========================================
def shakti_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C1}             /\\
    {C1}            /  \\           {C1}S H A K T I
    {C2}           /____\\          {C4}G D P R
    {C1}          |  {C3}(P){C1}  |         {C15}v8.6 [PRIVACY_ENFORCER]
    {C2}          |______|
    {C13}         /________\\
    """
    print(logo)
    print(f"{C1}{BLD}   SHAKTI-GDPR: DISTRIBUTED DATA PRIVACY RIGHTS MANAGEMENT{RST}\n")
    
    # GDPR Compliance Scan animation
    rights = ["Data_Portability", "Consent_Logging", "Right_To_Erasure", "Purpose_Limitation"]
    for r in rights:
        sys.stdout.write(f"\r{C15}[{C2}LAW{C15}] {C3}Enforcing Sovereign Right: {C11}{r:<20}{RST}")
        sys.stdout.flush()
        time.sleep(0.3)
    print(f"\n{C4}[+] Privacy-Guard active. Personal data processing is now compliant.{RST}\n")

# ==========================================
# ARCHITECTURE: PRIVACY RIGHTS ENGINE
# ==========================================
class ShaktiGdprEngine:
    """Simulates GDPR core principles: Consent, Access, and Deletion."""
    def __init__(self):
        self.user_database = {
            "raj_gautam": {"consent": True, "data": "BCA_Academic_Records", "location": "IN_Server"},
            "johnson_sr": {"consent": False, "data": "Grading_History", "location": "EU_Server"}
        }

    def process_data(self, user):
        """Checks if consent exists before processing."""
        ts = datetime.now().strftime("%H:%M:%S")
        print(f"{C15}[{ts}] {C2}REQUEST: {C3}Processing data for {C1}{user}{RST}...")
        time.sleep(0.8)

        if user in self.user_database:
            if self.user_database[user]["consent"]:
                print(f"    {C4}[✔] CONSENT VERIFIED. Action: ALLOWED.{RST}")
                return True
            else:
                self._trigger_privacy_alert(ts, user, "NO_CONSENT_GIVEN")
                return False
        print(f"    {C5}[!] User not found in Registry.{RST}")
        return False

    def right_to_be_forgotten(self, user):
        """Implements the GDPR Right to Erasure."""
        print(f"\n{C7}[*] EXERCISING RIGHT TO ERASURE: {C1}{user}{RST}")
        time.sleep(1)
        if user in self.user_database:
            del self.user_database[user]
            print(f"    {C11}[✔] Data Shredded. Logs Purged. User '{user}' has been forgotten.{RST}\n")
        else:
            print(f"    {C5}[!] No records found to purge.{RST}\n")

    def _trigger_privacy_alert(self, ts, user, reason):
        print(f"\n{C5}{BLD}!!! SHAKTI-GDPR: PRIVACY VIOLATION INTERCEPTED !!!{RST}")
        print(f"{C5}│ {C3}TIMESTAMP : {C10}{ts}{RST}")
        print(f"{C5}│ {C3}USER      : {C15}{user}{RST}")
        print(f"{C5}│ {C3}REASON    : {C5}{BLD}{reason}{RST}")
        print(f"{C5}│ {C3}ACTION    : {C5}{BLD}PROCESSING_HALTED | LEGAL_LOG_GENERATED{RST}")
        print(f"{C5}└{'─'*55}{RST}\n")

# ==========================================
# SIMULATION: PRIVACY LIFECYCLE
# ==========================================
if __name__ == "__main__":
    try:
        shakti_banner_anim()
        engine = ShaktiGdprEngine()
        
        # 1. Processing with Consent
        engine.process_data("raj_gautam")
        
        # 2. Processing without Consent (Blocked)
        time.sleep(1)
        engine.process_data("johnson_sr")
        
        # 3. Exercising "Right to be Forgotten"
        time.sleep(1)
        engine.right_to_be_forgotten("raj_gautam")
        
        # 4. Attempting to process after deletion
        engine.process_data("raj_gautam")

    except KeyboardInterrupt:
        print(f"\n{C5}[!] Shakti Guard Deactivated.{RST}")