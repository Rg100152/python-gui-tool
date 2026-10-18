import os
import sys
import time
import secrets
from datetime import datetime

# ==========================================
# MARUT-INTRUSION: TEMPEST & AIR 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;33m', '\033[38;5;244m', '\033[38;5;226m', '\033[38;5;231m', '\033[38;5;30m'
C6, C7, C8, C9, C10  = '\033[38;5;51m', '\033[38;5;93m', '\033[38;5;118m', '\033[38;5;250m', '\033[38;5;153m'
C11, C12, C13, C14, C15 = '\033[38;5;39m', '\033[38;5;18m', '\033[38;5;60m', '\033[38;5;196m', '\033[38;5;252m'
C16, C17, C18, C19, C20 = '\033[38;5;232m', '\033[38;5;160m', '\033[38;5;28m', '\033[38;5;214m', '\033[38;5;234m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE WHIRLWIND SENTRY (MARUT)
# ==========================================
def marut_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C6}             _
    {C6}          __( )__      {C1}M A R U T
    {C1}       _ (  _  _ ) _   {C8}I N T R U S I O N
    {C10}      (_(_(_)(_)_)_)   {C15}v5.5 [H-NIDS_ENGINE]
    {C5}         / /  / / 
    {C5}        /_/  /_/  
    """
    print(logo)
    print(f"{C6}{BLD}   MARUT-INTRUSION: MULTI-VECTOR THREAT DETECTION SYSTEM{RST}\n")
    
    # Sensor calibration animation
    sensors = ["Log_Watch", "Traffic_Scanner", "Process_Monitor", "Auth_Sentry"]
    for s in sensors:
        sys.stdout.write(f"\r{C2}[{C3}SYNC{C2}] {C4}Activating Sensor: {C6}{s:<16}{RST}")
        sys.stdout.flush()
        time.sleep(0.3)
    print(f"\n{C8}[+] All Air-Gapped and Network Sensors are Live. Vigilance Mode Active.{RST}\n")

# ==========================================
# ARCHITECTURE: HYBRID IDS ENGINE
# ==========================================
class MarutIDS:
    """Simulates an intrusion detection system with signature & anomaly logic."""
    def __init__(self):
        self.signatures = ["UNION SELECT", "../etc/passwd", "DROP TABLE", "BASH_REVERSE_SHELL"]
        self.auth_attempts = {}

    def analyze_event(self, source, event_type, data):
        """Analyzes event data for intrusions."""
        ts = datetime.now().strftime("%H:%M:%S")
        
        # 1. Signature-Based Check
        sig_match = [s for s in self.signatures if s in data.upper()]
        
        # 2. Anomaly-Based Check (Brute-force simulation)
        is_anomaly = False
        if event_type == "AUTH_FAIL":
            self.auth_attempts[source] = self.auth_attempts.get(source, 0) + 1
            if self.auth_attempts[source] > 3:
                is_anomaly = True

        # Decision Logic
        if sig_match or is_anomaly:
            reason = f"Sig_Match: {sig_match}" if sig_match else "Brute_Force_Anomaly"
            self._trigger_intrusion_alert(ts, source, event_type, reason, data)
            return False
        
        # Normal Traffic Display
        print(f"{C2}[{ts}] {C5}{event_type:<10} {C9}SRC:{source:<12} {C10}| {C4}DATA: {data[:20]}... {C8}[OK]{RST}")
        return True

    def _trigger_intrusion_alert(self, ts, src, etype, reason, raw):
        print(f"\n{C14}{BLD}!!! MARUT-INTRUSION: THREAT VECTORS DETECTED !!!{RST}")
        print(f"{C14}│ {C4}TIMESTAMP : {C10}{ts}{RST}")
        print(f"{C14}│ {C4}SOURCE    : {C11}{src}{RST}")
        print(f"{C14}│ {C4}CATEGORY  : {C14}{etype}{RST}")
        print(f"{C14}│ {C4}EVIDENCE  : {C3}{reason}{RST}")
        print(f"{C14}│ {C4}RAW_DATA  : {C2}{raw}{RST}")
        print(f"{C14}│ {C4}ACTION    : {C14}{BLD}BLOCK_SRC | ISOLATE_NODE | ADMIN_NOTIFIED{RST}")
        print(f"{C14}└{'─'*55}{RST}\n")
        time.sleep(1)

# ==========================================
# SIMULATION: REAL-TIME EVENT STREAM
# ==========================================
def start_monitoring():
    marut_banner_anim()
    ids = MarutIDS()
    
    # Event Stream Data
    events = [
        ("192.168.1.5", "SQL_QUERY", "SELECT * FROM users WHERE id=1"),
        ("10.0.0.99", "AUTH_FAIL", "Invalid credentials for user 'admin'"),
        ("10.0.0.99", "AUTH_FAIL", "Invalid credentials for user 'admin'"),
        ("45.33.12.1", "HTTP_REQ", "GET /search?q=' OR 1=1; UNION SELECT passwd'"), # VIOLATION
        ("10.0.0.99", "AUTH_FAIL", "Invalid credentials for user 'admin'"),
        ("10.0.0.99", "AUTH_FAIL", "Invalid credentials for user 'admin'"), # VIOLATION (Anomaly)
        ("192.168.1.10", "SYS_LOG", "CUI_Access granted to Raj_G"),
        ("152.1.44.2", "TRAFFIC", "Attempting to download ../etc/passwd") # VIOLATION
    ]
    
    print(f"{C13}[!] SNIFFING SYSTEM AND NETWORK LOGS FOR ANOMALIES...{RST}\n")
    
    for src, etype, data in events:
        time.sleep(1.2)
        ids.analyze_event(src, etype, data)

if __name__ == "__main__":
    try:
        start_monitoring()
        print(f"{C8}[✔] Marut-Intrusion session stabilized. All vectors secured.{RST}")
    except KeyboardInterrupt:
        print(f"\n{C14}[!] IDS Offline.{RST}")