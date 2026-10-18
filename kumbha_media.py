import os
import sys
import time
import secrets
from datetime import datetime

# ==========================================
# KUMBHA-MEDIA: THE SACRED VESSEL 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;214m', '\033[38;5;160m', '\033[38;5;94m', '\033[38;5;33m', '\033[38;5;180m'
C6, C7, C8, C9, C10  = '\033[38;5;34m', '\033[38;5;221m', '\033[38;5;202m', '\033[38;5;19m', '\033[38;5;250m'
C11, C12, C13, C14, C15 = '\033[38;5;30m', '\033[38;5;121m', '\033[38;5;18m', '\033[38;5;196m', '\033[38;5;242m'
C16, C17, C18, C19, C20 = '\033[38;5;232m', '\033[38;5;161m', '\033[38;5;170m', '\033[38;5;214m', '\033[38;5;233m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE SACRED KUMBHA (POT)
# ==========================================
def kumbha_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C1}             _____
    {C1}            (_____)
    {C3}         .-'       '-.
    {C3}        /           \\
    {C7}       |   {C1}KUMBHA{C7}    |
    {C7}       |   {C1}MEDIA {C7}    |
    {C3}        \           /
    {C15}         '-_______-'
    {C13}    [ MEDIA LIFECYCLE MONITOR v5.0 ]
    """
    print(logo)
    print(f"{C1}{BLD}   KUMBHA-MEDIA: SERIALIZED REMOVABLE STORAGE CONTROL{RST}\n")
    
    # Media synchronization animation
    for i in range(12):
        sys.stdout.write(f"\r{C15}[{C6}WAIT{C15}] {C10}Initializing Media Serialization Engine... {C1}{'|/-\\'[i%4]}{RST}")
        sys.stdout.flush()
        time.sleep(0.1)
    print(f"\n{C6}[+] Device-ID Whitelist Loaded. Real-time Block Analysis Active.{RST}\n")

# ==========================================
# ARCHITECTURE: MEDIA ACCESS CONTROL ENGINE
# ==========================================
class KumbhaSentry:
    """Manages the lifecycle of removable media devices."""
    def __init__(self):
        self.authorized_serials = ["WD-7892X", "SN-4411Z", "KNG-001A"]
        self.active_sessions = {}

    def analyze_mount(self, device_name, serial, capacity):
        """Validates and registers a new media device."""
        ts = datetime.now().strftime("%H:%M:%S")
        print(f"{C15}[{ts}] {C4}HARDWARE_INT: {C8}Device '{device_name}' detected on Port 2.{RST}")
        time.sleep(1)

        if serial in self.authorized_serials:
            session_key = secrets.token_hex(4).upper()
            self.active_sessions[serial] = {"key": session_key, "files": []}
            self._approve_mount(serial, session_key, capacity)
            return True
        else:
            self._reject_mount(device_name, serial)
            return False

    def track_file_transfer(self, serial, filename, size, action):
        """Logs every file operation on the removable media."""
        if serial not in self.active_sessions: return
        
        ts = datetime.now().strftime("%H:%M:%S")
        is_violation = "CUI" in filename.upper() and action == "WRITE"
        
        color = C14 if is_violation else C6
        print(f"{C15}[{ts}] {C10}SESSION:{C1}{self.active_sessions[serial]['key']}{RST} | {C5}{action:<6}{RST} | FILE: {C18}{filename:<20}{RST} | {color}STATUS: {('FLAGGED' if is_violation else 'OK')}{RST}")
        
        if is_violation:
            self._trigger_block(serial, filename)

    def _approve_mount(self, serial, key, cap):
        print(f"{C6}{BLD}✔ MOUNT GRANTED: Authorized Media (SN: {serial}){RST}")
        print(f"{C11}│ SESSION_ID: {C1}{key}{RST} | CAPACITY: {C10}{cap}{RST}")
        print(f"{C11}└─────────────────────────────────────────────────────┘{RST}\n")

    def _reject_mount(self, name, serial):
        print(f"{C2}{BLD}!!! ACCESS DENIED: UNREGISTERED MEDIA (SN: {serial}) !!!{RST}")
        print(f"{C2}│ {C5}DEVICE : {C10}{name}{RST}")
        print(f"{C2}│ {C5}ACTION : {C2}{BLD}I/O_LEVEL_BLOCK | PORT_DISABLED{RST}")
        print(f"{C2}└─────────────────────────────────────────────────────┘{RST}\n")

    def _trigger_block(self, serial, file):
        print(f"\n{C14}{BLD}!!! SECURITY BREACH: CUI EXFILTRATION ATTEMPT !!!{RST}")
        print(f"{C14}│ {C10}FILE   : {C18}{file}{RST}")
        print(f"{C14}│ {C10}MEDIA  : {C1}SERIAL_{serial}{RST}")
        print(f"{C14}│ {C10}ACTION : {C14}{BLD}WRITE_INTERRUPT | BUFFER_PURGED | SESSION_REVOKED{RST}")
        print(f"{C14}└─────────────────────────────────────────────────────┘{RST}\n")
        time.sleep(1)

# ==========================================
# SIMULATION: MEDIA USAGE LIFECYCLE
# ==========================================
def run_media_simulation():
    kumbha_banner_anim()
    sentry = KumbhaSentry()
    
    # 1. Authorized Device Insertion
    if sentry.analyze_mount("Secure_Drive_X1", "SN-4411Z", "64 GB"):
        time.sleep(1.5)
        sentry.track_file_transfer("SN-4411Z", "Presentation.pptx", "12 MB", "WRITE")
        time.sleep(1)
        sentry.track_file_transfer("SN-4411Z", "CUI_Nuclear_Draft.pdf", "4.5 MB", "WRITE") # VIOLATION

    # 2. Unauthorized Device Insertion
    time.sleep(2)
    sentry.analyze_mount("Generic_Flash", "UNK-12345", "128 GB")

if __name__ == "__main__":
    try:
        run_media_simulation()
        print(f"{C1}{BLD}Project 50/50 Complete. CUI Ecosystem Lifecycle Fully Secured.{RST}")
    except KeyboardInterrupt:
        print(f"\n{C2}[!] Media Watchdog Offline.{RST}")