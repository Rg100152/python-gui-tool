import os
import time
import sys
import threading
import hashlib
import random

# ==========================================
# RAJ-DRISHTI: THE ALL-SEEING EYE THEME
# (Exactly 10 Unique ANSI 256 Colors)
# ==========================================
EYE_ORG    = '\033[38;5;214m'  # Orange
IRIS_GLD   = '\033[38;5;220m'  # Gold
SCLERA_WHT = '\033[38;5;253m'  # White
WATCH_CYN  = '\033[38;5;51m'   # Cyan
MOD_PURP   = '\033[38;5;135m'  # Purple
DEL_RED    = '\033[38;5;196m'  # Red
NEW_GRN    = '\033[38;5जीत46m' # Green (Fixed code: \033[38;5;46m)
NEW_GRN    = '\033[38;5;46m'
TIME_BLU   = '\033[38;5;33m'   # Blue
SYS_GRY    = '\033[38;5;244m'  # Gray
PUPIL_BLK  = '\033[38;5;236m'  # Dark Gray
RST        = '\033[0m'
BLD        = '\033[1m'

# ==========================================
# ANIMATION: AWAKENING DRISHTI (THE EYE)
# ==========================================
def drishti_boot_animation():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{IRIS_GLD}{BLD}>> RAJ-DRISHTI: CONTINUOUS CUI SURVEILLANCE <<{RST}\n")
    
    # Eye opening animation frames
    frames = [
        [
            "       -------       ",
            "                     ",
            "       -------       "
        ],
        [
            "      .-------.      ",
            "     /         \\     ",
            "     '---------'     "
        ],
        [
            "     .---------.     ",
            f"    /   {IRIS_GLD}( {EYE_ORG}O{IRIS_GLD} ){SCLERA_WHT}   \\    ",
            "    '-----------'    "
        ]
    ]
    
    for frame in frames:
        sys.stdout.write("\033[F" * 3) if frames.index(frame) > 0 else None
        for line in frame:
            print(f"{SCLERA_WHT}{line}{RST}")
        time.sleep(0.5)
        
    print(f"\n{WATCH_CYN}[*] Calibrating Cryptographic Retinas...{RST}")
    for i in range(20):
        sys.stdout.write(f"\r{SYS_GRY}['{RST}{WATCH_CYN}{'/' * i}{SYS_GRY}{' ' * (20-i)}]{RST}")
        sys.stdout.flush()
        time.sleep(0.05)
    print(f"\n{NEW_GRN}[+] DRISHTI ONLINE. FIM DAEMON ACTIVE.{RST}\n")

