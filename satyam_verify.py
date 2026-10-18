import os
import sys
import time
import hashlib
from datetime import datetime

# ==========================================
# SATYAM-VERIFY: PATH OF TRUTH 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;231m', '\033[38;5;220m', '\033[38;5;51m', '\033[38;5;33m', '\033[38;5;246m'
C6, C7, C8, C9, C10  = '\033[38;5;93m', '\033[38;5;34m', '\033[38;5;226m', '\033[38;5;160m', '\033[38;5;180m'
C11, C12, C13, C14, C15 = '\033[38;5;254m', '\033[38;5;39m', '\033[38;5;250m', '\033[38;5;202m', '\033[38;5;242m'
C16, C17, C18, C19, C20 = '\033[38;5;232m', '\033[38;5;124m', '\033[38;5;28m', '\033[38;5;214m', '\033[38;5;233m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE ALL-SEEING EYE OF TRUTH (SATYAM)
# ==========================================
def satyam_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C1}             .---.
    {C1}            /  {C2}_{C1}  \\         {C1}S A T Y A M
    {C2}           |  {C3}(@){C2}  |        {C4}V E R I F Y
    {C1}            \\  {C2}-{C1}  /         {C15}v7.7 [IDENTITY_PROOFING]
    {C2}             '---'
    {C13}          [{C7}ID_VALIDATED{C13}]
    """
    print(logo)
    print(f"{C1}{BLD}   SATYAM-VERIFY: MULTI-STAGE IDENTITY PROOFING PIPELINE{RST}\n")
    
    # Verification Stages animation
    stages = ["Document_OCR", "Facial_Matching", "Liveness_Check", "Sanction_List_Scan"]
    for s in stages:
        sys.stdout.write(f"\r{C15}[{C2}WAIT{C15}] {C1}Verifying Truth Anchors: {C3}{s:<20}{RST}")
        sys.stdout.flush()
        time.sleep(0.3)
    print(f"\n{C7}[+] Identity Proofing Engine Online. Monitoring Ingress Points.{RST}\n")

# ==========================================
# ARCHITECTURE: IDENTITY VALIDATION ENGINE
# ==========================================
class SatyamVerifier:
    """Simulates an identity verification system with digital footprint analysis."""
    def __init__(self):
        # Database of 'Proven' Identities
        self.proven_identities = {
            "raj_gautam": {"aadhaar_hash": "a1b2c3d4", "status": "VERIFIED"},
            "admin_vbspu": {"aadhaar_hash": "e5f6g7h8", "status": "VERIFIED"}
        }

    def verify_request(self, user_id, doc_id, liveness_score):
        """Validates if the person is who they claim to be."""
        ts = datetime.now().strftime("%H:%M:%S")
        print(f"{C15}[{ts}] {C4}PROBING: {C1}{user_id:<15}{RST} | {C13}Doc_ID: {doc_id}{RST}")
        time.sleep(1)

        # 1. Document Integrity Check
        doc_hash = hashlib.md5(doc_id.encode()).hexdigest()[:8]
        
        # 2. Liveness & Truth Check
        # Formula: $Confidence = Liveness \times Match\_Ratio$
        print(f"    {C5}>> Analyzing Liveness Telemetry: {C2}{liveness_score * 100}% Confidence{RST}")
        
        if user_id in self.proven_identities and liveness_score > 0.85:
            if self.proven_identities[user_id]["aadhaar_hash"] == doc_hash:
                print(f"    {C18}[✔] IDENTITY PROVEN: {C1}{user_id}{C18} is authentic.{RST}")
                print(f"    {C7}{BLD}    ACCESS TOKEN ISSUED FOR CUI REPOSITORY.{RST}\n")
                return True
            else:
                self._trigger_identity_alarm(ts, user_id, "DOCUMENT_HASH_MISMATCH")
        else:
            reason = "LOW_LIVENESS_CONFIDENCE" if liveness_score <= 0.85 else "IDENTITY_NOT_FOUND"
            self._trigger_identity_alarm(ts, user_id, reason)
        return False

    def _trigger_identity_alarm(self, ts, user, reason):
        print(f"\n{C9}{BLD}!!! SATYAM-VERIFY: IDENTITY FRAUD DETECTED !!!{RST}")
        print(f"{C9}│ {C1}TIMESTAMP : {C10}{ts}{RST}")
        print(f"{C9}│ {C1}CLAIMANT  : {C15}{user}{RST}")
        print(f"{C9}│ {C1}VIOLATION : {C9}{BLD}{reason}{RST}")
        print(f"{C9}│ {C1}ACTION    : {C9}{BLD}BLOCKING_REQUEST | ALERTING_PROCTOR_OFFICE{RST}")
        print(f"{C9}└{'─'*55}{RST}\n")
        time.sleep(0.5)

# ==========================================
# SIMULATION: IDENTITY GATEKEEPER
# ==========================================
if __name__ == "__main__":
    try:
        satyam_banner_anim()
        verifier = SatyamVerifier()
        
        # Case 1: Raj Gautam - Authentic Access
        verifier.verify_request("raj_gautam", "aadhaar_123", 0.98)
        
        # Case 2: Deepfake/Bot Attempt (Low Liveness)
        time.sleep(1)
        verifier.verify_request("admin_vbspu", "aadhaar_456", 0.45)
        
        # Case 3: Identity Theft Attempt (Wrong Doc ID)
        time.sleep(1)
        verifier.verify_request("raj_gautam", "fake_doc_999", 0.95)

    except KeyboardInterrupt:
        print(f"\n{C9}[!] Verification Engine Shutdown.{RST}")