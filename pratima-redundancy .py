import os
import sys
import time
import random
from datetime import datetime

# ==========================================
# PRATIMA-REDUNDANCY: MIRROR IMAGE 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;220m', '\033[38;5;51m', '\033[38;5;250m', '\033[38;5;46m', '\033[38;5;208m'
C6, C7, C8, C9, C10  = '\033[38;5;196m', '\033[38;5;231m', '\033[38;5;93m', '\033[38;5;244m', '\033[38;5;232m'
C11, C12, C13, C14, C15 = '\033[38;5;118m', '\033[38;5;158m', '\033[38;5;18m', '\033[38;5;202m', '\033[38;5;242m'
C16, C17, C18, C19, C20 = '\033[38;5;234m', '\033[38;5;124m', '\033[38;5;28m', '\033[38;5;214m', '\033[38;5;233m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE TWIN PILLARS (PRATIMA)
# ==========================================
def pratima_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C2}             ||      ||
    {C2}             ||      ||        {C1}P R A T I M A
    {C1}             ||      ||        {C5}R E D U N D A N C Y
    {C3}            [==]    [==]       {C15}v9.4 [HIGH_AVAILABILITY]
    {C2}             ||      ||
    {C13}          [{C11}HEARTBEAT_SYNCED{C13}]
    """
    print(logo)
    print(f"{C1}{BLD}   PRATIMA-REDUNDANCY: ACTIVE-PASSIVE FAILOVER ORCHESTRATION{RST}\n")
    
    # Sync animation
    states = ["Checking_Primary", "Heartbeat_Ping", "Data_Replication", "Standby_Ready"]
    for s in states:
        sys.stdout.write(f"\r{C15}[{C2}LIVE{C15}] {C1}Synchronizing Twin Pillars: {C12}{s:<20}{RST}")
        sys.stdout.flush()
        time.sleep(0.3)
    print(f"\n{C11}[+] Cluster Health: OPTIMAL. Primary and Pratima nodes in sync.{RST}\n")

# ==========================================
# ARCHITECTURE: FAILOVER ENGINE
# ==========================================
class PratimaCluster:
    """Manages Active and Standby nodes with automated failover logic."""
    def __init__(self):
        self.primary_status = "ACTIVE"
        self.standby_status = "STANDBY"
        self.health_pings = 0

    def monitor_heartbeat(self):
        """Simulates the constant monitoring between twin nodes."""
        ts = datetime.now().strftime("%H:%M:%S")
        self.health_pings += 1
        
        # Simulating a random failure after some successful pings
        if self.health_pings > 3 and random.random() < 0.3:
            self.primary_status = "FAILED"
            print(f"{C6}{BLD}[!] HEARTBEAT LOST: Primary Node is unresponsive!{RST}")
            self._trigger_failover(ts)
            return False
        
        print(f"{C15}[{ts}] {C4}HEARTBEAT: {C7}Primary -> {C11}OK{RST} | {C2}Standby -> {C11}OK{RST}")
        return True

    def _trigger_failover(self, ts):
        print(f"{C13}[*] PRATIMA-ENGINE: Initiating Emergency Failover...{RST}")
        time.sleep(1)
        self.standby_status = "PROMOTED_TO_ACTIVE"
        print(f"\n{C16}┌─────────────────────────────────────────────────────┐")
        print(f"{C16}│ {C5}{BLD}FAILOVER CERTIFICATE: CLUSTER RE-STABILIZED{' '*8} {C16}│")
        print(f"{C16}├─────────────────────────────────────────────────────┤")
        print(f"{C16}│ {C1}TIMESTAMP : {ts:<39} {C16}│")
        print(f"{C16}│ {C3}NEW MASTER: PRATIMA_NODE_B (Standby){' '*14} {C16}│")
        print(f"{C16}│ {C11}DOWNTIME  : < 1.2 Seconds{' '*26} {C16}│")
        print(f"{C16}└─────────────────────────────────────────────────────┘{RST}\n")

# ==========================================
# SIMULATION: NODE FAILURE SCENARIO
# ==========================================
if __name__ == "__main__":
    try:
        pratima_banner_anim()
        cluster = PratimaCluster()
        
        # Run monitor loop
        while cluster.primary_status == "ACTIVE":
            time.sleep(1.2)
            if not cluster.monitor_heartbeat():
                break
        
        print(f"{C11}[✔] Continuity maintained. CUI Inventory remains online via Pratima Node.{RST}")

    except KeyboardInterrupt:
        print(f"\n{C6}[!] Cluster Monitoring Disrupted.{RST}")