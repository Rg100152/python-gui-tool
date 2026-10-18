import os
import sys
import time
import math
import secrets
from datetime import datetime, timedelta

# ==========================================
# SOMA-ANALYZER: LUNAR CLARITY 20-COLOR PALETTE
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;51m', '\033[38;5;252m', '\033[38;5;24m', '\033[38;5;122m', '\033[38;5;231m'
C6, C7, C8, C9, C10  = '\033[38;5;18m', '\033[38;5;159m', '\033[38;5;57m', '\033[38;5;33m', '\033[38;5;31m'
C11, C12, C13, C14, C15 = '\033[38;5;147m', '\033[38;5;93m', '\033[38;5;96m', '\033[38;5;170m', '\033[38;5;60m'
C16, C17, C18, C19, C20 = '\033[38;5;43m', '\033[38;5;48m', '\033[38;5;22m', '\033[38;5;250m', '\033[38;5;255m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE LUNAR CRESCENT
# ==========================================
def soma_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C1}         _.._
    {C7}       .' .-'`
    {C4}      /  /      {C1}S O M A
    {C10}      |  |      {C2}A N A L Y Z E R
    {C9}      \\  \\      {C11}v3.7 [TREND_ENGINE]
    {C8}       '._'-._
    {C6}          `--`
    """
    print(logo)
    print(f"{C1}{BLD}   SOMA-ANALYZER: SEMANTIC THREAT TREND IDENTIFICATION{RST}\n")
    
    # Pulse animation
    for i in range(12):
        sys.stdout.write(f"\r{C3}[{C1}{'#' * (i+1)}{C3}{' ' * (11-i)}] {C2}Aggregating Temporal Log Data...{RST}")
        sys.stdout.flush()
        time.sleep(0.08)
    print(f"\n{C17}[+] Neural Archive Synced. Ready for Pattern Extraction.{RST}\n")

# ==========================================
# ARCHITECTURE: TREND ANALYSIS ENGINE
# ==========================================
class SomaTrendEngine:
    """Identifies surges and patterns in security event streams."""
    def __init__(self):
        self.event_buckets = {} # {timestamp: {type: count}}
        self.threat_threshold = 1.5 # 150% increase triggers a trend alert

    def ingest_log(self, log_type, ts):
        """Groups logs into 1-minute temporal buckets."""
        bucket_key = ts.strftime("%H:%M")
        if bucket_key not in self.event_buckets:
            self.event_buckets[bucket_key] = {}
        
        self.event_buckets[bucket_key][log_type] = self.event_buckets[bucket_key].get(log_type, 0) + 1

    def identify_trends(self):
        """Analyzes the delta between the last two buckets to detect surges."""
        buckets = sorted(self.event_buckets.keys())
        if len(buckets) < 2: return []

        prev_b, curr_b = buckets[-2], buckets[-1]
        trends = []

        for log_type in self.event_buckets[curr_b]:
            curr_val = self.event_buckets[curr_b][log_type]
            prev_val = self.event_buckets[prev_b].get(log_type, 0)

            # Avoid division by zero, assume baseline of 1
            growth = (curr_val / max(1, prev_val))
            
            if growth >= self.threat_threshold:
                trends.append((log_type, growth, curr_val))
        
        return trends

# ==========================================
# ANALYTICAL DASHBOARD SIMULATION
# ==========================================
def render_dashboard(engine):
    """A high-tech visualization of the log trends."""
    trends = engine.identify_trends()
    
    print(f"{C15}┌──[ TIME-SERIES SECURITY DASHBOARD ]{'─'*25}{RST}")
    
    # Show active counts
    latest_ts = sorted(engine.event_buckets.keys())[-1]
    data = engine.event_buckets[latest_ts]
    
    for ltype, count in data.items():
        bar = f"{C9}{'█' * count}{RST}"
        print(f"{C15}│ {C11}{ltype:<18} {C2}Count: {C5}{count:<3} {bar}")

    if trends:
        print(f"{C15}├{'─'*58}{RST}")
        for ltype, growth, val in trends:
            color = '\033[38;5;196m' if growth > 2.0 else C14
            print(f"{C15}│ {C1}TREND ALERT: {color}{BLD}SURGE IN {ltype.upper()}{RST}")
            print(f"{C15}│ {C14}Growth: {color}+{int((growth-1)*100)}% {RST}over previous window.")
    
    print(f"{C15}└{'─'*58}{RST}\n")

def simulate_log_stream():
    soma_banner_anim()
    engine = SomaTrendEngine()
    log_types = ["SQL_INJECTION", "AUTH_FAILURE", "FILE_READ", "SSH_LOGIN", "XSS_ATTEMPT"]
    
    base_time = datetime.now()
    
    # Phase 1: Normal baseline (Bucket T-1)
    for _ in range(20):
        ltype = secrets.choice(log_types)
        engine.ingest_log(ltype, base_time - timedelta(minutes=1))
    
    # Phase 2: Active attack (Current Bucket)
    print(f"{C12}[*] Ingesting Live Log Stream...{RST}")
    for i in range(50):
        # High probability of SQL_INJECTION to create a trend
        weights = [10, 2, 2, 2, 2] # SQLi is heavily weighted
        ltype = secrets.choice(random_choices(log_types, weights))
        engine.ingest_log(ltype, base_time)
        
        if i % 10 == 0:
            sys.stdout.write(f"{C7}·{RST}")
            sys.stdout.flush()
            time.sleep(0.3)
    
    print("\n")
    render_dashboard(engine)

def random_choices(population, weights):
    """Helper for weighted selection in old python versions."""
    res = []
    for p, w in zip(population, weights):
        res.extend([p] * w)
    return res

if __name__ == "__main__":
    try:
        simulate_log_stream()
        print(f"{C17}[✔] Analysis complete. Patterns archived to Neural Cache.{RST}")
    except KeyboardInterrupt:
        print(f"\n{C13}[!] Analysis Halted.{RST}")