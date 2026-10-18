import os
import sys
import time
import secrets
from datetime import datetime

# ==========================================
# RAJPUT-SCANNER: VALOR & DEFENSE 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;208m', '\033[38;5;247m', '\033[38;5;220m', '\033[38;5;160m', '\033[38;5;180m'
C6, C7, C8, C9, C10  = '\033[38;5;196m', '\033[38;5;241m', '\033[38;5;202m', '\033[38;5;28m', '\033[38;5;27m'
C11, C12, C13, C14, C15 = '\033[38;5;35m', '\033[38;5;255m', '\033[38;5;130m', '\033[38;5;202m', '\033[38;5;238m'
C16, C17, C18, C19, C20 = '\033[38;5;232m', '\033[38;5;46m', '\033[38;5;214m', '\033[38;5;215m', '\033[38;5;233m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE CROSSED SWORDS (RAJPUT)
# ==========================================
def rajput_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C1}             /\\          /\\
    {C2}            /  \\        /  \\
    {C2}           /    \\      /    \\
    {C3}          /      \\____/      \\
    {C4}         |  {C3}(@){C4}  |    |  {C3}(@){C4}  |
    {C7}         |________|____|________|
    {C1}        [ RAJPUT VULN-SCANNER v6.2 ]
    """
    print(logo)
    print(f"{C1}{BLD}   RAJPUT-SCANNER: DEFENDING THE CUI PERIMETER{RST}\n")
    
    # Scanning initialization animation
    modules = ["Port_Scanner", "Version_Auditor", "Config_Checker", "CVSS_Calculator"]
    for m in modules:
        sys.stdout.write(f"\r{C15}[{C3}SCAN{C15}] {C12}Deploying Scout: {C1}{m:<18}{RST}")
        sys.stdout.flush()
        time.sleep(0.3)
    print(f"\n{C17}[+] Scouting Complete. Analyzing Fortification Weaknesses...{RST}\n")

# ==========================================
# ARCHITECTURE: VULNERABILITY AUDIT ENGINE
# ==========================================
class RajputScanner:
    """Simulates a VAPT scanner with scoring logic."""
    def __init__(self):
        self.vuln_database = {
            "PORT_21": {"name": "FTP Anonymous Access", "severity": "HIGH", "cvss": 8.5},
            "VER_OLD": {"name": "Outdated OpenSSL (Heartbleed Risk)", "severity": "CRITICAL", "cvss": 9.8},
            "CFG_WEAK": {"name": "Default Admin Credentials", "severity": "CRITICAL", "cvss": 10.0},
            "LOG_FAIL": {"name": "No Audit Logging Enabled", "severity": "MEDIUM", "cvss": 5.0}
        }

    def run_assessment(self, target):
        print(f"{C13}[*] Target Identified: {C12}{target}{RST}\n")
        findings = []
        
        # Simulated scan events
        print(f"{C15}{BLD}{'VULNERABILITY ID':<20} | {'NAME':<30} | {'SCORE'}{RST}")
        print(f"{C15}{'-'*70}{RST}")
        
        for vid, data in self.vuln_database.items():
            time.sleep(0.5)
            color = C4 if data['cvss'] > 7.5 else C1 if data['cvss'] > 4.0 else C11
            print(f"{C2}{vid:<20} | {C12}{data['name']:<30} | {color}{data['cvss']}{RST}")
            findings.append(data['cvss'])
            
        self._calculate_total_risk(findings)

    def _calculate_total_risk(self, scores):
        # Calculate Risk using a weighted average simulation
        # Formula: $Risk = \sum \frac{CVSS_i}{N}$
        avg_score = sum(scores) / len(scores)
        print(f"\n{C16}┌─────────────────────────────────────────────────────┐")
        print(f"{C16}│ {C3}OVERALL SECURITY POSTURE REPORT{' '*20} {C16}│")
        print(f"{C16}├─────────────────────────────────────────────────────┤")
        print(f"{C16}│ {C12}MEAN CVSS SCORE   : {C4}{BLD}{avg_score:.1f}/10.0{' '*21} {C16}│")
        print(f"{C16}│ {C12}THREAT LEVEL      : {C4}{BLD}RED ALERT{' '*25} {C16}│")
        print(f"{C16}│ {C12}REMEDIATION ETA   : {C1}IMMEDIATE ACTION REQUIRED{' '*11} {C16}│")
        print(f"{C16}└─────────────────────────────────────────────────────┘{RST}\n")

# ==========================================
# SIMULATION: VULNERABILITY SCAN
# ==========================================
if __name__ == "__main__":
    try:
        rajput_banner_anim()
        scanner = RajputScanner()
        scanner.run_assessment("Internal-CUI-Vault-01")
        print(f"{C11}[✔] Scan report exported to rajput_audit.log. Fix the criticals first!{RST}")
    except KeyboardInterrupt:
        print(f"\n{C4}[!] Scanner Aborted. Fortress status unknown.{RST}")