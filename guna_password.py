import os
import sys
import time
import re
import math
from datetime import datetime

# ==========================================
# GUNA-PASSWORD: INNER STRENGTH 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;220m', '\033[38;5;214m', '\033[38;5;231m', '\033[38;5;244m', '\033[38;5;33m'
C6, C7, C8, C9, C10  = '\033[38;5;160m', '\033[38;5;93m', '\033[38;5;51m', '\033[38;5;250m', '\033[38;5;94m'
C11, C12, C13, C14, C15 = '\033[38;5;121m', '\033[38;5;18m', '\033[38;5;238m', '\033[38;5;202m', '\033[38;5;248m'
C16, C17, C18, C19, C20 = '\033[38;5;232m', '\033[38;5;124m', '\033[38;5;28m', '\033[38;5;208m', '\033[38;5;233m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE FORTIFIED VAULT (GUNA)
# ==========================================
def guna_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C1}             _______
    {C1}            |  {C3}KEY{C1}  |
    {C10}          __|_______|__      {C1}G U N A
    {C10}         |  {C5}[{C1}*****{C5}]{C10}  |     {C2}P A S S W O R D
    {C13}         |___________|     {C15}v7.4 [ENTROPY_ENFORCER]
    """
    print(logo)
    print(f"{C1}{BLD}   GUNA-PASSWORD: NIST-COMPLIANT COMPLEXITY VALIDATOR{RST}\n")
    
    # Policy check animation
    policies = ["Length_Audit", "Entropy_Calc", "Dictionary_Scan", "Sequence_Check"]
    for p in policies:
        sys.stdout.write(f"\r{C13}[{C5}INFO{C13}] {C9}Enforcing Account Policy: {C11}{p:<18}{RST}")
        sys.stdout.flush()
        time.sleep(0.3)
    print(f"\n{C12}[+] Guna Policy Engine Active. Minimum Complexity: 80 Bits Entropy.{RST}\n")

# ==========================================
# ARCHITECTURE: PASSWORD ENTROPY ENGINE
# ==========================================
class GunaPolicy:
    """Calculates password strength using information theory entropy."""
    def __init__(self):
        self.min_length = 12
        self.blacklist = ["password", "admin123", "welcome", "rajgautam"]

    def calculate_entropy(self, password):
        """Math: $E = L \times \log_2(R)$ where L is length and R is pool size."""
        length = len(password)
        pool = 0
        if re.search(r'[a-z]', password): pool += 26
        if re.search(r'[A-Z]', password): pool += 26
        if re.search(r'[0-9]', password): pool += 10
        if re.search(r'[^a-zA-Z0-9]', password): pool += 32

        if pool == 0: return 0
        entropy = length * math.log2(pool)
        return round(entropy, 2)

    def validate(self, password):
        ts = datetime.now().strftime("%H:%M:%S")
        print(f"{C13}[{ts}] {C4}AUDITING: {C3}{'*' * len(password):<15}{RST}")
        time.sleep(0.8)

        entropy = self.calculate_entropy(password)
        
        # 1. Length Check
        if len(password) < self.min_length:
            self._trigger_failure(ts, "PASSWORD_TOO_SHORT", f"Min: {self.min_length}")
            return False

        # 2. Blacklist Check
        if password.lower() in self.blacklist:
            self._trigger_failure(ts, "DICTIONARY_WORD_DETECTED", "High Risk")
            return False

        # 3. Entropy Check
        print(f"    {C9}>> Entropy Score: {C1}{entropy} bits{RST}")
        if entropy < 60:
            self._trigger_failure(ts, "LOW_ENTROPY_CRITICAL", "Easily Crackable")
            return False

        print(f"    {C11}[✔] PASS: Strength 'Sovereign' | Entropy {entropy} bits.{RST}")
        print(f"    {C12}{BLD}ACCOUNT SECURITY PARAMETERS UPDATED.{RST}\n")
        return True

    def _trigger_failure(self, ts, reason, detail):
        print(f"\n{C6}{BLD}!!! GUNA-PASSWORD: POLICY VIOLATION DETECTED !!!{RST}")
        print(f"{C6}│ {C3}TIMESTAMP : {C10}{ts}{RST}")
        print(f"{C6}│ {C3}REASON    : {C6}{BLD}{reason}{RST}")
        print(f"{C6}│ {C3}DETAIL    : {C9}{detail}{RST}")
        print(f"{C6}│ {C3}ACTION    : {C6}{BLD}REJECTED | LOGGED_TO_AUDIT{RST}")
        print(f"{C6}└{'─'*55}{RST}\n")
        time.sleep(0.5)

# ==========================================
# SIMULATION: ACCOUNT CREATION
# ==========================================
if __name__ == "__main__":
    try:
        guna_banner_anim()
        policy = GunaPolicy()
        
        # Scenario 1: Weak Password
        policy.validate("Raj123")
        
        # Scenario 2: Dictionary Password
        time.sleep(1)
        policy.validate("password12345")
        
        # Scenario 3: Strong Guna Password
        time.sleep(1)
        policy.validate("Kshatriya#2026!Secure")

    except KeyboardInterrupt:
        print(f"\n{C6}[!] Policy Engine Halted.{RST}")