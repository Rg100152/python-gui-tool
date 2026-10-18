import os
import sys
import time
import secrets
from datetime import datetime

# ==========================================
# DWIPA-SEGMENTER: ISOLATED ISLAND 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;45m', '\033[38;5;34m', '\033[38;5;223m', '\033[38;5;203m', '\033[38;5;18m'
C6, C7, C8, C9, C10  = '\033[38;5;30m', '\033[38;5;28m', '\033[38;5;255m', '\033[38;5;242m', '\033[38;5;214m'
C11, C12, C13, C14, C15 = '\033[38;5;39m', '\033[38;5;46m', '\033[38;5;101m', '\033[38;5;211m', '\033[38;5;251m'
C16, C17, C18, C19, C20 = '\033[38;5;234m', '\033[38;5;196m', '\033[38;5;80m', '\033[38;5;214m', '\033[38;5;232m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE PROTECTED ARCHIPELAGO (DWIPA)
# ==========================================
def dwipa_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C1}          .  {C2}  _  {C1}  .
    {C1}        .  {C2}  / \\ {C1}  .     {C1}D W I P A
    {C1}       .  {C2} ( O ) {C1} .     {C2}S E G M E N T E R
    {C5}      ~~~~~{C10}/   \\{C5}~~~~~     {C15}v5.3 [VLAN_ISOLATION]
    {C5}     ~~~~~~~~~~~~~~~~~
    """
    print(logo)
    print(f"{C1}{BLD}   DWIPA-SEGMENTER: NETWORK ISOLATION & INTER-ZONE ACL{RST}\n")
    
    # Virtual Segment Creation animation
    zones = ["GUEST", "STAFF", "CUI_VAULT", "ADMIN"]
    for i, zone in enumerate(zones):
        sys.stdout.write(f"\r{C9}[{C11}VLAN {10*(i+1)}{C9}] {C15}Provisioning Isolated Island: {C12}{zone:<10}{RST}")
        sys.stdout.flush()
        time.sleep(0.3)
    print(f"\n{C3}[+] Micro-Segmentation Complete. Zero-Trust Routing Active.{RST}\n")

# ==========================================
# ARCHITECTURE: INTER-ZONE ROUTING ENGINE
# ==========================================
class DwipaRouter:
    """Simulates a Layer 3 Switch with VLAN isolation and ACLs."""
    def __init__(self):
        # Access Control List (ACL) Rules
        self.acls = {
            "GUEST_TO_CUI": "DENY",
            "STAFF_TO_CUI": "INSPECT",
            "ADMIN_TO_CUI": "ALLOW",
            "CUI_TO_WAN": "DENY"
        }

    def route_packet(self, src_zone, dst_zone, packet_id):
        """Analyzes packets moving between virtual islands."""
        ts = datetime.now().strftime("%H:%M:%S")
        route_key = f"{src_zone}_TO_{dst_zone}"
        
        # Policy Lookup
        policy = self.acls.get(route_key, "DENY_DEFAULT")
        
        # UI Feedback
        color = C12 if policy == "ALLOW" else C10 if policy == "INSPECT" else C4
        print(f"{C9}[{ts}] {C11}PKT:{packet_id} {C15}{src_zone:>10} {C1}>> {C15}{dst_zone:<10} | {C9}POLICY: {color}{BLD}{policy}{RST}")

        if policy == "DENY" or policy == "DENY_DEFAULT":
            self._trigger_segment_block(src_zone, dst_zone)
            return False
        return True

    def _trigger_segment_block(self, src, dst):
        """Simulates dropping packets at the VLAN boundary."""
        print(f"\n{C4}{BLD}!!! DWIPA-SEGMENTER: INTER-ZONE BREACH PREVENTED !!!{RST}")
        print(f"{C4}│ {C8}SOURCE ZONE : {C11}{src}{RST}")
        print(f"{C4}│ {C8}TARGET ZONE : {C17}{dst} (PROTECTED){RST}")
        print(f"{C4}│ {C8}ACTION      : {C4}{BLD}VLAN_DROP | LOGGED_TO_SIEM{RST}")
        print(f"{C4}└{'─'*55}{RST}\n")
        time.sleep(0.5)

# ==========================================
# SIMULATION: NETWORK TRAFFIC FLOW
# ==========================================
def simulate_segmentation():
    dwipa_banner_anim()
    router = DwipaRouter()
    
    # Traffic Scenarios
    traffic = [
        ("GUEST", "STAFF", "PKT-101"),
        ("STAFF", "CUI_VAULT", "PKT-102"),  # Requires Inspection
        ("GUEST", "CUI_VAULT", "PKT-103"),  # HARD DENY
        ("ADMIN", "CUI_VAULT", "PKT-104"),  # ALLOW
        ("CUI_VAULT", "WAN", "PKT-105")     # EXFILTRATION PREVENTED
    ]
    
    print(f"{C13}[!] MONITORING INTER-VLAN TRAFFIC TRUNKS...{RST}\n")
    
    for src, dst, pid in traffic:
        time.sleep(1.2)
        router.route_packet(src, dst, pid)

if __name__ == "__main__":
    try:
        simulate_segmentation()
        print(f"{C12}[✔] Network द्वीपीकरण (Segmentation) complete. CUI Zone is isolated.{RST}")
    except KeyboardInterrupt:
        print(f"\n{C4}[!] Router Offline.{RST}")