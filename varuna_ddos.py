import os
import sys
import time
import collections
from datetime import datetime

# ==========================================
# VARUNA-DDOS: OCEANIC & TIDAL 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;33m', '\033[38;5;18m', '\033[38;5;255m', '\033[38;5;244m', '\033[38;5;208m'
C6, C7, C8, C9, C10  = '\033[38;5;21m', '\033[38;5;51m', '\033[38;5;232m', '\033[38;5;28m', '\033[38;5;45m'
C11, C12, C13, C14, C15 = '\033[38;5;39m', '\033[38;5;27m', '\033[38;5;60m', '\033[38;5;196m', '\033[38;5;252m'
C16, C17, C18, C19, C20 = '\033[38;5;234m', '\033[38;5;160m', '\033[38;5;46m', '\033[38;5;214m', '\033[38;5;233m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE PROTECTIVE WAVE (VARUNA)
# ==========================================
def varuna_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C1}             _
    {C1}          _ ( ) _      {C11}V A R U N A
    {C11}       _ (       ) _   {C7}D D o S
    {C2}      (_______________)  {C15}v5.6 [TRAFFIC_SCRUBBER]
    {C10}         ~~~~ ~~~~
    {C10}        ~~~~~~~~~~~
    """
    print(logo)
    print(f"{C1}{BLD}   VARUNA-DDOS: FLOOD PROTECTION & TRAFFIC SHAPING{RST}\n")
    
    # Scrubbing center initialization
    for i in range(12):
        sys.stdout.write(f"\r{C4}[{C7}OK{C4}] {C1}Deploying Traffic Scrubbers: {C10}Zone_{i+1}... {C7}{'|/-\\'[i%4]}{RST}")
        sys.stdout.flush()
        time.sleep(0.1)
    print(f"\n{C19}[+] Global Traffic Throttling Active. Monitoring PPS (Packets Per Second).{RST}\n")

# ==========================================
# ARCHITECTURE: DDOS DEFENSE ENGINE
# ==========================================
class VarunaGuard:
    """Simulates a DDoS mitigation engine with rate limiting."""
    def __init__(self, limit=3):
        self.rate_limit = limit # Max 3 requests per second per IP
        self.traffic_history = collections.defaultdict(list)
        self.blocked_ips = set()

    def inspect_request(self, ip_addr):
        """Monitors request velocity to detect flood attacks."""
        ts = time.time()
        readable_ts = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        
        if ip_addr in self.blocked_ips:
            print(f"{C4}[{readable_ts}] {C17}DROPPED: {C4}Source {ip_addr} is globally blacklisted.{RST}")
            return False

        # Maintain history (only last 1 second)
        self.traffic_history[ip_addr] = [t for t in self.traffic_history[ip_addr] if ts - t < 1.0]
        
        # Check Threshold
        if len(self.traffic_history[ip_addr]) >= self.rate_limit:
            self._trigger_flood_mitigation(readable_ts, ip_addr)
            self.blocked_ips.add(ip_addr)
            return False

        # Allow request
        self.traffic_history[ip_addr].append(ts)
        print(f"{C4}[{readable_ts}] {C7}PASS: {C11}{ip_addr:<12} {C4}| Load: {len(self.traffic_history[ip_addr])}/{self.rate_limit} RPS {C19}[STABLE]{RST}")
        return True

    def _trigger_flood_mitigation(self, ts, ip):
        print(f"\n{C17}{BLD}!!! VARUNA-DDOS: TRAFFIC FLOOD DETECTED (IPS ALERT) !!!{RST}")
        print(f"{C17}│ {C3}TIME      : {C10}{ts}{RST}")
        print(f"{C17}│ {C3}ATTACKER  : {C17}{ip}{RST}")
        print(f"{C17}│ {C3}THRESHOLD : {C5}>{self.rate_limit} Requests/Sec{RST}")
        print(f"{C17}│ {C3}ACTION    : {C17}{BLD}BLACKHOLE_IP | CHALLENGE_SENT | DNS_REDIRECTION{RST}")
        print(f"{C17}└{'─'*55}{RST}\n")
        time.sleep(0.5)

# ==========================================
# SIMULATION: DDOS ATTACK VECTOR
# ==========================================
def run_ddos_sim():
    varuna_banner_anim()
    guard = VarunaGuard(limit=4) # Allowing 4 req/sec
    
    # 1. Normal Traffic
    print(f"{C13}[!] MONITORING NORMAL TRAFFIC FLOW...{RST}")
    for _ in range(3):
        guard.inspect_request("192.168.1.10")
        time.sleep(0.4)

    # 2. DDoS Attack (Fast Burst)
    print(f"\n{C14}[!] ALERT: DETECTING BOTNET BURST FROM 104.22.5.1...{RST}\n")
    for _ in range(6):
        guard.inspect_request("104.22.5.1")
        time.sleep(0.1) # Rapid requests

    # 3. Post-Attack Normalization
    time.sleep(1)
    guard.inspect_request("192.168.1.10") # Legitimate user still works
    guard.inspect_request("104.22.5.1")    # Still blocked

if __name__ == "__main__":
    try:
        run_ddos_sim()
        print(f"\n{C19}[✔] Varuna-DDoS mitigation successful. Server remains responsive.{RST}")
    except KeyboardInterrupt:
        print(f"\n{C17}[!] Mitigation Halted.{RST}")