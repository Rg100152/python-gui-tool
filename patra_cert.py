import os
import sys
import time
import hashlib
from datetime import datetime, timedelta

# ==========================================
# PATRA-CERT: THE OFFICIAL SEAL 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;220m', '\033[38;5;160m', '\033[38;5;230m', '\033[38;5;33m', '\033[38;5;244m'
C6, C7, C8, C9, C10  = '\033[38;5;30m', '\033[38;5;180m', '\033[38;5;93m', '\033[38;5;254m', '\033[38;5;226m'
C11, C12, C13, C14, C15 = '\033[38;5;21m', '\033[38;5;34m', '\033[38;5;136m', '\033[38;5;202m', '\033[38;5;240m'
C16, C17, C18, C19, C20 = '\033[38;5;232m', '\033[38;5;124m', '\033[38;5;28m', '\033[38;5;214m', '\033[38;5;233m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE IMPERIAL LETTER (PATRA)
# ==========================================
def patra_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C3}             _______
    {C3}            /      /|
    {C1}           /______/ |      {C1}P A T R A
    {C1}           | {C2}[S]{C1}   | |      {C4}C E R T
    {C7}           |      | /      {C15}v7.3 [PKI_TRUST_MODEL]
    {C7}           |______|/
    """
    print(logo)
    print(f"{C1}{BLD}   PATRA-CERT: X.509 DIGITAL CERTIFICATE & PKI GATEWAY{RST}\n")
    
    # PKI Chain Validation animation
    stages = ["Root_CA_Check", "Intermediate_Verify", "CRL_Sync", "Key_Exchange"]
    for s in stages:
        sys.stdout.write(f"\r{C15}[{C4}WAIT{C15}] {C9}Establishing Chain of Trust: {C12}{s:<20}{RST}")
        sys.stdout.flush()
        time.sleep(0.3)
    print(f"\n{C12}[+] CA Hierarchy Verified. Trust Anchors Secured.{RST}\n")

# ==========================================
# ARCHITECTURE: DIGITAL CERTIFICATE ENGINE
# ==========================================
class PatraCertEngine:
    """Simulates X.509 certificate issuance, validation, and revocation."""
    def __init__(self):
        # Simulated Certificate Revocation List (CRL)
        self.crl = ["CERT_ID_9901_REVOKED"]
        self.root_ca_sig = "SIG_VBSPU_TRUST_01"

    def validate_certificate(self, cert_id, subject, issuer_sig, expiry_days):
        """Checks the validity of a digital certificate."""
        ts = datetime.now()
        ts_str = ts.strftime("%Y-%m-%d %H:%M")
        
        print(f"{C15}[{ts_str}] {C6}ISSUER: {C1}{issuer_sig}{C5} | {C4}SUBJECT: {C3}{subject}{RST}")
        time.sleep(1)

        # 1. Chain of Trust Check
        if issuer_sig != self.root_ca_sig:
            self._trigger_cert_error(cert_id, "UNTRUSTED_ISSUER")
            return False

        # 2. Revocation Check (CRL)
        if cert_id in self.crl:
            self._trigger_cert_error(cert_id, "CERTIFICATE_REVOKED")
            return False

        # 3. Expiration Check
        if expiry_days < 0:
            self._trigger_cert_error(cert_id, "CERTIFICATE_EXPIRED")
            return False

        # Successful Validation Result
        # Certificate Fingerprint: $Hash = SHA256(Cert_ID + Subject)$
        cert_fingerprint = hashlib.sha256(f"{cert_id}{subject}".encode()).hexdigest()[:16]
        
        print(f"    {C12}[✔] Fingerprint: {cert_fingerprint}")
        print(f"    {C11}{BLD}TRUST ESTABLISHED. Mutual TLS (mTLS) session active.{RST}\n")
        return True

    def _trigger_cert_error(self, cid, reason):
        print(f"\n{C2}{BLD}!!! PATRA-CERT: CRYPTOGRAPHIC TRUST VIOLATION !!!{RST}")
        print(f"{C2}│ {C3}CERT_ID   : {C1}{cid}{RST}")
        print(f"{C2}│ {C3}REASON    : {C2}{BLD}{reason}{RST}")
        print(f"{C2}│ {C3}ACTION    : {C2}{BLD}HANDSHAKE_DENIED | CONNECTION_RESET | SIEM_LOGGED{RST}")
        print(f"{C2}└{'─'*55}{RST}\n")
        time.sleep(0.5)

# ==========================================
# SIMULATION: CERTIFICATE HANDSHAKE
# ==========================================
if __name__ == "__main__":
    try:
        patra_banner_anim()
        pki = PatraCertEngine()
        
        # Scenario 1: Valid Raj Gautam Certificate
        pki.validate_certificate("CERT_ID_1104", "Raj_Gautam_BCA", "SIG_VBSPU_TRUST_01", 365)
        
        # Scenario 2: Revoked Certificate (Stolen)
        time.sleep(1)
        pki.validate_certificate("CERT_ID_9901_REVOKED", "Compromised_Node", "SIG_VBSPU_TRUST_01", 100)
        
        # Scenario 3: Untrusted Self-Signed Certificate (Hacker)
        time.sleep(1)
        pki.validate_certificate("CERT_ID_666", "Hacker_Proxy", "SIG_EVIL_CA_666", 999)

    except KeyboardInterrupt:
        print(f"\n{C2}[!] Trust Anchor Reset.{RST}")