import os
import sys
import time
import base64
import hashlib
from datetime import datetime

# ==========================================
# KOSHA-VAULT: TREASURE KEEPER 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;220m', '\033[38;5;242m', '\033[38;5;93m', '\033[38;5;51m', '\033[38;5;246m'
C6, C7, C8, C9, C10  = '\033[38;5;160m', '\033[38;5;28m', '\033[38;5;214m', '\033[38;5;33m', '\033[38;5;180m'
C11, C12, C13, C14, C15 = '\033[38;5;231m', '\033[38;5;235m', '\033[38;5;136m', '\033[38;5;202m', '\033[38;5;240m'
C16, C17, C18, C19, C20 = '\033[38;5;232m', '\033[38;5;124m', '\033[38;5;35m', '\033[38;5;208m', '\033[38;5;233m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE IMPENETRABLE CHEST (KOSHA)
# ==========================================
def kosha_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C2}             __________
    {C2}            /         /|
    {C1}           /________ / |     {C1}K O S H A
    {C2}          |   {C8}[{C1}@{C8}]{C2}   | |     {C13}V A U L T
    {C13}          | {C1}SECRET{C13}   | /     {C15}v7.6 [AES_256_STORAGE]
    {C13}          |_________|/
    """
    print(logo)
    print(f"{C1}{BLD}   KOSHA-VAULT: SECURE PROGRAMMATIC SECRET MANAGEMENT{RST}\n")
    
    # Initialization animation
    tasks = ["Entropy_Harvesting", "Key_Derivation", "Memory_Lockdown", "Integrity_Check"]
    for t in tasks:
        sys.stdout.write(f"\r{C15}[{C1}SAFE{C15}] {C9}Sealing Vault Chambers: {C4}{t:<20}{RST}")
        sys.stdout.flush()
        time.sleep(0.3)
    print(f"\n{C7}[+] Vault Unsealed. Secrets are accessible in-memory only.{RST}\n")

# ==========================================
# ARCHITECTURE: SECRET STORAGE ENGINE
# ==========================================
class KoshaVault:
    """Simulates a secure credential store with encryption logic."""
    def __init__(self, master_pass):
        # Deriving a 'Storage Key' from Master Password
        self.master_key = hashlib.sha256(master_pass.encode()).hexdigest()
        self.secret_store = {}

    def add_secret(self, key_name, value):
        """Encrypts and stores a secret."""
        ts = datetime.now().strftime("%H:%M:%S")
        print(f"{C15}[{ts}] {C9}ENCRYPTING: {C1}{key_name:<15}{RST}...", end="")
        
        # Simulating AES encryption (Base64 + XOR for demo)
        encrypted_val = base64.b64encode(value.encode()).decode()
        self.secret_store[key_name] = encrypted_val
        
        time.sleep(0.6)
        print(f" {C7}[SECURED]{RST}")

    def retrieve_secret(self, key_name, provided_pass):
        """Verifies master key and decrypts secret."""
        ts = datetime.now().strftime("%H:%M:%S")
        provided_key = hashlib.sha256(provided_pass.encode()).hexdigest()

        if provided_key != self.master_key:
            self._trigger_vault_alert(ts, key_name, "INVALID_MASTER_KEY")
            return None

        if key_name in self.secret_store:
            raw_b64 = self.secret_store[key_name]
            decrypted = base64.b64decode(raw_b64).decode()
            print(f"{C15}[{ts}] {C11}RETRIEVAL: {C1}{key_name:<15}{RST} >> {C8}{decrypted}{RST}")
            return decrypted
        
        print(f"{C6}[!] Secret not found.{RST}")
        return None

    def _trigger_vault_alert(self, ts, target, reason):
        print(f"\n{C6}{BLD}!!! KOSHA-VAULT: UNAUTHORIZED ACCESS ATTEMPT !!!{RST}")
        print(f"{C6}│ {C11}TIMESTAMP : {C10}{ts}{RST}")
        print(f"{C6}│ {C11}TARGET    : {C1}{target}{RST}")
        print(f"{C6}│ {C11}VIOLATION : {C6}{BLD}{reason}{RST}")
        print(f"{C6}│ {C11}ACTION    : {C6}{BLD}VAULT_LOCKDOWN | SELF_DESTRUCT_PENDING{RST}")
        print(f"{C6}└{'─'*55}{RST}\n")
        time.sleep(0.5)

# ==========================================
# SIMULATION: SECRET LIFECYCLE
# ==========================================
if __name__ == "__main__":
    try:
        # Step 1: Initialize Vault with Master Password
        MASTER_PWD = "Raj#Kshatriya2026"
        kosha_banner_anim()
        vault = KoshaVault(MASTER_PWD)
        
        # Step 2: Store sensitive CUI kets
        vault.add_secret("DB_PASSWORD", "SuperSecureSQL#99")
        vault.add_secret("AWS_API_KEY", "AKIA-RAJ-GAUTAM-PRV")
        vault.add_secret("SSH_PASSPHRASE", "VBSPU_Admin_Key")
        print("")

        # Step 3: Legitimate Retrieval
        vault.retrieve_secret("DB_PASSWORD", MASTER_PWD)
        
        # Step 4: Malicious Retrieval (Wrong Password)
        time.sleep(1)
        vault.retrieve_secret("AWS_API_KEY", "wrong_password_123")

    except KeyboardInterrupt:
        print(f"\n{C6}[!] Vault purged from memory.{RST}")