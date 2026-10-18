import os
import sys
import time
import hashlib
from datetime import datetime

# ==========================================
# CHAKRI-BIOMETRIC: ETERNAL VISION 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;27m', '\033[38;5;51m', '\033[38;5;93m', '\033[38;5;244m', '\033[38;5;231m'
C6, C7, C8, C9, C10  = '\033[38;5;220m', '\033[38;5;46m', '\033[38;5;196m', '\033[38;5;226m', '\033[38;5;153m'
C11, C12, C13, C14, C15 = '\033[38;5;18m', '\033[38;5;111m', '\033[38;5;252m', '\033[38;5;202m', '\033[38;5;240m'
C16, C17, C18, C19, C20 = '\033[38;5;232m', '\033[38;5;160m', '\033[38;5;28m', '\033[38;5;214m', '\033[38;5;233m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE ALL-SEEING EYE (CHAKRI)
# ==========================================
def chakri_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C2}             .---.
    {C2}            / {C5} _ {C2} \\          {C1}C H A K R I
    {C1}           (  {C2}({C1}@{C2}){C1}  )         {C6}B I O M E T R I C
    {C2}            \\ {C5} ~ {C2} /          {C15}v7.2 [MINUTIAE_HASH]
    {C1}             '---'
    {C11}          [{C7}SCANNING{C11}]
    """
    print(logo)
    print(f"{C1}{BLD}   CHAKRI-BIOMETRIC: HIGH-ASSURANCE BIOMETRIC GATEWAY{RST}\n")
    
    # Scanning hardware initialization
    sensors = ["Optical_Scanner", "Thermal_Live_Check", "Minutiae_Extractor", "Cryptographic_Silo"]
    for s in sensors:
        sys.stdout.write(f"\r{C15}[{C2}INIT{C15}] {C5}Calibrating Sensor: {C12}{s:<20}{RST}")
        sys.stdout.flush()
        time.sleep(0.3)
    print(f"\n{C7}[+] Biometric Perimeter Active. High-Value Access requires Physical Proof.{RST}\n")

# ==========================================
# ARCHITECTURE: BIOMETRIC TEMPLATE ENGINE
# ==========================================
class ChakriEngine:
    """Simulates biometric ridge-pattern mapping and secure template hashing."""
    def __init__(self):
        # Fingerprint Minutiae Points simulated as strings
        self.enrolled_templates = {
            "raj_g": hashlib.sha256(b"RIDGE_PATTERN_DELTA_7721").hexdigest(),
            "admin": hashlib.sha256(b"RIDGE_PATTERN_ARCH_9901").hexdigest()
        }

    def verify_biometric(self, user, raw_scan_data):
        """Processes raw scan, extracts minutiae, and compares hashes."""
        ts = datetime.now().strftime("%H:%M:%S")
        print(f"{C15}[{ts}] {C6}SCANNER: {C5}Processing fingerprint for {C1}{user}{C5}...{RST}")
        
        # Simulating ridge extraction delay
        for i in range(5):
            sys.stdout.write(f"\r    {C4}Mapping Points: {C2}{'#' * (i+1)}{'.' * (4-i)}{RST}")
            sys.stdout.flush()
            time.sleep(0.3)
        print(f" {C7}[OK]{RST}")

        # Hash the 'scanned' pattern
        scan_hash = hashlib.sha256(raw_scan_data.encode()).hexdigest()

        if user in self.enrolled_templates and self.enrolled_templates[user] == scan_hash:
            print(f"{C11}    [✔] Hash Match: {C12}{scan_hash[:16]}...{RST}")
            print(f"{C7}{BLD}    BIOMETRIC VALIDATED. ACCESS TO HIGH-VALUE CUI GRANTED.{RST}\n")
            return True
        else:
            self._trigger_biometric_lock(ts, user)
            return False

    def _trigger_biometric_lock(self, ts, user):
        print(f"\n{C8}{BLD}!!! CHAKRI-BIOMETRIC: BIOMETRIC MISMATCH / SPOOF DETECTED !!!{RST}")
        print(f"{C8}│ {C5}TIMESTAMP : {C10}{ts}{RST}")
        print(f"{C8}│ {C5}USER ID   : {C15}{user}{RST}")
        print(f"{C8}│ {C5}EVIDENCE  : {C8}{BLD}NON-REPRODUCIBLE PATTERN ERROR{RST}")
        print(f"{C8}│ {C5}ACTION    : {C8}{BLD}LOCKDOWN_LEVEL_5 | PHOTO_LOGGED | SECURITY_DISPATCH{RST}")
        print(f"{C8}└{'─'*55}{RST}\n")
        time.sleep(0.5)

# ==========================================
# SIMULATION: BIOMETRIC ACCESS FLOW
# ==========================================
if __name__ == "__main__":
    try:
        chakri_banner_anim()
        engine = ChakriEngine()
        
        # Traffic Simulation
        print(f"{C13}[!] REQUESTING BIOMETRIC PROOF FOR 'TOP_SECRET_VAULT'...{RST}\n")
        
        # Case 1: Raj Gautam - Correct Scan
        engine.verify_biometric("raj_g", "RIDGE_PATTERN_DELTA_7721")
        
        # Case 2: Spoof Attempt / Dirty Finger
        time.sleep(1)
        engine.verify_biometric("admin", "INVALID_SPOOF_PATTERN_001")

    except KeyboardInterrupt:
        print(f"\n{C8}[!] Scanner Offline.{RST}")