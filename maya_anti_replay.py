import os
import sys
import time
import secrets
import hashlib
from datetime import datetime

# ==========================================
# MAYA-ANTI-REPLAY: ILLUSION & TIME 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;63m', '\033[38;5;244m', '\033[38;5;226m', '\033[38;5;51m', '\033[38;5;196m'
C6, C7, C8, C9, C10  = '\033[38;5;46m', '\033[38;5;129m', '\033[38;5;232m', '\033[38;5;231m', '\033[38;5;220m'
C11, C12, C13, C14, C15 = '\033[38;5;198m', '\033[38;5;27m', '\033[38;5;238m', '\033[38;5;202m', '\033[38;5;242m'
C16, C17, C18, C19, C20 = '\033[38;5;232m', '\033[38;5;160m', '\033[38;5;28m', '\033[38;5;214m', '\033[38;5;233m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE INFINITE KNOT (MAYA)
# ==========================================
def maya_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C1}             .____.
    {C7}            /  /\  \\         {C1}M A Y A
    {C1}           |  {C10}(  ){C1}  |        {C4}A N T I - R E P L A Y
    {C7}            \\  \/  /         {C15}v8.0 [NONCE_VALIDATOR]
    {C1}             '----'
    {C13}          [{C3}NONCE_SYNCED{C13}]
    """
    print(logo)
    print(f"{C1}{BLD}   MAYA-ANTI-REPLAY: CRYPTOGRAPHIC TRANSACTION FRESHNESS{RST}\n")
    
    # Handshake synchronization
    steps = ["Seed_Exchange", "Timestamp_Windowing", "Nonce_Registry_Init", "Signature_Bind"]
    for s in steps:
        sys.stdout.write(f"\r{C15}[{C1}VEIL{C15}] {C9}Creating Temporal Illusion: {C3}{s:<20}{RST}")
        sys.stdout.flush()
        time.sleep(0.3)
    print(f"\n{C6}[+] Maya Guard is active. Stale requests will be dissolved in the void.{RST}\n")

# ==========================================
# ARCHITECTURE: ANTI-REPLAY ENGINE
# ==========================================
class MayaEngine:
    """Simulates a replay-prevention mechanism using Nonces and Timestamps."""
    def __init__(self):
        self.used_nonces = set()
        self.time_window = 10 # 10 seconds validity window

    def generate_request(self, user, action):
        """Client-side: Creates a fresh request with Nonce and Timestamp."""
        nonce = secrets.token_hex(8)
        timestamp = int(time.time())
        # Signature: Hash(User + Action + Nonce + Timestamp)
        payload = f"{user}|{action}|{nonce}|{timestamp}"
        signature = hashlib.sha256(payload.encode()).hexdigest()[:16]
        return {"user": user, "action": action, "nonce": nonce, "ts": timestamp, "sig": signature}

    def process_request(self, req):
        """Server-side: Validates freshness and uniqueness."""
        curr_ts = int(time.time())
        ts = datetime.now().strftime("%H:%M:%S")
        print(f"{C15}[{ts}] {C4}INCOMING: {C1}{req['user']}{RST} -> {C10}{req['action']}{RST}")
        time.sleep(0.8)

        # 1. Integrity Check (Signature)
        re_sig = hashlib.sha256(f"{req['user']}|{req['action']}|{req['nonce']}|{req['ts']}".encode()).hexdigest()[:16]
        if req['sig'] != re_sig:
            self._trigger_maya_alert(ts, "SIGNATURE_TAMPERED")
            return False

        # 2. Freshness Check (Timestamp Window)
        if abs(curr_ts - req['ts']) > self.time_window:
            self._trigger_maya_alert(ts, "TIMESTAMP_EXPIRED (Stale Request)")
            return False

        # 3. Uniqueness Check (Nonce Replay)
        if req['nonce'] in self.used_nonces:
            self._trigger_maya_alert(ts, "REPLAY_ATTACK_DETECTED (Nonce Reused)")
            return False

        # If all checks pass
        self.used_nonces.add(req['nonce'])
        print(f"    {C6}[✔] REQUEST VALIDATED. Action executed successfully.{RST}\n")
        return True

    def _trigger_maya_alert(self, ts, reason):
        print(f"\n{C5}{BLD}!!! MAYA-ANTI-REPLAY: SECURITY ILLUSION BROKEN !!!{RST}")
        print(f"{C5}│ {C9}TIMESTAMP : {C10}{ts}{RST}")
        print(f"{C5}│ {C9}VIOLATION : {C5}{BLD}{reason}{RST}")
        print(f"{C5}│ {C9}ACTION    : {C5}{BLD}NULLIFYING_REQUEST | BLACKLISTING_REMOTE_IP{RST}")
        print(f"{C5}└{'─'*55}{RST}\n")
        time.sleep(0.5)

# ==========================================
# SIMULATION: REPLAY ATTACK SCENARIO
# ==========================================
if __name__ == "__main__":
    try:
        maya = MayaEngine()
        maya_banner_anim()
        
        # Step 1: Legitimate User Request
        print(f"{C13}[!] Generating legitimate request...{RST}")
        valid_req = maya.generate_request("Raj_Gautam", "ACCESS_CUI_VAULT")
        maya.process_request(valid_req)
        
        # Step 2: Hacker intercepts and REPLAYS the same request
        time.sleep(2)
        print(f"{C13}[!] Hacker replaying the captured request...{RST}")
        maya.process_request(valid_req) # REPLAY ATTEMPT
        
        # Step 3: Stale Request Simulation (Old Timestamp)
        time.sleep(1)
        print(f"{C13}[!] Simulating a stale/old request...{RST}")
        stale_req = maya.generate_request("Admin", "DELETE_LOGS")
        stale_req['ts'] -= 30 # Making it 30 seconds old
        maya.process_request(stale_req)

    except KeyboardInterrupt:
        print(f"\n{C5}[!] Maya Veil Dissolved.{RST}")