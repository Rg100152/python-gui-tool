import os
import sys
import time
from datetime import datetime

# ==========================================
# SENA-FIREWALL: COMBAT BATTALION 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;65m', '\033[38;5;240m', '\033[38;5;136m', '\033[38;5;51m', '\033[38;5;196m'
C6, C7, C8, C9, C10  = '\033[38;5;94m', '\033[38;5;232m', '\033[38;5;255m', '\033[38;5;137m', '\033[38;5;160m'
C11, C12, C13, C14, C15 = '\033[38;5;46m', '\033[38;5;18m', '\033[38;5;143m', '\033[38;5;244m', '\033[38;5;22m'
C16, C17, C18, C19, C20 = '\033[38;5;233m', '\033[38;5;88m', '\033[38;5;28m', '\033[38;5;214m', '\033[38;5;16m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE COMBAT SHIELD (SENA)
# ==========================================
def sena_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C1}            _________
    {C1}           |  {C3}/   \\{C1}  |
    {C2}           | {C3}| {C8}S{C3} |{C2} |    {C1}S E N A
    {C2}           | {C3}| {C8}E{C3} |{C2} |    {C2}F I R E W A L L
    {C1}           | {C3}| {C8}N{C3} |{C1} |    {C14}v6.6 [HOST_DEFENSE]
    {C1}            \\{C3}\\ {C8}A{C3} /{C1}/
    {C2}             \\___/
    """
    print(logo)
    print(f"{C1}{BLD}   SENA-FIREWALL: LOCAL HOST OS PERIMETER LOCKDOWN{RST}\n")
    
    # Booting Up Sena Rulesets
    chains = ["INPUT_CHAIN", "OUTPUT_CHAIN", "FORWARD_CHAIN", "PORT_MASKING"]
    for chain in chains:
        sys.stdout.write(f"\r{C2}[{C3}BOOT{C2}] {C8}Hardening OS Tables: {C1}{chain:<18}{RST}")
        sys.stdout.flush()
        time.sleep(0.3)
    print(f"\n{C11}[+] Sena Battalion is stationed at the Kernel level. Default Policy: DROP.{RST}\n")

# ==========================================
# ARCHITECTURE: HOST-BASED FIREWALL ENGINE
# ==========================================
class SenaHostDefense:
    """Enforces strict host-level rules directly on the operating system ports."""
    def __init__(self):
        # Strict IPtables-style Rules
        self.ruleset = {
            "IN_SSH": {"port": 22, "src_ip": "10.0.5.50", "action": "ALLOW"}, # Only Admin IP
            "IN_WEB": {"port": 443, "src_ip": "ANY", "action": "ALLOW"},
            "OUT_DNS": {"port": 53, "dst_ip": "10.0.0.2", "action": "ALLOW"} # Only Internal DNS
        }
        self.default_policy = "DROP"

    def inspect_socket(self, direction, proto, port, ip_addr):
        ts = datetime.now().strftime("%H:%M:%S")
        
        # Determine if packet matches any explicit ALLOW rule
        action = self.default_policy
        matched_rule = None
        
        for rule_name, rule_data in self.ruleset.items():
            if direction in rule_name and rule_data["port"] == port:
                if rule_data.get("src_ip") in [ip_addr, "ANY"] or rule_data.get("dst_ip") in [ip_addr, "ANY"]:
                    action = rule_data["action"]
                    matched_rule = rule_name
                    break

        # Display Result
        if action == "ALLOW":
            print(f"{C2}[{ts}] {C4}{direction:<6}{RST} {C8}| PROTO: {proto:<4} | PORT: {port:<4} | IP: {ip_addr:<15} {C2}>> {C11}ACCEPTED ({matched_rule}){RST}")
        else:
            self._trigger_host_block(ts, direction, port, ip_addr)

    def _trigger_host_block(self, ts, direction, port, ip):
        print(f"\n{C5}{BLD}!!! SENA-FIREWALL: HOST-LEVEL INTRUSION BLOCKED !!!{RST}")
        print(f"{C5}│ {C8}TIME      : {C14}{ts}{RST}")
        print(f"{C5}│ {C8}VECTOR    : {C5}{direction} on Port {port}{RST}")
        print(f"{C5}│ {C8}THREAT IP : {C10}{ip}{RST}")
        print(f"{C5}│ {C8}ACTION    : {C5}{BLD}PACKET_DROPPED_SILENTLY (STEALTH MODE){RST}")
        print(f"{C5}└{'─'*55}{RST}\n")
        time.sleep(0.5)

# ==========================================
# SIMULATION: KERNEL TRAFFIC MONITORING
# ==========================================
if __name__ == "__main__":
    try:
        sena_banner_anim()
        hbf = SenaHostDefense()
        
        # Traffic Simulation Array
        traffic_events = [
            ("IN", "TCP", 443, "192.168.1.100"),  # Allowed Web Traffic
            ("IN", "TCP", 22, "10.0.5.50"),       # Allowed Admin SSH
            ("IN", "TCP", 22, "172.16.0.4"),      # BLOCKED: Unauthorized SSH attempt
            ("OUT", "UDP", 53, "10.0.0.2"),       # Allowed DNS query
            ("OUT", "TCP", 80, "8.8.8.8"),        # BLOCKED: Server shouldn't browse the web
            ("IN", "TCP", 3389, "10.0.5.50")      # BLOCKED: RDP not in allowed rules
        ]
        
        print(f"{C13}[!] MONITORING LOCAL SOCKETS & DAEMONS...{RST}\n")
        
        for evt in traffic_events:
            time.sleep(1.2)
            hbf.inspect_socket(evt[0], evt[1], evt[2], evt[3])
            
        print(f"\n{C11}[✔] OS Perimeter secure. Sena guards the gates.{RST}")
    except KeyboardInterrupt:
        print(f"\n{C5}[!] Firewall deactivated. Host is exposed!{RST}")