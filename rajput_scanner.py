import os
import sys
import time
import secrets
from datetime import datetime

# ==========================================
# RAJPUT-SCANNER: WARRIOR'S CREED 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;208m', '\033[38;5;196m', '\033[38;5;244m', '\033[38;5;253m', '\033[38;5;94m'
C6, C7, C8, C9, C10  = '\033[38;5;226m', '\033[38;5;28m', '\033[38;5;93m', '\033[38;5;166m', '\033[38;5;39m'
C11, C12, C13, C14, C15 = '\033[38;5;130m', '\033[38;5;18m', '\033[38;5;255m', '\033[38;5;202m', '\033[38;5;95m'
C16, C17, C18, C19, C20 = '\033[38;5;232m', '\033[38;5;88m', '\033[38;5;35m', '\033[38;5;214m', '\033[38;5;233m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE PROTECTIVE SWORD (RAJPUT)
# ==========================================
def rajput_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C4}          /| ________________
    {C4}    O|===|* >________________>
    {C4}          \\|
    {C2}      [ {C13}RAJPUT SCANNER {C2}]
    {C15}    v6.2 [VULN_ASSESSMENT]
    """
    print(logo)
    print(f"{C1}{BLD}   RAJPUT-SCANNER: ENTERPRISE VULNERABILITY SENTRY{RST}\n")
    
    # Scanner Initialization
    for i in range(12):
        sys.stdout.write(f"\r{C3}[{C6}LOAD{C3}] {C13}Syncing Global CVE Database... {C1}{'|/-\\'[i%4]}{RST}")
        sys.stdout.flush()
        time.sleep(0.1)
    print(f"\n{C7}[+] Engine Primed. Vulnerability Signatures Loaded (145,000+).{RST}\n")

# ==========================================
# ARCHITECTURE: VULNERABILITY ASSESSMENT ENGINE
# ==========================================
class RajputScanner:
    """Simulates a system vulnerability scanner."""
    def __init__(self):
        # Database of known weak versions (CVE Simulation)
        self.vuln_db = {
            "Apache/2.4.49": {"CVE": "CVE-2021-41773", "Severity": "CRITICAL", "Risk": 9.8},
            "OpenSSH_7.2p2": {"CVE": "CVE-2016-6210", "Severity": "MEDIUM", "Risk": 5.3},
            "MySQL_5.5.40":  {"CVE": "CVE-2016-6662", "Severity": "HIGH", "Risk": 8.8}
        }

    def calculate_risk(self, impact, probability):
        """Formal risk calculation using simple formula."""
        # Using LaTeX for the formula representation:
        # $Risk = Impact \times Probability$
        return impact * probability

    def scan_target(self, ip):
        """Probes an IP for services and checks against VulnDB."""
        ts = datetime.now().strftime("%H:%M:%S")
        print(f"{C3}[{ts}] {C10}Targeting Node: {C13}{ip}{RST}")
        time.sleep(1)

        # Simulated Service Discovery
        discovered = [
            ("80/tcp", "Apache/2.4.49"),
            ("22/tcp", "OpenSSH_8.9p1"), # Secure version
            ("3306/tcp", "MySQL_5.5.40")
        ]

        results = []
        for port, banner in discovered:
            time.sleep(0.5)
            status = f"{C7}SECURE{RST}"
            cve_id = "N/A"
            severity = "NONE"
            
            if banner in self.vuln_db:
                status = f"{C2}{BLD}VULNERABLE{RST}"
                cve_id = self.vuln_db[banner]["CVE"]
                severity = self.vuln_db[banner]["Severity"]
            
            results.append((port, banner, status, cve_id, severity))
            print(f"    {C15}Port: {port:<8} {C11}Service: {banner:<15} {C3}>> {status}")

        self._display_report(ip, results)

    def _display_report(self, ip, results):
        print(f"\n{C1}{BLD}FINAL VULNERABILITY ASSESSMENT REPORT: {ip}{RST}")
        print(f"{C3}{'━'*75}{RST}")
        print(f"{C13}{'PORT':<10} {'SERVICE':<20} {'STATUS':<15} {'CVE_ID':<15} {'SEVERITY'}{RST}")
        print(f"{C3}{'━'*75}{RST}")
        
        for p, b, s, c, sev in results:
            color = C2 if sev in ["CRITICAL", "HIGH"] else C19 if sev == "MEDIUM" else C7
            print(f"{C4}{p:<10} {C15}{b:<20} {s:<15} {C10}{c:<15} {color}{sev}{RST}")
        print(f"{C3}{'━'*75}{RST}\n")

# ==========================================
# SIMULATION: NETWORK SCAN
# ==========================================
def run_scanner_session():
    rajput_banner_anim()
    scanner = RajputScanner()
    
    targets = ["192.168.1.50", "10.0.0.12"]
    
    print(f"{C8}[!] INITIATING SYSTEM AUDIT...{RST}\n")
    
    for target in targets:
        scanner.scan_target(target)
        time.sleep(1)

if __name__ == "__main__":
    try:
        run_scanner_session()
        print(f"{C7}[✔] Rajput-Scanner scan complete. Audit logs exported to /var/log/rajput/{RST}")
    except KeyboardInterrupt:
        print(f"\n{C2}[!] Scan Aborted.{RST}")
        