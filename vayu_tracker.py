import os
import time
import sys
import threading
import queue
import secrets
from datetime import datetime

# ==========================================
# VAYU-TRACKER: DOPPLER STORM THEME
# (Exactly 10 Unique ANSI 256 Colors)
# ==========================================
STORM_BLU     = '\033[38;5;25m'   
LIGHTNING_WHT = '\033[38;5;231m'  
RADAR_GRN     = '\033[38;5;40m'   
SQUALL_GRY    = '\033[38;5;240m'  
VORTEX_PURP   = '\033[38;5;93m'   
HAIL_CYN      = '\033[38;5;51m'    
GALE_YLW      = '\033[38;5;220m'  
CYCLONE_ORG   = '\033[38;5;208m'  
TYPHOON_RED   = '\033[38;5;196m'  
CALM_TEAL     = '\033[38;5;37m'   
RST           = '\033[0m'
BLD           = '\033[1m'

# ==========================================
# ANIMATION: STORM RADAR SCAN
# ==========================================
def vayu_radar_animation():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{STORM_BLU}{BLD}>> VAYU-TRACKER: EVENT THREAT RADAR <<{RST}\n")
    
    radar_chars = ["-", "\\", "|", "/"]
    for i in range(15):
        char = radar_chars[i % 4]
        dist = " " * i
        sys.stdout.write(f"\r{RADAR_GRN}[SCAN] {SQUALL_GRY}{dist}{char} Scanning Atmos-Sphere...{RST}")
        sys.stdout.flush()
        time.sleep(0.1)
    print(f"\n{CALM_TEAL}[+] Pulse-Doppler Sensors Locked. Monitoring Stream.{RST}\n")

# ==========================================
# ARCHITECTURE: PUB/SUB ALERT ENGINE
# ==========================================

class VayuBroker:
    """The Message Broker (The Pipe) where all events flow."""
    def __init__(self):
        self.bus = queue.Queue()

    def publish(self, event_type, source, severity, message):
        """Publishers send events here."""
        event = {
            "time": datetime.now().strftime("%H:%M:%S"),
            "type": event_type,
            "src": source,
            "sev": severity,
            "msg": message
        }
        self.bus.put(event)

class AlertSubscriber(threading.Thread):
    """The Consumer that analyzes the event stream for threat patterns."""
    def __init__(self, broker):
        super().__init__(daemon=True)
        self.broker = broker
        self.failed_logins = {} # Heuristic memory: {user: count}

    def run(self):
        while True:
            event = self.broker.bus.get()
            self._process_event(event)
            self.broker.bus.task_done()

    def _process_event(self, ev):
        """Heuristic Engine: Decides when to escalate a log to an alert."""
        # 1. Standard Logging
        print(f"{SQUALL_GRY}[LOG-{ev['time']}] {ev['src']}: {ev['msg']}{RST}")
        
        # 2. HEURISTIC: Brute Force Detection
        if ev['type'] == "AUTH_FAIL":
            user = ev['msg'].split()[-1]
            self.failed_logins[user] = self.failed_logins.get(user, 0) + 1
            
            if self.failed_logins[user] >= 3:
                self._trigger_alert("BRUTE_FORCE", user, "CRITICAL")
                self.failed_logins[user] = 0 # Reset after alert
        
        # 3. HEURISTIC: Unauthorized File Access
        if ev['sev'] == "HIGH" and "UNAUTHORIZED" in ev['type']:
            self._trigger_alert("PRIV_ESCALATION", ev['src'], "HIGH")

    def _trigger_alert(self, alert_type, target, severity):
        """Displays visual high-impact alerts."""
        color = TYPHOON_RED if severity == "CRITICAL" else CYCLONE_ORG
        print(f"\n{color}{BLD}!!! {severity} ALERT: {alert_type} DETECTED !!!{RST}")
        print(f"{color}>>> TARGET: {target} | SECTOR: SECURITY_CORE{RST}\n")
        time.sleep(0.5)

# ==========================================
# SIMULATOR: THE LIVE ENVIRONMENT
# ==========================================

def start_simulation():
    vayu_radar_animation()
    broker = VayuBroker()
    
    # Start the Alert Subscriber in background
    subscriber = AlertSubscriber(broker)
    subscriber.start()

    print(f"{VORTEX_PURP}[*] Simulating Network Activity Traffic...{RST}\n")
    
    # Event Scenario Pipeline
    scenarios = [
        ("LOGIN", "UI_NODE", "INFO", "User Raj logged in."),
        ("FILE_ACCESS", "FS_NODE", "INFO", "User Raj read cui_policy.pdf"),
        ("AUTH_FAIL", "SSH_NODE", "WARN", "Failed login for Admin"),
        ("AUTH_FAIL", "SSH_NODE", "WARN", "Failed login for Admin"),
        ("AUTH_FAIL", "SSH_NODE", "WARN", "Failed login for Admin"), # Will trigger alert
        ("UNAUTHORIZED_READ", "DB_NODE", "HIGH", "Attempt to bypass ACL on USER_TABLE"), # Will trigger alert
        ("LOGOUT", "UI_NODE", "INFO", "User Raj logged out.")
    ]

    for etype, src, sev, msg in scenarios:
        time.sleep(1.2)
        broker.publish(etype, src, sev, msg)

    # Wait for all events to be processed
    broker.bus.join()
    print(f"\n{CALM_TEAL}[*] Vayu-Tracker simulation complete.{RST}")

if __name__ == "__main__":
    try:
        start_simulation()
    except KeyboardInterrupt:
        print(f"\n{TYPHOON_RED}[!] Radar Deactivated.{RST}")