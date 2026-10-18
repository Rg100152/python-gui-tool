import os
import sys
import time
from datetime import datetime

# ==========================================
# NIST-RAJ: SOVEREIGN STANDARDS 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;33m', '\033[38;5;220m', '\033[38;5;252m', '\033[38;5;231m', '\033[38;5;208m'
C6, C7, C8, C9, C10  = '\033[38;5;244m', '\033[38;5;93m', '\033[38;5;160m', '\033[38;5;137m', '\033[38;5;232m'
C11, C12, C13, C14, C15 = '\033[38;5;121m', '\033[38;5;158m', '\033[38;5;18m', '\033[38;5;202m', '\033[38;5;242m'
C16, C17, C18, C19, C20 = '\033[38;5;234m', '\033[38;5;124m', '\033[38;5;28m', '\033[38;5;214m', '\033[38;5;233m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE SHIELD OF COMPLIANCE (NIST-RAJ)
# ==========================================
def nist_raj_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C1}             __________
    {C1}            / {C2}NIST-RAJ{C1} \\
    {C3}           |   {C5}[800-171]{C3} |       {C1}N I S T - R A J
    {C3}           |   {C2}VBSPU_ID{C3}  |       {C5}C O M P L I A N C E
    {C1}            \\__________/        {C15}v8.3 [GOV_VALIDATOR]
    {C13}          [{C11}BASELINES_SYNCED{C13}]
    """
    print(logo)
    print(f"{C1}{BLD}   NIST-RAJ: AUTOMATED NIST 800-171 CONTROL VERIFICATION{RST}\n")
    
    # NIST Family Verification animation
    families = ["Access_Control", "Audit_Accountability", "System_Integrity", "Media_Protection"]
    for fam in families:
        sys.stdout.write(f"\r{C15}[{C2}NIST{C15}] {C1}Scanning Family: {C12}{fam:<22}{RST}")
        sys.stdout.flush()
        time.sleep(0.3)
    print(f"\n{C11}[+] Standards Baseline Established. Checking local system artifacts.{RST}\n")

# ==========================================
# ARCHITECTURE: COMPLIANCE VALIDATOR
# ==========================================
class NistRajValidator:
    """Maps system configuration to NIST 800-171 regulatory controls."""
    def __init__(self):
        # NIST 800-171 Families and Controls
        self.controls = {
            "3.1.1": {"family": "Access Control", "req": "Limit system access to authorized users"},
            "3.1.3": {"family": "Access Control", "req": "Control flow of CUI"},
            "3.3.1": {"family": "Audit", "req": "Create and retain system audit logs"},
            "3.13.11": {"family": "Systems Protection", "req": "FIPS-validated cryptography"}
        }
        # Simulated System Diagnostics
        self.diagnostics = {
            "3.1.1": "PASS",
            "3.1.3": "FAIL",  # Critical: CUI flowing to unencrypted terminal
            "3.3.1": "PASS",
            "3.13.11": "PASS"
        }

    def validate_standards(self):
        print(f"{C13}[*] Initiating Regulatory Scrutiny Cycle...{RST}\n")
        time.sleep(1)
        
        print(f"{C6}{'CONTROL':<10} | {'NIST FAMILY':<20} | {'STATUS'}{RST}")
        print(f"{C6}{'-'*55}{RST}")
        
        for code, info in self.controls.items():
            time.sleep(0.6)
            result = self.diagnostics[code]
            
            if result == "PASS":
                status = f"{C18}COMPLIANT{RST}"
                color = C18
            else:
                status = f"{C8}{BLD}NON-COMPLIANT{RST}"
                color = C8
                
            print(f"{C2}{code:<10}{RST} | {C4}{info['family']:<20}{RST} | {status}")

        self._render_compliance_index()

    def _render_compliance_index(self):
        # Compliance Score calculation
        total = len(self.controls)
        passed = list(self.diagnostics.values()).count("PASS")
        score = (passed / total) * 100
        
        print(f"\n{C16}┌─────────────────────────────────────────────────────┐")
        print(f"{C16}│ {C1}NIST 800-171 COMPLIANCE DASHBOARD{' '*18} {C16}│")
        print(f"{C16}├─────────────────────────────────────────────────────┤")
        print(f"{C16}│ {C3}TOTAL CONTROLS SCANNED   : {total:<10}{' '*16} {C16}│")
        print(f"{C16}│ {C3}CONTROLS FAILED          : {C8}{BLD}{total - passed:<10}{RST}{' '*16} {C16}│")
        print(f"{C16}│ {C3}RAJ COMPLIANCE INDEX     : {C11}{BLD}{score:.1f}%{' '*19} {C16}│")
        print(f"{C16}└─────────────────────────────────────────────────────┘{RST}\n")

# ==========================================
# SIMULATION: STANDARDS AUDIT
# ==========================================
if __name__ == "__main__":
    try:
        nist_raj_banner_anim()
        validator = NistRajValidator()
        validator.validate_standards()
        print(f"{C11}[✔] Validation cycle complete. Exporting results for BCA Proctor Review.{RST}")
    except KeyboardInterrupt:
        print(f"\n{C8}[!] Audit Terminated. System Compliance Status: UNKNOWN.{RST}")