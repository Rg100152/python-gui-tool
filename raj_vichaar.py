import os
import time
import sys
import random

# ==========================================
# RAJ-VICHAAR: TERMINAL COLOR SCHEME
# ==========================================
G = '\033[92m'  # Success
Y = '\033[93m'  # Warning/Progress
R = '\033[91m'  # Critical/Alert
B = '\033[94m'  # Data
C = '\033[96m'  # Info
E = '\033[0m'   # Reset
BOLD = '\033[1m'

# ==========================================
# DATA-DRIVEN CLASSIFICATION ENGINE
# ==========================================
# This dictionary defines the "Vichaar" (Intelligence) of the tool.
VICHAAR_CONFIG = {
    "CUI_BASIC": {
        "keywords": ["internal", "draft", "project info", "meeting notes"],
        "level": 1,
        "color": B,
        "label": "CUI // BASIC"
    },
    "CUI_SENSITIVE": {
        "keywords": ["financial", "aadhar", "payroll", "tax record", "identity"],
        "level": 2,
        "color": Y,
        "label": "CUI // SP-SENSITIVE"
    },
    "CUI_RESTRICTED": {
        "keywords": ["zero-day", "exploit", "encryption key", "admin creds", "privilege"],
        "level": 3,
        "color": R,
        "label": "CUI // SP-RESTRICTED (HIGH-THREAT)"
    }
}

# ==========================================
# CORE LOGIC MODULES
# ==========================================

def display_header():
    """Renders the unique Raj-Vichaar aesthetic."""
    print(f"{C}{BOLD}" + "="*60)
    print("""
    ██████╗  █████╗      ██╗██╗   ██╗██╗ ██████╗██╗  ██╗ █████╗  █████╗ ██████╗ 
    ██╔══██╗██╔══██╗     ██║██║   ██║██║██╔════╝██║  ██║██╔══██╗██╔══██╗██╔══██╗
    ██████╔╝███████║     ██║██║   ██║██║██║     ███████║███████║███████║██████╔╝
    ██╔══██╗██╔══██║██   ██║╚██╗ ██╔╝██║██║     ██╔══██║██╔══██║██╔══██║██╔══██╗
    ██║  ██║██║  ██║╚█████╔╝ ╚████╔╝ ██║╚██████╗██║  ██║██║  ██║██║  ██║██║  ██║
    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚════╝   ╚═══╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
    """)
    print("="*60 + f"{E}")
    print(f"{C}[SYSTEM]{E} Project: RAJ-VICHAAR | Core: Content Intelligence Engine")
    print(f"{C}[SYSTEM]{E} Local Time: {time.strftime('%H:%M:%S')} | Target: Localhost\n")

def simulated_hex_scan(filename):
    """Simulates a low-level binary scan for aesthetic effect."""
    print(f"{Y}[*] Initiating bitstream analysis of {filename}...{E}")
    for _ in range(5):
        hex_line = " ".join([f"{random.randint(0, 255):02x}" for _ in range(8)])
        print(f"    {B}0x{random.randint(1000, 9999):04x}  {hex_line}  | ANALYZING BIT_DEPTH |{E}")
        time.sleep(0.2)

def classify_content(content):
    """
    Analyzes content against the VICHAAR_CONFIG.
    Returns the highest classification level matched.
    """
    matched_category = None
    highest_level = -1

    for key, data in VICHAAR_CONFIG.items():
        found = [word for word in data['keywords'] if word in content.lower()]
        if found:
            if data['level'] > highest_level:
                highest_level = data['level']
                matched_category = data
                matched_category['found_words'] = found

    return matched_category

def process_document(filepath):
    """Workflow for processing a single document."""
    if not os.path.exists(filepath):
        print(f"{R}[-] Error: Resource {filepath} not found.{E}")
        return

    simulated_hex_scan(filepath)
    
    with open(filepath, 'r') as f:
        data = f.read()

    print(f"{C}[*] Cross-referencing content with Vichaar Sensitivity Matrix...{E}")
    time.sleep(1)
    
    result = classify_content(data)

    if result:
        print(f"\n{G}[+] SCAN COMPLETE: CATEGORIZATION IDENTIFIED{E}")
        print(f"{'-'*45}")
        print(f" CATEGORY: {result['color']}{BOLD}{result['label']}{E}")
        print(f" EVIDENCE: {', '.join(result['found_words'])}")
        print(f" ACTION:   Apply marking requirements immediately.")
        print(f"{'-'*45}\n")
    else:
        print(f"\n{G}[+] SCAN COMPLETE: Document is PUBLIC / UNCLASSIFIED.{E}\n")

# ==========================================
# MAIN EXECUTION
# ==========================================

def start_engine():
    display_header()
    
    # Setup dummy data for Thonny execution
    test_file = "vichaar_payload.txt"
    with open(test_file, "w") as f:
        f.write("This document contains internal tax record information and aadhar identification numbers.")

    print(f"{C}[MENU] Select Operation Mode:{E}")
    print(" 1. Scan specific file (vichaar_payload.txt)")
    print(" 2. Scan Directory (Audit Mode)")
    print(" 3. Exit Intelligence Engine")
    
    cmd = input(f"\n{B}raj-vichaar@root:~# {E}")

    if cmd == "1":
        process_document(test_file)
    elif cmd == "2":
        print(f"{Y}[!] Audit Mode requires elevated privileges. Feature locked.{E}")
    else:
        print(f"{R}[!] Terminating Vichaar processes...{E}")
        sys.exit()

if __name__ == "__main__":
    try:
        start_engine()
    except KeyboardInterrupt:
        print(f"\n{R}[!] Manual Override Detected. Exiting.{E}")