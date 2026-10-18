import os
import sys
import time
import secrets
from datetime import datetime

# ==========================================
# DEVA-GATEWAY: CELESTIAL PROTECTOR 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;33m', '\033[38;5;51m', '\033[38;5;255m', '\033[38;5;93m', '\033[38;5;196m'
C6, C7, C8, C9, C10  = '\033[38;5;226m', '\033[38;5;46m', '\033[38;5;232m', '\033[38;5;87m', '\033[38;5;208m'
C11, C12, C13, C14, C15 = '\033[38;5;201m', '\033[38;5;141m', '\033[38;5;253m', '\033[38;5;250m', '\033[38;5;252m'
C16, C17, C18, C19, C20 = '\033[38;5;235m', '\033[38;5;160m', '\033[38;5;35m', '\033[38;5;214m', '\033[38;5;233m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE DIVINE GATE (DEVA)
# ==========================================
def deva_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C3}           /\\
    {C3}          /  \\          {C1}D E V A
    {C2}         | [] |         {C10}G A T E W A Y
    {C2}       --|____|--       {C15}v6.0 [ZERO_TRUST]
    {C1}      |          |
    {C1}      |____  ____|
    """
    print(logo)
    print(f"{C1}{BLD}   DEVA-GATEWAY: MULTI-LAYERED PERIMETER DEFENSE{RST}\n")
    
    # Gateway Initialization
    protocols = ["mTLS_Auth", "Geo_Fence", "JWT_Verify", "Payload_Scan"]
    for p in protocols:
        sys.stdout.write(f"\r{C16}[{C6}WAIT{C16}] {C3}Engaging Security Layer: {C2}{p:<15}{RST}")
        sys.stdout.flush()
        time.sleep(0.3)
    print(f"\n{C7}[+] Celestial Shield Active. Gateway is now In-Line.{RST}\n")

# ==========================================
# ARCHITECTURE: SECURE GATEWAY ENGINE
# ==========================================
class DevaGateway:
    """Simulates a secure entry/exit point for sensitive data networks."""
    def __init__(self):
        self.blocked_countries = ["RU", "CN", "KP"]
        self.valid_tokens = ["TOKEN_RAJ_2026", "TOKEN_VBSPU_ADMIN"]

    def process_request(self, ip, country, token, direction, payload):
        """Validates request based on multi-factor telemetry."""
        ts = datetime.now().strftime("%H:%M:%S")
        print(f"{C16}[{ts}] {C10}INCOMING: {C3}{direction:<7} {C16}| {C13}ORIGIN: {country} ({ip}){RST}")
        time.sleep(0.8)

        # 1. Geo-Fencing Check
        if country in self.blocked_countries:
            self._trigger_violation(ip, country, "GEO_FENCE_BLOCK")
            return False

        # 2. Token/mTLS Validation
        if token not in self.valid_tokens:
            self._trigger_violation(ip, country, "INVALID_AUTH_TOKEN")
            return False

        # 3. Payload Inspection (Egress)
        if direction == "EGRESS" and "CUI" in payload.upper():
            self._trigger_violation(ip, country, "UNAUTHORIZED_CUI_EXPORT")
            return False

        print(f"{C7}{BLD}[✔] ACCESS GRANTED: Request routed through secure tunnel.{RST}\n")
        return True

    def _trigger_violation(self, ip, country, reason):
        print(f"\n{C5}{BLD}!!! DEVA-GATEWAY: PERIMETER BREACH ATTEMPT !!!{RST}")
        print(f"{C5}│ {C3}SOURCE IP : {C2}{ip}{RST}")
        print(f"{C5}│ {C3}COUNTRY   : {C11}{country}{RST}")
        print(f"{C5}│ {C3}REASON    : {C5}{BLD}{reason}{RST}")
        print(f"{C5}│ {C3}ACTION    : {C5}{BLD}CONNECTION_TERMINATED | IP_SHUNTED{RST}")
        print(f"{C5}└{'─'*55}{RST}\n")
        time.sleep(0.5)

# ==========================================
# SIMULATION: NETWORK EDGE TRAFFIC
# ==========================================
def run_gateway_sim():
    deva_banner_anim()
    gate = DevaGateway()
    
    # Traffic Scenarios
    scenarios = [
        ("192.168.1.5", "IN", "TOKEN_RAJ_2026", "INGRESS", "Requesting dashboard"),
        ("45.12.3.11", "RU", "TOKEN_EXPIRED", "INGRESS", "Brute force attempt"), # Geo Violation
        ("10.0.0.50", "IN", "TOKEN_VBSPU_ADMIN", "EGRESS", "Exporting public_notes.txt"),
        ("10.0.0.50", "IN", "TOKEN_VBSPU_ADMIN", "EGRESS", "Exporting CUI_Research.pdf"), # Content Violation
        ("172.16.1.4", "US", "UNKNOWN", "INGRESS", "Anonymous scan") # Auth Violation
    ]
    
    print(f"{C12}[!] MONITORING PERIMETER TRUNKS (DEVA-G1)...{RST}\n")
    
    for ip, loc, tok, direct, pay in scenarios:
        time.sleep(1.5)
        gate.process_request(ip, loc, tok, direct, pay)

if __name__ == "__main__":
    try:
        run_gateway_sim()
        print(f"{C7}[*] Deva-Gateway stabilized. Boundary remains impenetrable.{RST}")
    except KeyboardInterrupt:
        print(f"\n{C5}[!] Gateway Offline.{RST}")