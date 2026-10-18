import os
import sys
import time
from datetime import datetime, timedelta

# ==========================================
# KALA-RETENTION: TEMPORAL CYCLE 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;232m', '\033[38;5;250m', '\033[38;5;93m', '\033[38;5;244m', '\033[38;5;231m'
C6, C7, C8, C9, C10  = '\033[38;5;214m', '\033[38;5;51m', '\033[38;5;94m', '\033[38;5;160m', '\033[38;5;33m'
C11, C12, C13, C14, C15 = '\033[38;5;118m', '\033[38;5;158m', '\033[38;5;235m', '\033[38;5;202m', '\033[38;5;242m'
C16, C17, C18, C19, C20 = '\033[38;5;233m', '\033[38;5;124m', '\033[38;5;28m', '\033[38;5;214m', '\033[38;5;234m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE HOURGLASS OF VOID (KALA)
# ==========================================
def kala_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C1}             ._____.
    {C2}            \\  {C6}:  {C2}/         {C1}K A L A
    {C1}             \\ {C3}v {C1}/          {C4}R E T E N T I O N
    {C2}             / {C1}. {C2}\\          {C15}v8.5 [SECURE_PURGE]
    {C1}            '-----'
    {C13}          [{C9}TIME_EXPIRED{C13}]
    """
    print(logo)
    print(f"{C1}{BLD}   KALA-RETENTION: AUTOMATED DATA LIFE-CYCLE & DISPOSAL{RST}\n")
    
    # Chrono-scan animation
    tasks = ["Scanning_Metadata", "Calculating_TTL", "Legal_Hold_Check", "Secure_Shredding"]
    for t in tasks:
        sys.stdout.write(f"\r{C15}[{C3}CHRONO{C15}] {C1}Processing Temporal Drift: {C7}{t:<20}{RST}")
        sys.stdout.flush()
        time.sleep(0.3)
    print(f"\n{C11}[+] Retention policies active. Monitoring data age across CUI nodes.{RST}\n")

# ==========================================
# ARCHITECTURE: DATA RETENTION ENGINE
# ==========================================
class KalaRetentionEngine:
    """Manages the life-cycle of CUI data from creation to secure deletion."""
    def __init__(self):
        # Retention Policy (in days)
        self.policies = {
            "FINANCIAL_CUI": 365,
            "STUDENT_RECORD": 730,
            "TEMP_AUDIT_LOG": 0.0001 # Seconds for demo
        }
        self.inventory = [
            {"id": "F_001", "type": "FINANCIAL_CUI", "created": datetime.now() - timedelta(days=400)},
            {"id": "S_992", "type": "STUDENT_RECORD", "created": datetime.now() - timedelta(days=100)},
            {"id": "T_555", "type": "TEMP_AUDIT_LOG", "created": datetime.now() - timedelta(minutes=5)}
        ]

    def enforce_retention(self):
        ts = datetime.now().strftime("%H:%M:%S")
        print(f"{C13}[{ts}] {C4}INITIATING AUTOMATED PURGE CYCLE...{RST}\n")
        time.sleep(1)
        
        print(f"{C4}{'ITEM_ID':<10} | {'TYPE':<16} | {'AGE (Days)':<10} | {'STATUS'}{RST}")
        print(f"{C4}{'-'*60}{RST}")

        for item in self.inventory:
            time.sleep(0.6)
            age = (datetime.now() - item["created"]).days
            limit = self.policies[item["type"]]
            
            if age >= limit:
                status = f"{C9}{BLD}PURGING (EXPIRED){RST}"
                action = f"{C8}SHREDDING_BLOCKS... OK{RST}"
            else:
                status = f"{C11}RETAINED (ACTIVE){RST}"
                action = f"{C10}NEXT_SCAN_IN {int(limit-age)} DAYS{RST}"
                
            print(f"{C6}{item['id']:<10}{RST} | {C2}{item['type']:<16}{RST} | {C3}{age:<10.1f}{RST} | {status}")
            if "PURGING" in status:
                print(f"    {C13}>> {action}")

        self._render_void_summary()

    def _render_void_summary(self):
        print(f"\n{C16}┌─────────────────────────────────────────────────────┐")
        print(f"{C16}│ {C6}KALA TEMPORAL RECLAMATION SUMMARY{' '*18} {C16}│")
        print(f"{C16}├─────────────────────────────────────────────────────┤")
        print(f"{C16}│ {C5}Total CUI Artifacts Tracked  : 3{' '*23} {C16}│")
        print(f"{C16}│ {C9}Artifacts Securely Erased    : 2{' '*23} {C16}│")
        print(f"{C16}│ {C11}Attack Surface Reduction     : 66.7%{' '*18} {C16}│")
        print(f"{C16}└─────────────────────────────────────────────────────┘{RST}\n")

# ==========================================
# SIMULATION: THE PURGE
# ==========================================
if __name__ == "__main__":
    try:
        kala_banner_anim()
        reaper = KalaRetentionEngine()
        reaper.enforce_retention()
        print(f"{C11}[✔] Cycle complete. Expired CUI data has been dissolved into the void.{RST}")
    except KeyboardInterrupt:
        print(f"\n{C9}[!] Reaper halted. Stale data remains on disk.{RST}")
        