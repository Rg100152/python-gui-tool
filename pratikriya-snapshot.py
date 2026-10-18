import os
import sys
import time
import hashlib
from datetime import datetime

# ==========================================
# PRATIKRIYA-SNAPSHOT: INSTANT REFLECTION 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;231m', '\033[38;5;33m', '\033[38;5;51m', '\033[38;5;244m', '\033[38;5;220m'
C6, C7, C8, C9, C10  = '\033[38;5;121m', '\033[38;5;93m', '\033[38;5;250m', '\033[38;5;18m', '\033[38;5;232m'
C11, C12, C13, C14, C15 = '\033[38;5;118m', '\033[38;5;158m', '\033[38;5;18m', '\033[38;5;202m', '\033[38;5;242m'
C16, C17, C18, C19, C20 = '\033[38;5;233m', '\033[38;5;124m', '\033[38;5;28m', '\033[38;5;214m', '\033[38;5;234m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE CAMERA LENS (PRATIKRIYA)
# ==========================================
def pratikriya_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C1}             .---.
    {C1}            /  {C2}O{C1}  \\          {C1}P R A T I K R I Y A
    {C1}           |  {C3}[S]{C1}  |         {C2}S N A P S H O T
    {C1}            \\  {C2}-{C1}  /          {C15}v9.6 [IMMUTABLE_IMAGE]
    {C1}             '---'
    {C13}          [{C11}STATE_FROZEN{C13}]
    """
    print(logo)
    print(f"{C1}{BLD}   PRATIKRIYA-SNAPSHOT: INSTANT POINT-IN-TIME DATA CAPTURE{RST}\n")
    
    # Snapshot freezing animation
    steps = ["Indexing_Blocks", "Freezing_IO", "Capturing_Metadata", "Sealing_Snapshot"]
    for s in steps:
        sys.stdout.write(f"\r{C15}[{C2}SNAP{C15}] {C1}Freezing System State: {C3}{s:<20}{RST}")
        sys.stdout.flush()
        time.sleep(0.3)
    print(f"\n{C11}[+] Snapshot created. Current state is now read-only in the snapshot repository.{RST}\n")

# ==========================================
# ARCHITECTURE: SNAPSHOT ENGINE
# ==========================================
class PratikriyaEngine:
    """Manages immutable snapshots of system data."""
    def __init__(self):
        self.snapshots = {}
        self.live_data = {"CUI_ID_101": "VBSPU_DEPT_A", "STATUS": "SECURE"}

    def take_snapshot(self, label):
        """Creates an immutable copy of current live data."""
        ts = datetime.now().strftime("%H:%M:%S")
        snap_id = hashlib.md5(f"{label}{ts}".encode()).hexdigest()[:8]
        
        # In reality, this uses Copy-on-Write pointers
        self.snapshots[snap_id] = {
            "label": label,
            "ts": ts,
            "data": self.live_data.copy(),
            "hash": hashlib.sha256(str(self.live_data).encode()).hexdigest()[:16]
        }
        
        print(f"{C15}[{ts}] {C4}SNAP_GEN: {C1}{label}{RST} | ID: {C5}{snap_id}{RST}")
        print(f"    {C13}>> State Sealed. Integrity Hash: {C11}{self.snapshots[snap_id]['hash']}{RST}\n")
        return snap_id

    def modify_live_data(self, key, value):
        """Changes the live data (while snapshot remains frozen)."""
        print(f"{C13}[*] Modifying Live Data: {C9}{key} -> {value}{RST}")
        self.live_data[key] = value

    def compare_to_snapshot(self, snap_id):
        """Compares current live data with a previous snapshot."""
        snap = self.snapshots.get(snap_id)
        print(f"\n{C16}┌─────────────────────────────────────────────────────┐")
        print(f"{C16}│ {C5}PRATIKRIYA DIFFERENTIAL ANALYSIS (Live vs Snap){' '*6} {C16}│")
        print(f"{C16}├─────────────────────────────────────────────────────┤")
        print(f"{C16}│ {C1}SNAPSHOT ID : {snap_id:<38} {C16}│")
        print(f"{C16}│ {C3}LIVE DATA   : {str(self.live_data):<38} {C16}│")
        print(f"{C16}│ {C3}SNAP DATA   : {str(snap['data']):<38} {C16}│")
        print(f"{C16}└─────────────────────────────────────────────────────┘{RST}\n")

# ==========================================
# SIMULATION: STATE CAPTURE
# ==========================================
if __name__ == "__main__":
    try:
        pratikriya_banner_anim()
        engine = PratikriyaEngine()
        
        # Step 1: Take initial 'Safe' snapshot
        sid = engine.take_snapshot("BEFORE_UPDATE")
        time.sleep(1)

        # Step 2: Modify live data (Simulation of change or attack)
        engine.modify_live_data("STATUS", "COMPROMISED")
        
        # Step 3: Compare to see how easy it is to 'Rollback' or Audit
        engine.compare_to_snapshot(sid)
        
        print(f"{C11}[✔] Pratikriya successful. You can now rollback to '{sid}' instantly.{RST}")

    except KeyboardInterrupt:
        print(f"\n{C17}[!] Snapshot process halted.{RST}")