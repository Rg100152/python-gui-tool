import os
import sys
import time
import secrets
import hashlib
from datetime import datetime, timedelta

# ==========================================
# SATYA-SESSION: TEMPORAL GUARD 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;33m', '\033[38;5;252m', '\033[38;5;244m', '\033[38;5;51m', '\033[38;5;196m'
C6, C7, C8, C9, C10  = '\033[38;5;214m', '\033[38;5;46m', '\033[38;5;232m', '\033[38;5;231m', '\033[38;5;220m'
C11, C12, C13, C14, C15 = '\033[38;5;118m', '\033[38;5;93m', '\033[38;5;240m', '\033[38;5;202m', '\033[38;5;245m'
C16, C17, C18, C19, C20 = '\033[38;5;233m', '\033[38;5;160m', '\033[38;5;28m', '\033[38;5;215m', '\033[38;5;234m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE HOURGLASS (SATYA)
# ==========================================
def satya_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C10}             .====.
    {C2}            \\  {C1}.{C2}  /         {C1}S A T Y A
    {C1}             \\{C10}:{C1}/          {C4}S E S S I O N
    {C2}             / {C1}.{C2} \\          {C15}v7.9 [TIMEOUT_ENFORCER]
    {C10}            '===='
    {C13}          [{C6}TIME_FLIES{C13}]
    """
    print(logo)
    print(f"{C1}{BLD}   SATYA-SESSION: SECURE STATE MANAGEMENT & INACTIVITY REAPER{RST}\n")
    
    # Session lifecycle animation
    stages = ["ID_Generation", "TTL_Assignment", "Heartbeat_Monitor", "Auto_Eviction"]
    for s in stages:
        sys.stdout.write(f"\r{C15}[{C1}SYNC{C15}] {C9}Synchronizing Temporal State: {C11}{s:<18}{RST}")
        sys.stdout.flush()
        time.sleep(0.3)
    print(f"\n{C7}[+] Satya Watcher is active. Enforcing 5-second Idle Timeout (Demo Mode).{RST}\n")

# ==========================================
# ARCHITECTURE: SESSION MANAGEMENT ENGINE
# ==========================================
class SatyaSessionManager:
    """Simulates a secure session handler with timeout and rotation logic."""
    def __init__(self, idle_timeout_sec=5):
        self.sessions = {}
        self.idle_timeout = idle_timeout_sec

    def create_session(self, user):
        """Generates a high-entropy session ID and sets initial expiration."""
        session_id = secrets.token_urlsafe(32)
        expiry = datetime.now() + timedelta(seconds=self.idle_timeout)
        self.sessions[session_id] = {"user": user, "expiry": expiry}
        
        ts = datetime.now().strftime("%H:%M:%S")
        print(f"{C15}[{ts}] {C7}NEW_SESSION: {C10}{user}{RST} | ID: {C2}{session_id[:12]}...{RST}")
        return session_id

    def validate_access(self, session_id):
        """Checks if session is valid and updates sliding window."""
        ts = datetime.now().strftime("%H:%M:%S")
        
        if session_id not in self.sessions:
            self._trigger_session_alert(ts, "INVALID_OR_REVOKED_SESSION")
            return False

        session = self.sessions[session_id]
        if datetime.now() > session["expiry"]:
            self._trigger_session_alert(ts, f"SESSION_EXPIRED (User: {session['user']})")
            del self.sessions[session_id]
            return False

        # Sliding Window: Update expiry on every activity
        session["expiry"] = datetime.now() + timedelta(seconds=self.idle_timeout)
        print(f"{C15}[{ts}] {C11}ACTIVE: {C9}{session['user']}{RST} | Sliding Window Extended.{RST}")
        return True

    def _trigger_session_alert(self, ts, reason):
        print(f"\n{C5}{BLD}!!! SATYA-SESSION: TEMPORAL EXCLUSION TRIGGERED !!!{RST}")
        print(f"{C5}│ {C9}TIMESTAMP : {C10}{ts}{RST}")
        print(f"{C5}│ {C9}VIOLATION : {C5}{BLD}{reason}{RST}")
        print(f"{C5}│ {C9}ACTION    : {C5}{BLD}NULLIFYING_SESSION_STATE | REDIRECT_TO_AUTH{RST}")
        print(f"{C5}└{'─'*55}{RST}\n")
        time.sleep(0.5)

# ==========================================
# SIMULATION: ACTIVITY & TIMEOUT
# ==========================================
if __name__ == "__main__":
    try:
        # Initializing manager with 5-second timeout for demo
        satya_banner_anim()
        manager = SatyaSessionManager(idle_timeout_sec=5)
        
        # Step 1: User Logs In
        sid = manager.create_session("Raj_Gautam")
        time.sleep(2)

        # Step 2: User is active (Extends window)
        manager.validate_access(sid)
        time.sleep(2)

        # Step 3: User is still active
        manager.validate_access(sid)
        
        # Step 4: User goes Idle (Sleep for 6 seconds, exceeding 5s limit)
        print(f"\n{C13}[!] User {C10}Raj_Gautam{C13} is now idle (Walking away from desk...){RST}")
        time.sleep(6)

        # Step 5: Attempt access after timeout
        manager.validate_access(sid)

    except KeyboardInterrupt:
        print(f"\n{C5}[!] Time stands still. Session Manager Offline.{RST}")