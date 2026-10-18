import os
import sys
import time
import hashlib
from datetime import datetime

# ==========================================
# PRAVAH-SYNC: DYNAMIC FLOW 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;33m', '\033[38;5;231m', '\033[38;5;51m', '\033[38;5;220m', '\033[38;5;121m'
C6, C7, C8, C9, C10  = '\033[38;5;18m', '\033[38;5;93m', '\033[38;5;244m', '\033[38;5;39m', '\033[38;5;232m'
C11, C12, C13, C14, C15 = '\033[38;5;118m', '\033[38;5;158m', '\033[38;5;18m', '\033[38;5;202m', '\033[38;5;242m'
C16, C17, C18, C19, C20 = '\033[38;5;233m', '\033[38;5;124m', '\033[38;5;28m', '\033[38;5;214m', '\033[38;5;234m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE DATA STREAM (PRAVAH)
# ==========================================
def pravah_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C1}           ~~~~~ {C3}>>{C1} ~~~~~
    {C3}          (  {C2}PRAVAH{C3}  )        {C1}P R A V A H
    {C1}           ~~~~~ {C3}>>{C1} ~~~~~        {C4}S Y N C
    {C13}          [{C3}OFFSITE_ACTIVE{C13}]       {C15}v9.7 [DELTA_REPLICATION]
    """
    print(logo)
    print(f"{C1}{BLD}   PRAVAH-SYNC: GEOGRAPHICALLY DISPERSED DATA SYNCHRONIZATION{RST}\n")
    
    # Replication sequence animation
    steps = ["Scanning_Local_Delta", "Compressing_Stream", "Encrypted_Tunneling", "Remote_Handshake"]
    for s in steps:
        sys.stdout.write(f"\r{C15}[{C1}FLOW{C15}] {C3}Streaming to Remote Site: {C5}{s:<20}{RST}")
        sys.stdout.flush()
        time.sleep(0.3)
    print(f"\n{C11}[+] Synchronization link established. Local and Offsite sites are in parity.{RST}\n")

# ==========================================
# ARCHITECTURE: DELTA SYNC ENGINE
# ==========================================
class PravahSyncEngine:
    """Simulates asynchronous data replication to a remote location."""
    def __init__(self):
        self.local_state = {"inventory": "v1.2", "policy": "v8.8"}
        self.remote_state = {"inventory": "v1.1", "policy": "v8.8"}

    def check_parity(self):
        """Identifies differences between local and remote sites."""
        ts = datetime.now().strftime("%H:%M:%S")
        print(f"{C15}[{ts}] {C4}SCANNING FOR DELTA CHANGES...{RST}")
        time.sleep(1)
        
        diff = []
        for key in self.local_state:
            if self.local_state[key] != self.remote_state.get(key):
                diff.append(key)
        
        if not diff:
            print(f"    {C11}[✔] SYSTEM IN PARITY. No synchronization needed.{RST}\n")
            return None
        
        print(f"    {C13}[!] DELTA DETECTED: {C5}{len(diff)} module(s) out of sync.{RST}")
        return diff

    def synchronize(self, modules):
        """Streams only the changed parts to the remote site."""
        if not modules: return
        
        ts = datetime.now().strftime("%H:%M:%S")
        print(f"{C13}[*] INITIATING PRAVAH STREAM...{RST}")
        
        for mod in modules:
            time.sleep(0.8)
            # Simulate streaming
            self.remote_state[mod] = self.local_state[mod]
            print(f"    {C11}>> SYNCED: {C3}{mod:<15}{RST} | New Version: {C1}{self.local_state[mod]}{RST}")
            
        self._render_sync_report(ts, len(modules))

    def _render_sync_report(self, ts, count):
        print(f"\n{C16}┌─────────────────────────────────────────────────────┐")
        print(f"{C16}│ {C1}OFFSITE SYNCHRONIZATION REPORT (PRAVAH){' '*11} {C16}│")
        print(f"{C16}├─────────────────────────────────────────────────────┤")
        print(f"{C16}│ {C3}REMOTE SITE      : {C4}Lucknow_DR_Center{' '*18} {C16}│")
        print(f"{C16}│ {C3}MODULES UPDATED  : {count:<33} {C16}│")
        print(f"{C16}│ {C11}STATUS           : SYNCHRONIZED (PARITY){' '*14} {C16}│")
        print(f"{C16}└─────────────────────────────────────────────────────┘{RST}\n")

# ==========================================
# SIMULATION: OFFSITE REPLICATION
# ==========================================
if __name__ == "__main__":
    try:
        pravah_banner_anim()
        sync_tool = PravahSyncEngine()
        
        # Step 1: Initial check
        delta = sync_tool.check_parity()
        
        # Step 2: Perform Sync
        sync_tool.synchronize(delta)
        
        # Step 3: Verify again
        sync_tool.check_parity()

    except KeyboardInterrupt:
        print(f"\n{C17}[!] Pravah link broken.{RST}")