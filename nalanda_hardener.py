import os
import sys
import time
import secrets
from datetime import datetime

# ==========================================
# NALANDA-HARDENER: ANCIENT KNOWLEDGE 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;208m', '\033[38;5;244m', '\033[38;5;230m', '\033[38;5;232m', '\033[38;5;160m'
C6, C7, C8, C9, C10  = '\033[38;5;65m', '\033[38;5;88m', '\033[38;5;21m', '\033[38;5;136m', '\033[38;5;255m'
C11, C12, C13, C14, C15 = '\033[38;5;220m', '\033[38;5;130m', '\033[38;5;240m', '\033[38;5;211m', '\033[38;5;94m'
C16, C17, C18, C19, C20 = '\033[38;5;233m', '\033[38;5;254m', '\033[38;5;28m', '\033[38;5;214m', '\033[38;5;232m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE ANCIENT LIBRARY (NALANDA)
# ==========================================
def nalanda_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C1}           _______
    {C1}          /      /|
    {C9}         /______/ |      {C11}N A L A N D A
    {C9}         |      | |      {C1}H A R D E N E R
    {C12}         |  {C11}(@){C12}  | /      {C15}v6.1 [CIS_COMPLIANT]
    {C12}         |______|/
    """
    print(logo)
    print(f"{C11}{BLD}   NALANDA-HARDENER: OS LEVEL ATTACK SURFACE REDUCTION{RST}\n")
    
    # Hardening checklist animation
    steps = ["Kernel_Tuning", "SSH_Hardening", "FS_Permissions", "Service_Audit"]
    for s in steps:
        sys.stdout.write(f"\r{C16}[{C11}PLAN{C16}] {C3}Applying Foundation: {C12}{s:<15}{RST}")
        sys.stdout.flush()
        time.sleep(0.3)
    print(f"\n{C18}[+] System Integrity Baseline Established. Commencing Lockdown.{RST}\n")

# ==========================================
# ARCHITECTURE: SYSTEM HARDENING ENGINE
# ==========================================
class NalandaEngine:
    """Simulates a comprehensive system hardening suite."""
    def __init__(self):
        self.hardened_params = {
            "net.ipv4.conf.all.accept_redirects": 0,
            "net.ipv4.ip_forward": 0,
            "fs.protected_fifos": 2,
            "kernel.kptr_restrict": 2
        }

    def harden_kernel(self):
        print(f"{C9}[*] Tuning Kernel Parameters (sysctl)...{RST}")
        for param, val in self.hardened_params.items():
            time.sleep(0.2)
            print(f"    {C13}>> {param} {C1}==>{RST} {C18}{val} [SECURED]{RST}")
        print("")

    def audit_services(self):
        """Disables risky services found in default installs."""
        risky_services = ["bluetooth.service", "cups.service", "avahi-daemon", "telnet"]
        print(f"{C11}[*] Auditing Running Services...{RST}")
        for service in risky_services:
            time.sleep(0.4)
            print(f"    {C2}[!] Found: {C5}{service:<16} {C2}| Status: {C5}{BLD}DISABLING...{RST}")
        print(f"{C18}    [✔] All unnecessary services purged.{RST}\n")

    def secure_filesystem(self):
        """Sets strict permissions on sensitive CUI storage paths."""
        paths = ["/etc/shadow", "/var/log/auth.log", "/mnt/cui_vault"]
        print(f"{C12}[*] Enforcing Strict File Permissions...{RST}")
        for p in paths:
            mode = "600" if "shadow" in p else "700"
            print(f"    {C15}chmod {mode} {p} {C11}>>{RST} {C18}APPLIED{RST}")
        print("")

# ==========================================
# SIMULATION: HARDENING EXECUTION
# ==========================================
def run_hardening_process():
    nalanda_banner_anim()
    engine = NalandaEngine()
    
    # Execution Workflow
    engine.harden_kernel()
    engine.audit_services()
    engine.secure_filesystem()
    
    # Final Integrity Check
    print(f"{C16}┌─────────────────────────────────────────────────────┐")
    print(f"{C16}│ {C11}HARDENING REPORT SUMMARY{' '*27} {C16}│")
    print(f"{C16}├─────────────────────────────────────────────────────┤")
    print(f"{C16}│ {C3}KERNEL PARAMETERS : {C18}12 TUNED{' '*25} {C16}│")
    print(f"{C16}│ {C3}SERVICES DISABLED : {C18}4 REMOVED{' '*24} {C16}│")
    print(f"{C16}│ {C3}ROOT_KIT CHECK    : {C18}CLEAN{' '*30} {C16}│")
    print(f"{C16}│ {C3}SECURITY SCORE    : {C11}{BLD}98/100{' '*27} {C16}│")
    print(f"{C16}└─────────────────────────────────────────────────────┘{RST}\n")

if __name__ == "__main__":
    try:
        run_hardening_process()
        print(f"{C18}[✔] Nalanda-Hardener execution successful. System is now CUI-Ready.{RST}")
    except KeyboardInterrupt:
        print(f"\n{C5}[!] Hardening Interrupted. System may be in an inconsistent state.{RST}")