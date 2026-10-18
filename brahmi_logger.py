import os
import sys
import time
import logging
import json
import secrets
from logging.handlers import RotatingFileHandler
from datetime import datetime

# ==========================================
# BRAHMI-LOGGER: THE ETERNAL SCRIBE THEME
# (Exactly 10 Unique ANSI 256 Colors)
# ==========================================
SCRIBE_GLD  = '\033[38;5;214m' 
INK_BLU     = '\033[38;5;26m'   
PARCH_WHT   = '\033[38;5;255m'  
STAMP_RED   = '\033[38;5;160m'  
VINTAGE_GRN = '\033[38;5;34m'   
MIDNIGHT_PRP= '\033[38;5;55m'   
QUARTZ_GRY  = '\033[38;5;244m'  
SKY_AZURE   = '\033[38;5;45m'   
SUNSET_ORG  = '\033[38;5;208m'  
NEON_LIME   = '\033[38;5;118m'  
RST         = '\033[0m'
BLD         = '\033[1m'

# ==========================================
# ANIMATION: INKING THE SCROLL
# ==========================================
def brahmi_boot_animation():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{SCRIBE_GLD}{BLD}>> BRAHMI-LOGGER: THE ETERNAL SCRIBE v3.2 <<{RST}\n")
    
    scribe_chars = ["|", "/", "-", "\\", "✒", "✍"]
    sys.stdout.write(f"{SKY_AZURE}[*] Dipping pen in digital ink... {RST}")
    for i in range(12):
        char = scribe_chars[i % len(scribe_chars)]
        sys.stdout.write(f"\b{SCRIBE_GLD}{char}{RST}")
        sys.stdout.flush()
        time.sleep(0.1)
    print(f"\n{NEON_LIME}[+] Structured Logging Subsystem Deployed.{RST}\n")

# ==========================================
# ARCHITECTURE: STRUCTURED ROTARY LOGGING
# ==========================================

class BrahmiLogger:
    """Enterprise-grade logging engine with Rotating File I/O."""
    
    def __init__(self, log_name="access_audit.log"):
        self.log_file = log_name
        self.logger = logging.getLogger("BrahmiEngine")
        self.logger.setLevel(logging.INFO)
        
        # 1. ARCHITECTURE: Rotating File Handler
        # Max size 2048 bytes (2KB) for demo rotation, keeping up to 3 backup files
        handler = RotatingFileHandler(self.log_file, maxBytes=2048, backupCount=3)
        
        # 2. FORMATTING: JSON-like Structured Output
        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def record_access(self, user, action, status, resource):
        """Records an access event with cryptographic session IDs."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        session_id = secrets.token_hex(4).upper()
        
        # Structured Data Packet
        log_entry = {
            "timestamp": timestamp,
            "session": session_id,
            "user": user,
            "action": action,
            "resource": resource,
            "status": status
        }
        
        # Write to Physical File
        self.logger.info(json.dumps(log_entry))
        
        # Display on Terminal with "The Scribe" Theme
        self._terminal_print(log_entry)

    def _terminal_print(self, entry):
        """Visual terminal output for real-time monitoring."""
        status_color = VINTAGE_GRN if entry["status"] == "SUCCESS" else STAMP_RED
        
        print(f"{MIDNIGHT_PRP}┌──[{QUARTZ_GRY}{entry['timestamp']}{MIDNIGHT_PRP}]─[{SKY_AZURE}ID:{entry['session']}{MIDNIGHT_PRP}]{RST}")
        print(f"{MIDNIGHT_PRP}│ {PARCH_WHT}SUBJECT : {SCRIBE_GLD}{entry['user']:<12}{RST} {MIDNIGHT_PRP}ACTION: {INK_BLU}{entry['action']}{RST}")
        print(f"{MIDNIGHT_PRP}│ {PARCH_WHT}TARGET  : {SKY_AZURE}{entry['resource']:<12}{RST} {MIDNIGHT_PRP}STATE:  {status_color}{entry['status']}{RST}")
        print(f"{MIDNIGHT_PRP}└{'─'*45}{RST}")

# ==========================================
# SIMULATION ENGINE
# ==========================================

def run_simulation():
    brahmi_boot_animation()
    scribe = BrahmiLogger()
    
    users = ["Admin_Raj", "User_Shani", "Analyst_Rishab", "Guest_Void"]
    actions = ["READ", "WRITE", "DELETE", "ENCRYPT", "ACCESS"]
    resources = ["CUI_DOC_01", "VAULT_S02", "CORE_KERNEL", "ROOT_SHELL"]
    
    print(f"{SUNSET_ORG}[!] Monitoring Live CUI Access Stream...{RST}\n")
    
    try:
        # Simulate 10 rapid events to trigger Log Rotation
        for i in range(10):
            user = random_choice(users)
            action = random_choice(actions)
            res = random_choice(resources)
            status = "SUCCESS" if random_choice([True, True, False]) else "FAILURE"
            
            scribe.record_access(user, action, status, res)
            time.sleep(0.8) # Real-time delay
            
        print(f"\n{NEON_LIME}[*] Check directory for: {scribe.log_file} and backup rotations.{RST}")
        
    except KeyboardInterrupt:
        print(f"\n{STAMP_RED}[!] Scribe logging halted.{RST}")

def random_choice(lst):
    """Secure random selection."""
    return lst[secrets.randbelow(len(lst))]

if __name__ == "__main__":
    run_simulation()