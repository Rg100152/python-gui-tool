import os
import sys
import time
import random
import hmac
import hashlib
import struct
from datetime import datetime

# ==========================================
# DVIJA-MFA: REBIRTH & PURITY 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;231m', '\033[38;5;220m', '\033[38;5;208m', '\033[38;5;211m', '\033[38;5;160m'
C6, C7, C8, C9, C10  = '\033[38;5;33m', '\033[38;5;51m', '\033[38;5;226m', '\033[38;5;248m', '\033[38;5;254m'
C11, C12, C13, C14, C15 = '\033[38;5;34m', '\033[38;5;121m', '\033[38;5;94m', '\033[38;5;202m', '\033[38;5;244m'
C16, C17, C18, C19, C20 = '\033[38;5;234m', '\033[38;5;160m', '\033[38;5;35m', '\033[38;5;214m', '\033[38;5;233m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE TWICE-BORN KEY (DVIJA)
# ==========================================
def dvija_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C2}             __{C1}O{C2}__
    {C2}            /      \\          {C1}D V I J A
    {C3}           |  {C1}1234{C3}  |         {C2}M F A
    {C3}           |________|         {C15}v7.1 [TOTP_ENFORCER]
    {C10}            |      |
    {C10}            |______|
    """
    print(logo)
    print(f"{C2}{BLD}   DVIJA-MFA: IDENTITY PURIFICATION & SECOND-FACTOR VALIDATION{RST}\n")
    
    # Handshake animation
    layers = ["Primary_Auth", "TOTP_Sync", "Channel_Verification", "Biometric_Sim"]
    for layer in layers:
        sys.stdout.write(f"\r{C15}[{C2}INIT{C15}] {C1}Strengthening Gateway: {C6}{layer:<20}{RST}")
        sys.stdout.flush()
        time.sleep(0.3)
    print(f"\n{C11}[+] MFA Layer 2 Engaged. Accessing CUI now requires Dual-Validation.{RST}\n")

# ==========================================
# ARCHITECTURE: TOTP ALGORITHM SIMULATION
# ==========================================
class DvijaMFA:
    """Simulates a Multi-Factor Authentication engine using TOTP logic."""
    def __init__(self):
        self.secret = b"RAJ_GAUTAM_SECURE_KEY_2026"
        self.users = {"raj_g": "Pass@123", "admin": "SecureAdmin!"}

    def generate_totp(self):
        """Generates a pseudo-TOTP based on current time slices."""
        interval = int(time.time()) // 30
        msg = struct.pack(">Q", interval)
        hmac_hash = hmac.new(self.secret, msg, hashlib.sha1).digest()
        offset = hmac_hash[-1] & 0x0F
        code = (struct.unpack(">I", hmac_hash[offset:offset+4])[0] & 0x7FFFFFFF) % 1000000
        return f"{code:06d}"

    def authenticate_access(self, username, password):
        ts = datetime.now().strftime("%H:%M:%S")
        print(f"{C15}[{ts}] {C10}PRIMARY AUTH: {C3}Verifying credentials for {username}...{RST}")
        time.sleep(1)

        # Step 1: Check Password
        if username in self.users and self.users[username] == password:
            print(f"{C11}    [✔] Password Accepted. {C2}Awaiting Second Factor...{RST}")
            
            # Step 2: Request MFA Code
            expected_otp = self.generate_totp()
            print(f"{C3}    [!] MFA Challenge: {C1}Enter 6-digit TOTP from your 'Dvija' App.{RST}")
            
            # Simulation: Auto-entering correct/incorrect code for demo
            user_otp = expected_otp if random.random() > 0.2 else "000000"
            time.sleep(1.5)
            
            if user_otp == expected_otp:
                print(f"{C11}    [✔] MFA Code {user_otp} Verified. {C1}Identity Re-born.{RST}")
                print(f"{C7}{BLD}    ACCESS GRANTED TO CUI INVENTORY.{RST}\n")
                return True
            else:
                self._trigger_auth_failure(ts, username, "MFA_CODE_MISMATCH")
                return False
        else:
            self._trigger_auth_failure(ts, username, "PRIMARY_CREDENTIALS_INVALID")
            return False

    def _trigger_auth_failure(self, ts, user, reason):
        print(f"\n{C5}{BLD}!!! DVIJA-MFA: AUTHENTICATION PURITY VIOLATION !!!{RST}")
        print(f"{C5}│ {C1}TIMESTAMP : {C10}{ts}{RST}")
        print(f"{C5}│ {C1}IDENTITY  : {C15}{user}{RST}")
        print(f"{C5}│ {C1}REASON    : {C5}{BLD}{reason}{RST}")
        print(f"{C5}│ {C1}ACTION    : {C5}{BLD}ACCESS_DENIED | IP_LOGGED | ACCOUNT_THROTTLED{RST}")
        print(f"{C5}└{'─'*55}{RST}\n")
        time.sleep(0.5)

# ==========================================
# SIMULATION: ACCESS ATTEMPTS
# ==========================================
if __name__ == "__main__":
    try:
        dvija_banner_anim()
        mfa_system = DvijaMFA()
        
        # Test Cases
        print(f"{C13}[!] MONITORING ACCESS REQUESTS FOR CUI_VAULT_01...{RST}\n")
        
        # Scenario 1: Correct Password, Correct MFA
        mfa_system.authenticate_access("raj_g", "Pass@123")
        
        # Scenario 2: Correct Password, Incorrect MFA (Theft Simulation)
        mfa_system.authenticate_access("admin", "SecureAdmin!")
        
        # Scenario 3: Incorrect Password
        mfa_system.authenticate_access("intruder", "password")

    except KeyboardInterrupt:
        print(f"\n{C5}[!] Dvija-MFA Service Offline.{RST}")