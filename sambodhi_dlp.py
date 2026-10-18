import os
import sys
import time
import re
import secrets

# ==========================================
# SAMBODHI-DLP: ENLIGHTENMENT 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;220m', '\033[38;5;255m', '\033[38;5;33m', '\033[38;5;208m', '\033[38;5;51m'
C6, C7, C8, C9, C10  = '\033[38;5;246m', '\033[38;5;202m', '\033[38;5;93m', '\033[38;5;40m', '\033[38;5;196m'
C11, C12, C13, C14, C15 = '\033[38;5;39m', '\033[38;5;18m', '\033[38;5;28m', '\033[38;5;213m', '\033[38;5;137m'
C16, C17, C18, C19, C20 = '\033[38;5;250m', '\033[38;5;232m', '\033[38;5;214m', '\033[38;5;22m', '\033[38;5;153m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE DHARMA WHEEL (SAMBODHI)
# ==========================================
def sambodhi_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C1}           _.._
    {C1}         .'    '.
    {C1}    _   /  {C5}O  O{C1}  \\   _
    {C1}   (_|  |  {C3}  |  {C1}  |  |_)
    {C1}     |  \\  {C5}O__O{C1}  /  |
    {C1}     '.  '.____.'  .'
    {C1}       '..______..'
    """
    print(logo)
    print(f"{C1}{BLD}   SAMBODHI-DLP v4.1: DATA EXFILTRATION PROTECTION{RST}\n")
    
    # Inspection pulse animation
    for i in range(15):
        sys.stdout.write(f"\r{C6}[{C9}{'#' * (i%6)}{C6}] {C11}Scanning Outbound Buffer for CUI Markers...{RST}")
        sys.stdout.flush()
        time.sleep(0.1)
    print(f"\n{C9}[+] Deep Content Inspection (DCI) Subsystem Online.{RST}\n")

# ==========================================
# ARCHITECTURE: CONTENT INSPECTION ENGINE
# ==========================================
class DLPEngine:
    """Monitors and intercepts data exfiltration attempts."""
    def __init__(self):
        # Sensitive patterns (RegEx for CUI, SSN, Secret keys)
        self.forbidden_patterns = [
            r"(?i)CONFIDENTIAL",
            r"(?i)CUI//SP-PRVT",
            r"(?i)RESTRICTED",
            r"\b\d{3}-\d{2}-\d{4}\b", # SSN Pattern
            r"(?i)NUCLEAR_SPECS",
            r"(?i)TOP_SECRET"
        ]

    def inspect_and_filter(self, payload_name, content):
        """Analyzes content and decides whether to block or allow."""
        print(f"{C16}[*] INTERCEPTED: {C5}{payload_name}{RST} {C6}(Size: {len(content)} bytes){RST}")
        time.sleep(0.8)
        
        violations = []
        for pattern in self.forbidden_patterns:
            if re.search(pattern, content):
                match = re.search(pattern, content).group()
                violations.append(match)

        if violations:
            self._trigger_block(payload_name, violations)
            return False
        else:
            print(f"{C9}[✔] PASS: No exfiltration markers detected.{RST}\n")
            return True

    def _trigger_block(self, name, markers):
        print(f"{C10}{BLD}!!! BLOCK ALERT: UNAUTHORIZED EXFILTRATION !!!{RST}")
        print(f"{C10}│ {C2}FILE    : {C18}{name}{RST}")
        print(f"{C10}│ {C2}REASON  : {C10}Sensitive content detected.{RST}")
        print(f"{C10}│ {C2}MARKERS : {C14}{', '.join(markers)}{RST}")
        print(f"{C10}│ {C2}ACTION  : {C10}{BLD}EGRESS BLOCKED & INCIDENT LOGGED.{RST}")
        print(f"{C10}└{'─'*55}{RST}\n")

# ==========================================
# SIMULATION: NETWORK EGRESS STREAM
# ==========================================
def simulate_egress():
    sambodhi_banner_anim()
    dlp = DLPEngine()
    
    # Simulation payloads
    outbound_stream = [
        ("email_draft_01.txt", "Hello, please find the meeting minutes attached."),
        ("research_data.csv", "ID, Value\n101, 45.5\n102, 66.8"),
        ("leak_attempt.sh", "Sending CUI//SP-PRVT nuclear_specs to external cloud..."),
        ("hr_report.docx", "Employee record for SSN 123-45-6789 is verified."),
        ("system_ping.pkg", "Keep-alive signal")
    ]
    
    print(f"{C8}[!] MONITORING OUTBOUND NETWORK INTERFACE (eth0)...{RST}\n")
    
    for filename, content in outbound_stream:
        # Simulate network delay
        time.sleep(1.2)
        dlp.inspect_and_filter(filename, content)

    print(f"{C1}{BLD}[*] Sambodhi session active. All egress channels secured.{RST}")

if __name__ == "__main__":
    try:
        simulate_egress()
    except KeyboardInterrupt:
        print(f"\n{C10}[!] DLP Shutdown.{RST}")