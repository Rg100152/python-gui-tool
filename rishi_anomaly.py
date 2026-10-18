import os
import sys
import time
import math
import statistics
import secrets
from datetime import datetime

# ==========================================
# RISHI-ANOMALY: SAGE CONSCIOUSNESS THEME
# (Exactly 10 Unique ANSI 256 Colors)
# ==========================================
SAGE_GRN   = '\033[38;5;112m'  
TRANCE_PRP = '\033[38;5;129m'  
VISION_WHT = '\033[38;5;255m'  
KARMA_GLD  = '\033[38;5;220m'  
MAYA_CYN   = '\033[38;5;51m'   
SHUNYA_BLK = '\033[38;5;232m'  
KRODH_RED  = '\033[38;5;196m'  
BODHI_BLU  = '\033[38;5;33m'   
DHYAN_YLW  = '\033[38;5;226m'  
ASH_GRY    = '\033[38;5;244m'  
RST        = '\033[0m'
BLD        = '\033[1m'

# ==========================================
# LOGO & BOOT: THE THIRD EYE OF SAGE
# ==========================================
def rishi_vision_animation():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    logo = f"""
    {SAGE_GRN}          _  _          
    {SAGE_GRN}         ( \/ )         
    {SAGE_GRN}  .---.  {KARMA_GLD} \  / {SAGE_GRN}  .---.  
    {SAGE_GRN} /     \ {KARMA_GLD}  \/  {SAGE_GRN} /     \\ 
    {SAGE_GRN}(  {VISION_WHT}O {SAGE_GRN}  ){KARMA_GLD}  ||  {SAGE_GRN}(  {VISION_WHT}O {SAGE_GRN}  )
    {SAGE_GRN} \     / {KARMA_GLD}  ||  {SAGE_GRN} \     / 
    {SAGE_GRN}  '---'  {KARMA_GLD}  ||  {SAGE_GRN}  '---'  
    {KARMA_GLD}         {TRANCE_PRP}/  \{KARMA_GLD}         
    {RST}"""
    print(logo)
    print(f"{SAGE_GRN}{BLD}   RISHI-ANOMALY v3.5: GAUSSIAN SENTRY{RST}\n")
    
    # Meditation scanning animation
    for i in range(10):
        dots = "." * (i % 4)
        sys.stdout.write(f"\r{BODHI_BLU}[*] Meditating on Data Flow{dots} {ASH_GRY}(Training Baselines){RST}")
        sys.stdout.flush()
        time.sleep(0.2)
    print(f"\n{MAYA_CYN}[+] Third Eye Awakened. Monitoring for Karmic Deviations.{RST}\n")

# ==========================================
# ARCHITECTURE: GAUSSIAN STATISTICAL ENGINE
# ==========================================
class RishiEngine:
    """Uses Z-Score statistics to identify outliers in request patterns."""
    def __init__(self, threshold=2.5):
        self.history = []
        self.threshold = threshold # Standard deviations
        self.is_trained = False

    def observe(self, request_count):
        """Learns the behavior pattern and detects anomalies."""
        self.history.append(request_count)
        
        # We need at least 10 data points to form a baseline
        if len(self.history) < 10:
            return "LEARNING", 0.0
            
        mean = statistics.mean(self.history)
        stdev = statistics.stdev(self.history) if len(self.history) > 1 else 1
        
        # Z-Score Calculation: (Observed - Mean) / Stdev
        z_score = abs(request_count - mean) / stdev
        
        if z_score > self.threshold:
            return "ANOMALY", z_score
        else:
            return "NORMAL", z_score

# ==========================================
# REAL-TIME SIMULATION
# ==========================================
def run_anomaly_detector():
    rishi_vision_animation()
    rishi = RishiEngine(threshold=2.2)
    
    # 1. Normal User Activity (Baseline)
    print(f"{BODHI_BLU}>>> PHASE 1: NORMAL USER BEHAVIOR (BASELINE TRAINING){RST}")
    for i in range(15):
        reqs = secrets.randbelow(10) + 20 # Constant traffic between 20-30 reqs
        status, z = rishi.observe(reqs)
        
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"{ASH_GRY}[{timestamp}]{RST} Flow: {MAYA_CYN}{reqs:<3}{RST} | Z-Score: {ASH_GRY}{z:.2f}{RST} | State: {MAYA_CYN}{status}{RST}")
        time.sleep(0.3)

    print(f"\n{KARMA_GLD}[!] Baseline Established. Activating Vigilance Mode...{RST}\n")
    time.sleep(1)

    # 2. Sudden Attack / Suspicious Activity
    print(f"{DHYAN_YLW}>>> PHASE 2: INCOMING NETWORK ANOMALY DETECTED{RST}")
    
    # Test cases: Small spike, Huge spike, Low spike
    test_scenarios = [28, 35, 120, 25, 400, 22]
    
    for reqs in test_scenarios:
        status, z = rishi.observe(reqs)
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        if status == "ANOMALY":
            color = KRODH_RED
            alert = f"{KRODH_RED}{BLD}!!! CRITICAL DEVIATION DETECTED !!!{RST}"
        else:
            color = MAYA_CYN
            alert = f"{MAYA_CYN}Pattern Stable.{RST}"
            
        print(f"{ASH_GRY}[{timestamp}]{RST} Flow: {color}{reqs:<3}{RST} | Z-Score: {KRODH_RED if z > 2.2 else ASH_GRY}{z:.2f}{RST}")
        if status == "ANOMALY":
            print(f"      {alert}")
            print(f"      {TRANCE_PRP}Reason: Traffic spike is {z:.1f}x away from normal user karma.{RST}")
        time.sleep(0.8)

if __name__ == "__main__":
    try:
        run_anomaly_detector()
        print(f"\n{SAGE_GRN}[*] Rishi-Anomaly has finished the session. Environment clean.{RST}")
    except KeyboardInterrupt:
        print(f"\n{KRODH_RED}[!] Sentry Deactivated.{RST}")