import os
import sys
import time
from datetime import datetime

# ==========================================
# NEETI-PERMISSION: PRINCIPLED GOVERNANCE 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;231m', '\033[38;5;33m', '\033[38;5;232m', '\033[38;5;245m', '\033[38;5;220m'
C6, C7, C8, C9, C10  = '\033[38;5;223m', '\033[38;5;93m', '\033[38;5;18m', '\033[38;5;196m', '\033[38;5;121m'
C11, C12, C13, C14, C15 = '\033[38;5;252m', '\033[38;5;51m', '\033[38;5;94m', '\033[38;5;202m', '\033[38;5;248m'
C16, C17, C18, C19, C20 = '\033[38;5;234m', '\033[38;5;160m', '\033[38;5;34m', '\033[38;5;214m', '\033[38;5;233m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE SCALES OF JUSTICE (NEETI)
# ==========================================
def neeti_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C5}             ___
    {C5}            /   \\          {C1}N E E T I
    {C4}       ____|_____|____     {C2}P E R M I S S I O N
    {C5}      [  {C3}o{C5}  |  {C3}o{C5}  ]    {C15}v6.8 [DAC_AUDITOR]
    {C11}       \\____|____/
    {C13}            |
    """
    print(logo)
    print(f"{C2}{BLD}   NEETI-PERMISSION: FILE SYSTEM PRIVILEGE & ACL ENFORCEMENT{RST}\n")
    
    # Audit sequence animation
    checks = ["Inode_Traversal", "DAC_Verification", "SUID_Bit_Scan", "Orphan_File_Search"]
    for check in checks:
        sys.stdout.write(f"\r{C15}[{C2}LAW{C15}] {C1}Reviewing System Codes: {C12}{check:<20}{RST}")
        sys.stdout.flush()
        time.sleep(0.3)
    print(f"\n{C10}[+] Governance baseline loaded. Principles of Access are active.{RST}\n")

# ==========================================
# ARCHITECTURE: PERMISSION AUDIT ENGINE
# ==========================================
class NeetiAuditor:
    """Audits file system permissions to ensure compliance with CUI security standards."""
    def __init__(self):
        # Target Files and their 'Neeti' (Expected) Permissions
        self.target_files = {
            "/etc/shadow": {"current": "644", "expected": "600", "owner": "root"},
            "/mnt/cui_vault/data.pdf": {"current": "777", "expected": "660", "owner": "cui_mgr"},
            "/usr/bin/sudo": {"current": "4755", "expected": "4755", "owner": "root"}, # SUID bit
            "/home/user/notes.txt": {"current": "644", "expected": "644", "owner": "user"},
            "/var/log/secure": {"current": "666", "expected": "640", "owner": "root"}
        }

    def run_permission_audit(self):
        print(f"{C13}[*] Executing Judicial Scan of File System Inodes...{RST}\n")
        violations = 0
        
        print(f"{C4}{'FILE PATH':<25} | {'PERM':<6} | {'OWNER':<8} | {'STATUS'}{RST}")
        print(f"{C4}{'-'*65}{RST}")
        
        for path, meta in self.target_files.items():
            time.sleep(0.6)
            is_bad = meta["current"] != meta["expected"]
            
            if is_bad:
                status = f"{C9}{BLD}VIOLATION{RST}"
                violations += 1
                color = C9
            else:
                status = f"{C10}COMPLIANT{RST}"
                color = C10

            # Highlight SUID bits
            if "4" in meta["current"] and len(meta["current"]) == 4:
                status += f" {C7}[SUID]{RST}"

            print(f"{C11}{path:<25} | {color}{meta['current']:<6}{RST} | {C12}{meta['owner']:<8}{RST} | {status}")

        self._issue_verdict(len(self.target_files), violations)

    def _issue_verdict(self, total, v):
        # Permission Integrity Index: $PII = 1 - (V/T)$
        pii = (1 - (v / total)) * 100
        print(f"\n{C16}┌─────────────────────────────────────────────────────┐")
        print(f"{C16}│ {C5}NEETI VERDICT & AUDIT SUMMARY{' '*24} {C16}│")
        print(f"{C16}├─────────────────────────────────────────────────────┤")
        print(f"{C16}│ {C1}TOTAL ARTIFACTS SCANNED : {total:<10}{' '*16} {C16}│")
        print(f"{C16}│ {C1}POLICY DEVIATIONS       : {C9}{BLD}{v:<10}{RST}{' '*16} {C16}│")
        print(f"{C16}│ {C1}INTEGRITY INDEX         : {C10}{BLD}{pii:.1f}%{' '*19} {C16}│")
        print(f"{C16}└─────────────────────────────────────────────────────┘{RST}\n")

# ==========================================
# SIMULATION: JUDICIAL REVIEW
# ==========================================
if __name__ == "__main__":
    try:
        neeti_banner_anim()
        judge = NeetiAuditor()
        judge.run_permission_audit()
        print(f"{C10}[✔] Neeti-Permission scan complete. Integrity report generated.{RST}")
    except KeyboardInterrupt:
        print(f"\n{C9}[!] Audit aborted. System permissions remain unchecked.{RST}")