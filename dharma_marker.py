import os
import time
from datetime import datetime

# ==========================================
# DHARMA-MARKER: AUDIT COLOR PALETTE
# ==========================================
B = '\033[94m'  # Blue (System)
W = '\033[97m'  # White (Audit Log)
R = '\033[91m'  # Red (Enforcement/Violation)
Y = '\033[93m'  # Yellow (Warning)
E = '\033[0m'   # Reset
BOLD = '\033[1m'

# ==========================================
# THE EVENT BUS (PUB/SUB ARCHITECTURE)
# ==========================================
# This dictionary holds all registered events in the system.
_EVENT_REGISTRY = {}

def subscribe(event_name):
    """
    A professional Python Decorator. 
    It attaches functions to specific system events without calling them directly.
    """
    def decorator(func):
        if event_name not in _EVENT_REGISTRY:
            _EVENT_REGISTRY[event_name] = []
        _EVENT_REGISTRY[event_name].append(func)
        return func
    return decorator

def emit(event_name, payload=None):
    """Broadcasts an event to the system. All subscribed functions will trigger."""
    if event_name in _EVENT_REGISTRY:
        for handler in _EVENT_REGISTRY[event_name]:
            handler(payload)

# ==========================================
# SYSTEM UTILITIES & AESTHETICS
# ==========================================

def log_audit(action, status, details):
    """Generates an immutable-style forensic log entry."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    print(f"{W}[{timestamp}] {BOLD}{action:<15}{E} | {status:<10} | {details}")
    time.sleep(0.4) # Simulated delay for reading logs

def display_dharma_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = f"""{B}{BOLD}
       ____  __  _____    ____  __  ______ 
      / __ \/ / / /   |  / __ \/  |/  /   |
     / / / / /_/ / /| | / /_/ / /|_/ / /| |
    / /_/ / __  / ___ |/ _, _/ /  / / ___ |
   /_____/_/ /_/_/  |_/_/ |_/_/  /_/_/  |_|
   {W}M A R K E R   &   E N F O R C E M E N T{E}
    """
    print(banner)
    print(f"{B}>> ARCHITECTURE: EVENT-DRIVEN (PUB/SUB METAPROGRAMMING){E}")
    print(f"{R}>> DIRECTIVE: STRICT CUI COMPLIANCE ENFORCEMENT{E}\n")

# ==========================================
# EVENT HANDLERS (THE LOGIC)
# ==========================================

@subscribe("SYSTEM_BOOT")
def handle_boot(payload):
    """Triggers when the system starts."""
    display_dharma_banner()
    log_audit("SYS_BOOT", f"{B}OK{E}", "Dharma Event Bus initialized.")
    log_audit("SYS_BOOT", f"{B}OK{E}", "Awaiting TARGET_ACQUIRED event...")
    
    # Generate test environment
    test_file = "dharma_test_subject.txt"
    with open(test_file, "w") as f:
        f.write("CONFIDENTIAL: Q4 Financial Projections.\nDo not distribute outside the department.\n")
    
    # Chain reaction: Emit the next event
    emit("TARGET_ACQUIRED", test_file)

@subscribe("TARGET_ACQUIRED")
def handle_scan(filepath):
    """Triggers when a file is found. Scans for existing enforcement."""
    log_audit("SCAN_INIT", f"{Y}PENDING{E}", f"Analyzing {filepath} for Dharma markings.")
    
    try:
        with open(filepath, "r") as f:
            content = f.read()
            
        if "DHARMA ENFORCEMENT NOTICE" in content:
            log_audit("SCAN_RESULT", f"{B}PASS{E}", "Document is already compliant.")
            emit("SYSTEM_SHUTDOWN", "No enforcement necessary.")
        else:
            log_audit("SCAN_RESULT", f"{R}VIOLATION{E}", "CUI Markings missing! Triggering enforcement.")
            # Chain reaction: Trigger the enforcement protocol
            emit("ENFORCE_COMPLIANCE", filepath)
            
    except FileNotFoundError:
        log_audit("SCAN_ERROR", f"{R}FAIL{E}", f"Target {filepath} unreachable.")

@subscribe("ENFORCE_COMPLIANCE")
def handle_enforcement(filepath):
    """Triggers when a violation is found. Modifies the file to enforce compliance."""
    log_audit("ENFORCE_INIT", f"{Y}ACTIVE{E}", f"Injecting Dharma markings into {filepath}...")
    
    dharma_notice = f"""
{R}======================================================================
[!] DHARMA-MARKER ENFORCEMENT NOTICE
CLASSIFICATION: CUI // SP-SENSITIVE // MANDATORY PROTECTION
Under System Directive 4A, this document is strictly monitored.
Unauthorized modification or distribution is prohibited.
======================================================================{E}
"""
    try:
        with open(filepath, "r") as f:
            original_data = f.read()
            
        # Append the notice at the top of the file
        with open(filepath, "w") as f:
            f.write(dharma_notice + "\n" + original_data)
            
        log_audit("ENFORCE_DONE", f"{B}SUCCESS{E}", "Notice permanently injected into target.")
        emit("SYSTEM_SHUTDOWN", f"Enforcement successful on {filepath}.")
        
    except Exception as e:
        log_audit("ENFORCE_ERR", f"{R}FATAL{E}", str(e))

@subscribe("SYSTEM_SHUTDOWN")
def handle_shutdown(reason):
    """Triggers at the end of the sequence."""
    log_audit("SYS_HALT", f"{B}OK{E}", f"Reason: {reason}")
    print(f"\n{B}>> DHARMA-MARKER SECURELY DISCONNECTED <<{E}")

# ==========================================
# EXECUTION TRIGGER
# ==========================================
if __name__ == "__main__":
    # To start an Event-Driven program, we simply emit the very first event.
    # The rest happens automatically like a domino effect.
    try:
        emit("SYSTEM_BOOT")
        
        print(f"\n{Y}[*] Check 'dharma_test_subject.txt' in your Thonny directory to see the applied markings.{E}")
    except KeyboardInterrupt:
        print(f"\n{R}>> OPERATOR INTERRUPT DETECTED. HALTING DHARMA PROTOCOLS. <<{E}")