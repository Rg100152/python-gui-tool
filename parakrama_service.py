import os
import sys
import time
from datetime import datetime

# ==========================================
# PARAKRAMA-SERVICE: HEROIC MIGHT 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;220m', '\033[38;5;160m', '\033[38;5;244m', '\033[38;5;252m', '\033[38;5;130m'
C6, C7, C8, C9, C10  = '\033[38;5;33m', '\033[38;5;232m', '\033[38;5;93m', '\033[38;5;208m', '\033[38;5;255m'
C11, C12, C13, C14, C15 = '\033[38;5;34m', '\033[38;5;30m', '\033[38;5;235m', '\033[38;5;202m', '\033[38;5;238m'
C16, C17, C18, C19, C20 = '\033[38;5;232m', '\033[38;5;124m', '\033[38;5;28m', '\033[38;5;214m', '\033[38;5;233m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE SYMBOL OF VALOR (PARAKRAMA)
# ==========================================
def parakrama_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C1}             /\\
    {C1}            /  \\           {C1}P A R A K R A M A
    {C5}           /____\\          {C9}S E R V I C E
    {C2}          |  {C10}[#]{C2}  |         {C15}v6.7 [ATTACK_SURFACE_MIN]
    {C5}          |      |
    {C7}         /________\\
    """
    print(logo)
    print(f"{C1}{BLD}   PARAKRAMA-SERVICE: SYSTEM PROCESS PURGING & DE-CLUTTERING{RST}\n")
    
    # Audit sequence animation
    tasks = ["Process_Enumeration", "Dependency_Check", "Critical_Path_Lock", "Redundant_Purge"]
    for task in tasks:
        sys.stdout.write(f"\r{C7}[{C1}SCAN{C7}] {C4}Analyzing System Bloat: {C6}{task:<20}{RST}")
        sys.stdout.flush()
        time.sleep(0.3)
    print(f"\n{C11}[+] Audit Complete. Identifying non-warrior processes for termination.{RST}\n")

# ==========================================
# ARCHITECTURE: SERVICE PRUNING ENGINE
# ==========================================
class ParakramaPruner:
    """Identifies and disables unnecessary services to harden the OS."""
    def __init__(self):
        # Service Catalog
        self.services = {
            "CUI_Vault_Sync": {"status": "Running", "criticality": "ESSENTIAL"},
            "Print_Spooler": {"status": "Running", "criticality": "REDUNDANT"},
            "Remote_Registry": {"status": "Running", "criticality": "DANGEROUS"},
            "Bluetooth_OBEX": {"status": "Running", "criticality": "REDUNDANT"},
            "Kernel_Monitor": {"status": "Running", "criticality": "ESSENTIAL"},
            "Xbox_Live_Auth": {"status": "Running", "criticality": "BLOATWARE"}
        }

    def execute_purging(self):
        print(f"{C13}[*] Initiating Parakrama Protocol: Purging Attack Vectors...{RST}\n")
        purged_count = 0
        
        print(f"{C7}{'SERVICE NAME':<20} | {'CRITICALITY':<12} | {'ACTION'}{RST}")
        print(f"{C7}{'-'*50}{RST}")
        
        for name, info in self.services.items():
            time.sleep(0.6)
            crit = info["criticality"]
            
            if crit in ["REDUNDANT", "DANGEROUS", "BLOATWARE"]:
                action = f"{C2}{BLD}TERMINATED & DISABLED{RST}"
                purged_count += 1
                color = C2 if crit == "DANGEROUS" else C9
            else:
                action = f"{C11}WHITELISTED (KEPT){RST}"
                color = C11

            print(f"{C4}{name:<20} | {color}{crit:<12}{RST} | {action}")

        self._render_victory_stats(len(self.services), purged_count)

    def _render_victory_stats(self, total, purged):
        # Reduction Ratio: $R = \frac{Purged}{Total}$
        reduction = (purged / total) * 100
        print(f"\n{C16}┌─────────────────────────────────────────────────────┐")
        print(f"{C16}│ {C1}PARAKRAMA REDUCTION SUMMARY{' '*24} {C16}│")
        print(f"{C16}├─────────────────────────────────────────────────────┤")
        print(f"{C16}│ {C10}TOTAL SERVICES AUDITED  : {total:<10}{' '*16} {C16}│")
        print(f"{C16}│ {C10}SERVICES ELIMINATED     : {C2}{BLD}{purged:<10}{RST}{' '*16} {C16}│")
        print(f"{C16}│ {C10}ATTACK SURFACE REDUCED  : {C11}{BLD}{reduction:.1f}%{' '*19} {C16}│")
        print(f"{C16}└─────────────────────────────────────────────────────┘{RST}\n")

# ==========================================
# SIMULATION: SERVICE LOCKDOWN
# ==========================================
if __name__ == "__main__":
    try:
        parakrama_banner_anim()
        pruner = ParakramaPruner()
        pruner.execute_purging()
        print(f"{C11}[✔] System streamlined. Parakrama has neutralized unnecessary bloat.{RST}")
    except KeyboardInterrupt:
        print(f"\n{C2}[!] Purging halted. System remains bloated and vulnerable.{RST}")