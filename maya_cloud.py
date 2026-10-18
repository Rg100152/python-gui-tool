import os
import sys
import time
import secrets
from datetime import datetime

# ==========================================
# MAYA-CLOUD: CELESTIAL ILLUSION 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;33m', '\033[38;5;252m', '\033[38;5;93m', '\033[38;5;255m', '\033[38;5;244m'
C6, C7, C8, C9, C10  = '\033[38;5;226m', '\033[38;5;208m', '\033[38;5;232m', '\033[38;5;250m', '\033[38;5;51m'
C11, C12, C13, C14, C15 = '\033[38;5;201m', '\033[38;5;121m', '\033[38;5;18m', '\033[38;5;196m', '\033[38;5;60m'
C16, C17, C18, C19, C20 = '\033[38;5;46m', '\033[38;5;233m', '\033[38;5;27m', '\033[38;5;35m', '\033[38;5;235m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE CLOUD VORTEX (MAYA)
# ==========================================
def maya_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C10}             ______
    {C10}          _.(      )._
    {C1}        (             )
    {C1}      (      {C4}MAYA{C1}       )
    {C3}     (      {C4}CLOUD{C3}       )
    {C3}       '-(__________)-'
    {C13}    [ CLOUD EGRESS GUARD v4.8 ]
    """
    print(logo)
    print(f"{C10}{BLD}   MAYA-CLOUD: CLOUD STORAGE & API UPLOAD BLOCKING{RST}\n")
    
    # Interception pulse
    for i in range(12):
        sys.stdout.write(f"\r{C5}[{C6}LOCK{C5}] {C4}Filtering Egress API Calls... {C1}{'|/-\\'[i%4]}{RST}")
        sys.stdout.flush()
        time.sleep(0.1)
    print(f"\n{C16}[+] Proxy-Chain Active. External Storage Domains Blacklisted.{RST}\n")

# ==========================================
# ARCHITECTURE: CLOUD EGRESS FILTER
# ==========================================
class CloudSentry:
    """Monitors and prevents data uploads to unauthorized external services."""
    def __init__(self):
        self.blacklist = [
            "drive.google.com", "dropbox.com", "mega.nz", 
            "wetransfer.com", "mediafire.com", "icloud.com",
            "api.onedrive.com", "s3.amazonaws.com"
        ]

    def monitor_network_request(self, domain, method, payload_size):
        """Analyzes HTTP/HTTPS requests for exfiltration patterns."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        is_blocked = any(d in domain.lower() for d in self.blacklist)
        
        # Color coding based on status
        status_color = C14 if is_blocked else C16
        verdict = f"{C14}{BLD}BLOCKED{RST}" if is_blocked else f"{C16}ALLOWED{RST}"
        
        print(f"{C5}[{C2}{timestamp}{C5}] {C10}{method:<4} {C4}{domain:<22} {C5}| {C2}SIZE: {payload_size:<8} {C5}| {verdict}")

        if is_blocked:
            self._trigger_kill_switch(domain, method)

    def _trigger_kill_switch(self, domain, method):
        """Simulates cutting the connection to the cloud service."""
        print(f"\n{C14}{BLD}!!! MAYA-CLOUD: UNAUTHORIZED UPLOAD INTERCEPTED !!!{RST}")
        print(f"{C14}│ {C4}TARGET   : {C1}{domain}{RST}")
        print(f"{C14}│ {C4}METHOD   : {C14}{method} (DATA_PUSH){RST}")
        print(f"{C14}│ {C4}PROTOCOL : {C10}TLS/SSL Handshake Terminated{RST}")
        print(f"{C14}│ {C4}ACTION   : {C14}{BLD}RESET_PACKET SENT | API CALL NEUTRALIZED{RST}")
        print(f"{C14}└{'─'*55}{RST}\n")
        time.sleep(0.5)

# ==========================================
# SIMULATION: NETWORK TRAFFIC FLOW
# ==========================================
def run_traffic_monitor():
    maya_banner_anim()
    sentry = CloudSentry()
    
    # Simulated Traffic Log
    traffic = [
        ("vbsppu.edu.in", "GET", "4.2 KB"),
        ("drive.google.com", "POST", "125.8 MB"), # Violation
        ("github.com", "PUSH", "15.0 KB"),
        ("mega.nz", "PUT", "2.1 GB"),            # Violation
        ("stackoverflow.com", "GET", "22.1 KB"),
        ("api.onedrive.com", "POST", "450.0 MB")  # Violation
    ]
    
    print(f"{C13}[!] SNIFFING OUTBOUND CLOUD TRAFFIC...{RST}\n")
    
    for domain, method, size in traffic:
        time.sleep(1.5) # Simulate time between requests
        sentry.monitor_network_request(domain, method, size)

if __name__ == "__main__":
    try:
        run_traffic_monitor()
        print(f"{C16}[✔] Maya-Cloud Monitoring Stabilized. Cloud Shield Active.{RST}")
    except KeyboardInterrupt:
        print(f"\n{C14}[!] Proxy Offline.{RST}")