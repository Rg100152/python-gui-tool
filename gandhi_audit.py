import os
import time
import inspect
import re
import sys

# ==========================================
# GANDHI-AUDIT: FORENSIC COLOR THEME
# ==========================================
W = '\033[97m'   # White (Neutral)
C = '\033[96m'   # Cyan (Headers)
G = '\033[92m'   # Green (Pass/Truth)
R = '\033[91m'   # Red (Violation/Lie)
Y = '\033[93m'   # Yellow (Warning)
E = '\033[0m'    # Reset
BOLD = '\033[1m'

# ==========================================
# TEST ENVIRONMENT GENERATION
# ==========================================
def synthesize_evidence():
    """Generates files with intentional classification errors for auditing."""
    files = {
        "report_alpha.txt": "[PUBLIC]\nJust a standard meeting agenda. No secrets here.",
        "report_beta.txt": "[PUBLIC]\nAdmin login for the database is admin:password123.", # UNDER-CLASSIFIED
        "report_gamma.txt": "[TOP SECRET // CUI]\nThe cafeteria will serve pizza on Friday." # OVER-CLASSIFIED
    }
    for filename, content in files.items():
        with open(filename, "w") as f:
            f.write(content)
    return list(files.keys())

# ==========================================
# AUDIT RULES (PLUGIN ARCHITECTURE)
# ==========================================
# Any function starting with 'rule_' is automatically discovered by the engine.

def rule_detect_underclassification_credentials(content):
    """Detects if a public file contains passwords/credentials."""
    if "[PUBLIC]" in content.upper():
        # Regex to find common password patterns
        if re.search(r'(?i)(password|pass|pwd)\s*[:=]\s*\w+', content):
            return "FAIL", "Under-classified: Credentials found in [PUBLIC] document."
    return "PASS", "No exposed credentials in public domain."

def rule_detect_underclassification_pii(content):
    """Detects if a public file contains Aadhar or ID numbers."""
    if "[PUBLIC]" in content.upper():
        # Regex for fake Aadhar-style 12 digit numbers
        if re.search(r'\b\d{4}\s\d{4}\s\d{4}\b', content):
            return "FAIL", "Under-classified: PII (Aadhar format) exposed in [PUBLIC] document."
    return "PASS", "No PII exposure detected."

def rule_detect_overclassification(content):
    """Detects if a file is marked Secret but contains trivial data."""
    if "[TOP SECRET" in content.upper() or "[CUI" in content.upper():
        trivial_words = ["cafeteria", "lunch", "pizza", "holiday", "break"]
        if any(word in content.lower() for word in trivial_words):
            return "WARN", "Over-classified: Trivial keywords found in highly restricted document."
    return "PASS", "Classification level appears justified."

# ==========================================
# CORE ENGINE (INTROSPECTION)
# ==========================================

def display_forensic_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = f"""{W}{BOLD}
      ____                 _ _     _        _             _ _ _   
     / ___| __ _ _ __   __| | |__ (_)      / \  _   _  __| (_) |_ 
    | |  _ / _` | '_ \ / _` | '_ \| |____ / _ \| | | |/ _` | | __|
    | |_| | (_| | | | | (_| | | | | |____/ ___ \ |_| | (_| | | |_ 
     \____|\__,_|_| |_|\__,_|_| |_|_|   /_/   \_\__,_|\__,_|_|\__|
    {E}"""
    print(banner)
    print(f"{C}[*] ARCHITECTURE: REFLECTION & INTROSPECTION (AUTO-DISCOVERY){E}")
    print(f"{C}[*] OBJECTIVE: DETECT MISCLASSIFICATION & COMPLIANCE ANOMALIES{E}\n")

def run_auditor():
    display_forensic_banner()
    
    # 1. Synthesize target data
    print(f"{Y}[~] Synthesizing audit evidence...{E}")
    targets = synthesize_evidence()
    time.sleep(1)
    
    # 2. Auto-discover rules using Python's 'inspect' module
    current_module = sys.modules[__name__]
    # Find all functions in this file that start with 'rule_'
    active_rules = [
        func for name, func in inspect.getmembers(current_module, inspect.isfunction)
        if name.startswith("rule_")
    ]
    
    print(f"{G}[+] Engine initialized. Discovered {len(active_rules)} active audit rules.{E}")
    print(f"{C}[*] Commencing deep-pattern regex scanning...{E}\n")
    time.sleep(1)

    # 3. Print Tabular Header
    print(f"{W}{BOLD}{'TARGET FILE':<18} | {'RULE APPLIED':<45} | {'STATUS':<6} | {'FORENSIC NOTES'}{E}")
    print("-" * 120)

    # 4. Execute Map-Reduce style processing
    for filepath in targets:
        with open(filepath, "r") as f:
            content = f.read()
            
        for rule in active_rules:
            # Dynamically call the rule function
            status, message = rule(content)
            
            # Format the output based on status
            rule_name = rule.__name__.replace("rule_", "").replace("_", " ").title()
            
            if status == "PASS":
                status_color = f"{G}PASS{E}"
                note_color = W
            elif status == "FAIL":
                status_color = f"{R}FAIL{E}"
                note_color = R
            elif status == "WARN":
                status_color = f"{Y}WARN{E}"
                note_color = Y
                
            # Print tabular row
            print(f"{C}{filepath:<18}{E} | {rule_name:<45} | {status_color:<15} | {note_color}{message}{E}")
            time.sleep(0.1) # Simulate processing time per rule
            
        print("-" * 120)

# ==========================================
# EXECUTION
# ==========================================
if __name__ == "__main__":
    run_auditor()
    print(f"\n{C}[SYSTEM] Audit complete. Truth extracted. System standing by.{E}")