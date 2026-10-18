import os
import sys
import time
import secrets
import hashlib
from datetime import datetime

# ==========================================
# PRITHVI-INCIDENT: TERRA-FIRMAMENT 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;94m', '\033[38;5;124m', '\033[38;5;22m', '\033[38;5;107m', '\033[38;5;130m'
C6, C7, C8, C9, C10  = '\033[38;5;242m', '\033[38;5;26m', '\033[38;5;117m', '\033[38;5;214m', '\033[38;5;70m'
C11, C12, C13, C14, C15 = '\033[38;5;205m', '\033[38;5;52m', '\033[38;5;118m', '\033[38;5;196m', '\033[38;5;245m'
C16, C17, C18, C19, C20 = '\033[38;5;255m', '\033[38;5;234m', '\033[38;5;215m', '\033[38;5;28m', '\033[38;5;58m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE PROTECTIVE SPHERE (PRITHVI)
# ==========================================
def prithvi_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C3}          .  .  .
    {C3}        .        .
    {C7}       .    {C10}P R I{C7}    .
    {C7}      .    {C10}T H V I{C7}    .
    {C3}       .    {C10}4 0{C3}      .
    {C3}        .        .
    {C1}          '  '  '
    """
    print(logo)
    print(f"{C3}{BLD}   PRITHVI-INCIDENT v4.0: CUI EXPOSURE FORENSICS{RST}\n")
    
    # Forensic stabilization animation
    for i in range(12):
        sys.stdout.write(f"\r{C6}[{C14}{'!' * (i%4)}{C6}] {C16}Stabilizing Forensic Memory Buffers...{RST}")
        sys.stdout.flush()
        time.sleep(0.1)
    print(f"\n{C13}[+] Immutable Snapshotting Active. Incident Watchdog Ready.{RST}\n")

# ==========================================
# ARCHITECTURE: FORENSIC SNAPSHOT ENGINE
# ==========================================
class IncidentRecorder:
    """Captures and seals security incidents in an unalterable format."""
    def __init__(self):
        self.incident_vault = []

    def log_exposure(self, user, file_exposed, severity):
        """Creates a detailed forensic snapshot of an exposure event."""
        incident_id = f"INC-{secrets.token_hex(4).upper()}"
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        
        # Capture System Metadata (Simulated)
        metadata = {
            "source_ip": f"192.168.1.{secrets.randbelow(254)}",
            "access_vector": "Remote_SSH",
            "integrity_hash": hashlib.sha256(f"{ts}{file_exposed}".encode()).hexdigest()[:16]
        }
        
        incident_entry = {
            "id": incident_id,
            "time": ts,
            "user": user,
            "target": file_exposed,
            "sev": severity,
            "meta": metadata
        }
        
        self.incident_vault.append(incident_entry)
        self._display_incident(incident_entry)

    def _display_incident(self, inc):
        """Displays the incident in a high-impact military format."""
        s_color = C14 if inc["sev"] == "CRITICAL" else C9
        print(f"{C17}{C6}┌──[ INCIDENT CAPTURED ]{'─'*35}{RST}")
        print(f"{C6}│ {C16}CASE ID  : {C18}{inc['id']}{RST}")
        print(f"{C6}│ {C16}TIMESTAMP: {C8}{inc['time']}{RST}")
        print(f"{C6}│ {C16}SUBJECT  : {C15}{inc['user']}{RST}")
        print(f"{C6}│ {C16}EXPOSURE : {C5}{inc['target']}{RST}")
        print(f"{C6}│ {C16}SEVERITY : {s_color}{BLD}{inc['sev']}{RST}")
        print(f"{C6}│ {C16}HASH_TAG : {C10}{inc['meta']['integrity_hash']}{RST}")
        print(f"{C6}└{'─'*55}{RST}\n")

# ==========================================
# SIMULATION ENGINE
# ==========================================
def simulate_exposure_events():
    prithvi_banner_anim()
    recorder = IncidentRecorder()
    
    events = [
        ("Raj_G", "cui_nuclear_specs.pdf", "CRITICAL"),
        ("System_Monitor", "unauthorized_pcap_dump.log", "HIGH"),
        ("External_IP_88", "cui_staff_payroll.db", "CRITICAL")
    ]
    
    print(f"{C12}[!] ALERT: SENSORS DETECTED UNUSUAL CUI ACCESS PATTERNS{RST}")
    time.sleep(1)
    
    for user, target, sev in events:
        recorder.log_exposure(user, target, sev)
        time.sleep(1.5) # Time for manual inspection in simulation

    print(f"{C19}{BLD}[✔] All incidents have been cryptographically sealed.{RST}")
    print(f"{C6}[*] Digital Chain of Custody (CoC) maintained.{RST}")

if __name__ == "__main__":
    try:
        simulate_exposure_events()
    except KeyboardInterrupt:
        print(f"\n{C14}[!] Forensic recording interrupted.{RST}")