# ==========================================
# ARCHITECTURE: REACTIVE FILE INTEGRITY MONITOR
# ==========================================
class DrishtiFIM:
    """File Integrity Monitor using State-Machine Polling & SHA-256."""
    
    def __init__(self, target_dir):
        self.target_dir = target_dir
        self.state = {}
        
        # Ensure target directory exists
        if not os.path.exists(self.target_dir):
            os.makedirs(self.target_dir)

    def _hash_file(self, filepath):
        """Calculates SHA-256 hash of a file."""
        hasher = hashlib.sha256()
        try:
            with open(filepath, 'rb') as f:
                buf = f.read(65536)
                while len(buf) > 0:
                    hasher.update(buf)
                    buf = f.read(65536)
            return hasher.hexdigest()
        except Exception:
            return None

    def establish_baseline(self):
        """Records the initial state of the directory."""
        print(f"{SYS_GRY}[*] Establishing Baseline for: {self.target_dir}{RST}")
        for filename in os.listdir(self.target_dir):
            filepath = os.path.join(self.target_dir, filename)
            if os.path.isfile(filepath):
                stat = os.stat(filepath)
                self.state[filepath] = {
                    "mtime": stat.st_mtime,
                    "size": stat.st_size,
                    "hash": self._hash_file(filepath)
                }
        print(f"{SYS_GRY}[*] Baseline secured. Monitoring started...{RST}\n")

    def monitor_cycle(self):
        """The Daemon worker that polls for state changes."""
        current_files = []
        
        # 1. Check for Creations and Modifications
        for filename in os.listdir(self.target_dir):
            filepath = os.path.join(self.target_dir, filename)
            if not os.path.isfile(filepath): continue
            
            current_files.append(filepath)
            stat = os.stat(filepath)
            
            # Scenario A: New File
            if filepath not in self.state:
                file_hash = self._hash_file(filepath)
                self.state[filepath] = {"mtime": stat.st_mtime, "size": stat.st_size, "hash": file_hash}
                self._log_event("CREATED", filename, NEW_GRN)
                
            # Scenario B: Modified File
            # Optimization: Only calculate heavy SHA-256 if mtime or size changed
            elif stat.st_mtime != self.state[filepath]["mtime"] or stat.st_size != self.state[filepath]["size"]:
                new_hash = self._hash_file(filepath)
                
                if new_hash != self.state[filepath]["hash"]:
                    self.state[filepath] = {"mtime": stat.st_mtime, "size": stat.st_size, "hash": new_hash}
                    self._log_event("TAMPERED/MODIFIED", filename, MOD_PURP, f"New Hash: {new_hash[:8]}...")

        # 2. Check for Deletions
        deleted_files = [f for f in self.state.keys() if f not in current_files]
        for filepath in deleted_files:
            filename = os.path.basename(filepath)
            self._log_event("DELETED", filename, DEL_RED)
            del self.state[filepath]

    def _log_event(self, action, filename, color, extra=""):
        timestamp = time.strftime("%H:%M:%S")
        print(f"{PUPIL_BLK}┌─[{TIME_BLU}{timestamp}{PUPIL_BLK}]{RST}")
        print(f"{PUPIL_BLK}│ {SCLERA_WHT}TARGET : {WATCH_CYN}{filename}{RST}")
        print(f"{PUPIL_BLK}│ {SCLERA_WHT}ACTION : {color}{BLD}{action}{RST} {SYS_GRY}{extra}{RST}")
        print(f"{PUPIL_BLK}└{'─'*40}{RST}")


# ==========================================
# SIMULATOR: THE INSIDER THREAT (Runs in background)
# ==========================================
def insider_threat_simulator(target_dir):
    """Simulates a hacker adding, altering, or deleting files."""
    time.sleep(2) # Wait for Drishti to establish baseline
    
    actions = [
        # Action 1: Create a rogue file
        lambda: open(os.path.join(target_dir, "rogue_malware.sh"), "w").write("echo 'Hacked'"),
        # Action 2: Modify an existing file
        lambda: open(os.path.join(target_dir, "cui_finances.csv"), "a").write("\nTransferred $1M to Swiss Acc"),
        # Action 3: Delete a file
        lambda: os.remove(os.path.join(target_dir, "rogue_malware.sh")) if os.path.exists(os.path.join(target_dir, "rogue_malware.sh")) else None,
        # Action 4: Create secret data
        lambda: open(os.path.join(target_dir, "vault_keys.txt"), "w").write("Admin: 12345")
    ]
    
    for _ in range(5):
        time.sleep(random.uniform(2.0, 4.0)) # Wait randomly
        action = random.choice(actions)
        try:
            action()
        except Exception:
            pass

# ==========================================
# MAIN EXECUTION
# ==========================================
def start_surveillance():
    drishti_boot_animation()
    
    # Setup Vault
    vault_dir = "./drishti_vault"
    if not os.path.exists(vault_dir): os.makedirs(vault_dir)
    
    # Put some initial files
    with open(os.path.join(vault_dir, "cui_finances.csv"), "w") as f:
        f.write("Q1 Revenue: $500K\n")
        
    drishti = DrishtiFIM(vault_dir)
    drishti.establish_baseline()
    
    # Start the "Hacker" simulator thread
    simulator = threading.Thread(target=insider_threat_simulator, args=(vault_dir,), daemon=True)
    simulator.start()
    
    print(f"{EYE_ORG}[!] DRISHTI IS WATCHING. PRESS CTRL+C TO TERMINATE.{RST}\n")
    
    try:
        while True:
            drishti.monitor_cycle()
            time.sleep(1) # Polling interval
    except KeyboardInterrupt:
        print(f"\n{DEL_RED}[!] Surveillance Terminated. Closing Drishti...{RST}")

if __name__ == "__main__":
    start_surveillance()