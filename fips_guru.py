import os
import sys
import time
import hashlib
from datetime import datetime

# ==========================================
# FIPS-GURU: CRYPTO PURITY 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;220m', '\033[38;5;33m', '\033[38;5;231m', '\033[38;5;244m', '\033[38;5;232m'
C6, C7, C8, C9, C10  = '\033[38;5;214m', '\033[38;5;40m', '\033[38;5;250m', '\033[38;5;51m', '\033[38;5;196m'
C11, C12, C13, C14, C15 = '\033[38;5;118m', '\033[38;5;158m', '\033[38;5;18m', '\033[38;5;202m', '\033[38;5;242m'
C16, C17, C18, C19, C20 = '\033[38;5;234m', '\033[38;5;124m', '\033[38;5;28m', '\033[38;5;214m', '\033[38;5;233m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE SYMBOL OF CRYPTO TRUTH (FIPS-GURU)
# ==========================================
def fips_guru_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C1}             _________
    {C1}            / {C2} FIPS-G {C1} \\
    {C3}           |  {C10}<{C1}MOD-V{C10}>{C3}  |       {C1}F I P S - G U R U
    {C3}           |  {C1}140-3 V{C3}  |       {C4}C R Y P T O - A U D I T
    {C1}            \\_________/        {C15}v8.4 [CMVP_VALIDATED]
    {C13}          [{C11}CIPHER_LIST_LOADED{C13}]
    """
    print(logo)
    print(f"{C1}{BLD}   FIPS-GURU: CRYPTOGRAPHIC MODULE & ALGORITHM VALIDATOR{RST}\n")
    
    # Cipher inspection animation
    ciphers = ["AES_256_GCM", "SHA_512_HASH", "RSA_4096_PKI", "ECDSA_P384"]
    for c in ciphers:
        sys.stdout.write(f"\r{C15}[{C2}GURU{C15}] {C1}Inspecting Algorithm Integrity: {C12}{c:<20}{RST}")
        sys.stdout.flush()
        time.sleep(0.3)
    print(f"\n{C11}[+] Crypto-Baseline verified. Scanning local application modules.{RST}\n")

# ==========================================
# ARCHITECTURE: CRYPTO COMPLIANCE ENGINE
# ==========================================
class FipsGuruAuditor:
    """Audits software modules for FIPS-approved cryptographic practices."""
    def __init__(self):
        # Approved vs Legacy/Deprecated Lists
        self.approved_algorithms = ["AES-256", "SHA-256", "SHA-512", "RSA-3072", "ECDSA"]
        self.legacy_insecure = ["MD5", "SHA-1", "DES", "RC4", "3DES"]

    def audit_crypto_stack(self, app_name, modules):
        ts = datetime.now().strftime("%H:%M:%S")
        print(f"{C13}[{ts}] {C4}AUDITING STACK: {C1}{app_name}{RST}")
        time.sleep(0.8)
        
        violations = 0
        print(f"\n{C4}{'MODULE':<15} | {'ALGORITHM':<12} | {'FIPS STATUS'}{RST}")
        print(f"{C4}{'-'*50}{RST}")

        for mod, algo in modules.items():
            time.sleep(0.5)
            if algo in self.approved_algorithms:
                status = f"{C11}APPROVED{RST}"
            elif algo in self.legacy_insecure:
                status = f"{C10}{BLD}CRITICAL VIOLATION{RST}"
                violations += 1
            else:
                status = f"{C1}UNKNOWN / UNVALIDATED{RST}"
                violations += 1
            
            print(f"{C9}{mod:<15}{RST} | {C3}{algo:<12}{RST} | {status}")

        self._issue_certificate(app_name, violations)

    def _issue_certificate(self, app, v):
        print(f"\n{C16}┌─────────────────────────────────────────────────────┐")
        if v == 0:
            print(f"{C16}│ {C11}{BLD}FIPS 140-3 CONFORMANCE: SUCCESSFUL{' '*15} {C16}│")
            print(f"{C16}├─────────────────────────────────────────────────────┤")
            print(f"{C16}│ {C3}The application '{app}' meets all crypto standards.{' '*3}│")
        else:
            print(f"{C16}│ {C10}{BLD}FIPS 140-3 CONFORMANCE: FAILED{' '*19} {C16}│")
            print(f"{C16}├─────────────────────────────────────────────────────┤")
            print(f"{C16}│ {C8}Detected {v} non-compliant cryptographic practices.{' '*5}│")
        print(f"{C16}└─────────────────────────────────────────────────────┘{RST}\n")

# ==========================================
# SIMULATION: CRYPTO STACK SCAN
# ==========================================
if __name__ == "__main__":
    try:
        fips_guru_banner_anim()
        auditor = FipsGuruAuditor()
        
        # Test Case 1: Secure VBSPU Inventory Module
        vbspu_stack = {
            "Database_Enc": "AES-256",
            "User_Hashing": "SHA-512",
            "API_Signing": "ECDSA"
        }
        auditor.audit_crypto_stack("VBSPU_Inventory_Pro", vbspu_stack)
        
        # Test Case 2: Insecure Legacy Legacy Module
        legacy_stack = {
            "Old_Session_ID": "MD5",
            "Legacy_VPN": "DES"
        }
        time.sleep(1)
        auditor.audit_crypto_stack("Legacy_Admin_Portal", legacy_stack)

    except KeyboardInterrupt:
        print(f"\n{C10}[!] Guru is silent. Crypto-audit incomplete.{RST}")