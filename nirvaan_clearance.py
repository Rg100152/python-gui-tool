import os
import time
import sys
import hashlib
from datetime import datetime

# ==========================================
# NIRVAAN-CLEARANCE: CYBER-NEON LEDGER THEME
# (5 Unique Non-Repeating Colors + Formatting)
# ==========================================
EBLUE = '\033[38;5;39m'   # Electric Blue
PINK  = '\033[38;5;198m'  # Neon Pink
LIME  = '\033[38;5;154m'  # Lime Green
CRIM  = '\033[38;5;196m'  # Deep Crimson
ORNG  = '\033[38;5;214m'  # Bright Orange
RST   = '\033[0m'         # Reset
BLD   = '\033[1m'         # Bold (FIXED: Error was missing this)

# ==========================================
# ARCHITECTURE: IMMUTABLE EVENT SOURCING
# ==========================================

class ClearanceEventBlock:
    """A single immutable event in the clearance ledger."""
    def __init__(self, index, timestamp, user_id, action, level, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.user_id = user_id
        self.action = action  # e.g., GRANTED, SUSPENDED, REVOKED
        self.level = level    # e.g., SECRET, TOP_SECRET, NONE
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """Generates a SHA-256 hash mathematically locking the data."""
        block_data = f"{self.index}{self.timestamp}{self.user_id}{self.action}{self.level}{self.previous_hash}"
        return hashlib.sha256(block_data.encode('utf-8')).hexdigest()

class NirvaanLedger:
    """The central cryptographic chain that tracks all status changes."""
    def __init__(self):
        self.chain = [self._create_genesis_block()]

    def _create_genesis_block(self):
        """The foundation of the ledger."""
        return ClearanceEventBlock(0, "0000-00-00 00:00:00", "SYSTEM", "GENESIS", "NONE", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def record_event(self, user_id, action, level):
        """Adds a new cryptographically secured event to the chain."""
        prev_block = self.get_latest_block()
        new_block = ClearanceEventBlock(
            index=prev_block.index + 1,
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            user_id=user_id.upper(),
            action=action.upper(),
            level=level.upper(),
            previous_hash=prev_block.hash
        )
        self.chain.append(new_block)
        return new_block.hash

    def verify_ledger_integrity(self):
        """Audits the entire chain. If a database admin tampered with data, this catches it."""
        print(f"\n{PINK}[*] INITIATING DEEP CRYPTOGRAPHIC AUDIT...{RST}")
        time.sleep(0.5)
        
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            sys.stdout.write(f"{EBLUE} Verifying Block [{current_block.index}] for {current_block.user_id}... {RST}")
            sys.stdout.flush()
            time.sleep(0.3)

            # Check 1: Has the data inside the block been changed?
            if current_block.hash != current_block.calculate_hash():
                print(f"{CRIM}[ FAIL ]{RST}")
                print(f"{CRIM}[!] CRITICAL BREACH: Data tampering detected at Block {current_block.index}!{RST}")
                return False
            
            # Check 2: Has the link to the previous block been broken?
            if current_block.previous_hash != previous_block.hash:
                print(f"{CRIM}[ FAIL ]{RST}")
                print(f"{CRIM}[!] CRITICAL BREACH: Chain continuity broken at Block {current_block.index}!{RST}")
                return False
                
            print(f"{LIME}[ OK ]{RST}")

        print(f"{LIME}[+] LEDGER INTEGRITY VERIFIED: 100% SECURE.{RST}\n")
        return True

    def get_current_status(self, user_id):
        """Event Sourcing: Replays history to find current true state."""
        current_status = "UNKNOWN"
        current_level = "NONE"
        
        for block in self.chain:
            if block.user_id == user_id.upper():
                current_status = block.action
                current_level = block.level
                
        return current_status, current_level

# ==========================================
# SYSTEM INTERFACE & AESTHETICS
# ==========================================

ledger = NirvaanLedger()

def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = f"""{EBLUE}{BLD}
     _   _  ___  ____ __     __ ___     ___   _   _ 
    | \ | ||_ _| |  _ \\\ \   / // \ \   / \ \ | \ | |
    |  \| | | |  | |_) |\ \ / // _ \ \ / / \ \|  \| |
    | |\  | | |  |  _ <  \ V // ___ \ V /   _ \ |\  |
    |_| \_||___| |_| \_\  \_//_/   \_\_/   /_/ \_| \_|
    {PINK}C L E A R A N C E   V A L I D A T I O N   L E D G E R{RST}
    """
    print(banner)
    print(f"{EBLUE}>> ARCHITECTURE: EVENT SOURCING & CRYPTOGRAPHIC LEDGER{RST}")
    print(f"{EBLUE}>> PROTECTION: ZERO-TRUST INSIDER THREAT MITIGATION{RST}\n")

def cmd_help():
    print(f"\n{PINK}{BLD}--- NIRVAAN COMMANDS ---{RST}")
    print(f" {EBLUE}grant <user> <level>{RST}   : Issue or upgrade clearance (e.g., grant Raj SECRET)")
    print(f" {EBLUE}revoke <user>{RST}          : Permanently revoke clearance")
    print(f" {EBLUE}status <user>{RST}          : Replay events to find current clearance status")
    print(f" {EBLUE}audit{RST}                  : Run full cryptographic verification of the ledger")
    print(f" {CRIM}tamper <user> <level>{RST}  : [DEV ONLY] Simulate a DB hack to test the audit")
    print(f" {EBLUE}exit{RST}                   : Disconnect")
    print(f"{PINK}{'-'*24}{RST}")

def run_terminal():
    print_banner()
    
    # Pre-seed some real-world data
    ledger.record_event("RAJ", "GRANTED", "TOP_SECRET")
    ledger.record_event("SHANI", "GRANTED", "CONFIDENTIAL")
    ledger.record_event("SHANI", "SUSPENDED", "NONE")
    
    while True:
        try:
            raw = input(f"{PINK}nirvaan{RST}@{EBLUE}ledger{RST}:{PINK}~/validate{RST}# ").strip().split()
            if not raw: continue
            
            cmd = raw[0].lower()
            args = raw[1:]

            if cmd == "help":
                cmd_help()
                
            elif cmd == "grant":
                if len(args) < 2: print(f"{CRIM}[!] Usage: grant <user> <level>{RST}"); continue
                h = ledger.record_event(args[0], "GRANTED", args[1])
                print(f"{LIME}[+] Block appended. TX Hash: {PINK}{h[:16]}...{RST}")
                
            elif cmd == "revoke":
                if len(args) < 1: print(f"{CRIM}[!] Usage: revoke <user>{RST}"); continue
                h = ledger.record_event(args[0], "REVOKED", "NONE")
                print(f"{CRIM}[-] Clearance revoked. TX Hash: {PINK}{h[:16]}...{RST}")
                
            elif cmd == "status":
                if len(args) < 1: print(f"{CRIM}[!] Usage: status <user>{RST}"); continue
                status, lvl = ledger.get_current_status(args[0])
                c = LIME if status == "GRANTED" else (CRIM if status == "REVOKED" else ORNG)
                print(f"\n{EBLUE}IDENTITY:{RST} {args[0].upper()}")
                print(f"{EBLUE}STATUS:  {RST} {c}{status}{RST}")
                print(f"{EBLUE}LEVEL:   {RST} {PINK}{lvl}{RST}\n")
                
            elif cmd == "audit":
                ledger.verify_ledger_integrity()
                
            elif cmd == "tamper":
                if len(args) < 2: print(f"{CRIM}[!] Usage: tamper <user> <new_fake_level>{RST}"); continue
                # Simulate a DB Admin altering an old record without rehashing
                for block in ledger.chain:
                    if block.user_id == args[0].upper() and block.action != "GENESIS":
                        block.level = args[1].upper() # ILLEGAL MODIFICATION
                        print(f"{CRIM}[!] SECURITY BYPASS: Silently altered DB record for {block.user_id} to {block.level}{RST}")
                        print(f"{CRIM}[!] Run 'audit' to see if the system catches this fraud.{RST}")
                        break
                        
            elif cmd == "exit":
                print(f"{PINK}[*] Ledger connection terminated.{RST}")
                break
            else:
                print(f"{CRIM}[!] Unknown command. Type 'help'.{RST}")
                
        except Exception as e:
            print(f"{CRIM}[!] System Error: {e}{RST}")

if __name__ == "__main__":
    run_terminal()