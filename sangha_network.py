import os
import sys
import time
import secrets
import socket
from datetime import datetime

# ==========================================
# SANGHA-NETWORK: GLOBAL CONNECT 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;33m', '\033[38;5;226m', '\033[38;5;46m', '\033[38;5;93m', '\033[38;5;51m'
C6, C7, C8, C9, C10  = '\033[38;5;37m', '\033[38;5;250m', '\033[38;5;255m', '\033[38;5;208m', '\033[38;5;240m'
C11, C12, C13, C14, C15 = '\033[38;5;118m', '\033[38;5;18m', '\033[38;5;45m', '\033[38;5;165m', '\033[38;5;252m'
C16, C17, C18, C19, C20 = '\033[38;5;21m', '\033[38;5;203m', '\033[38;5;214m', '\033[38;5;28m', '\033[38;5;232m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE CONNECTED NODES (SANGHA)
# ==========================================
def sangha_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C1}         (O)---(O)---(O)
    {C1}          | \       / |
    {C5}          |  (SANGHA)  |
    {C5}          | /       \\ |
    {C1}         (O)---(O)---(O)
    {C13}       [ NETWORK SENTRY v4.3 ]
    """
    print(logo)
    print(f"{C1}{BLD}   SANGHA-NETWORK: REAL-TIME TRAFFIC FLOW INSPECTION{RST}\n")
    
    # Network handshake animation
    status_colors = [C1, C5, C13, C3]
    for i in range(12):
        color = status_colors[i % 4]
        sys.stdout.write(f"\r{C10}[{color}PULS{C10}] {C8}Listening on All Interfaces (Promiscuous Mode)...{RST}")
        sys.stdout.flush()
        time.sleep(0.1)
    print(f"\n{C3}[+] SPI Firewall Engine Synchronized with Network Stack.{RST}\n")

# ==========================================
# ARCHITECTURE: PACKET INSPECTION LOGIC
# ==========================================
class NetworkSentry:
    """Simulates a Network Intrusion Detection System (NIDS)."""
    def __init__(self):
        self.monitored_ips = ["192.168.1.50", "10.0.0.12"]
        self.threat_signatures = ["FTP_EXFIL", "CUI_STREAM", "TUNNEL_SSH"]

    def analyze_packet(self, src_ip, dst_ip, port, payload_size):
        """Heuristic analysis of a single network packet."""
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        
        # Check for High Volume Anomaly
        is_anomaly = payload_size > 1024 * 50 # 50KB per packet is suspicious for CUI
        
        # Identify Service
        service = self._get_service(port)
        
        # Visual Traffic Stream
        color = C17 if is_anomaly else C3
        print(f"{C10}[{C8}{timestamp}{C10}] {C5}{src_ip:<12} {C1}→ {C13}{dst_ip:<12} {C10}| {C15}PORT:{port:<4} {C7}SIZE:{C2}{payload_size:<6} {RST}")

        if is_anomaly:
            self._trigger_network_alert(src_ip, dst_ip, service, payload_size)

    def _get_service(self, port):
        services = {21: "FTP", 22: "SSH", 80: "HTTP", 443: "HTTPS", 3389: "RDP"}
        return services.get(port, "UNKNOWN")

    def _trigger_network_alert(self, src, dst, svc, size):
        print(f"\n{C17}{BLD}!!! NETWORK BREACH DETECTED: UNUSUAL DATA OUTFLOW !!!{RST}")
        print(f"{C17}│ {C8}SOURCE IP : {C5}{src}{RST}")
        print(f"{C17}│ {C8}TARGET IP : {C17}{dst} (OUTSIDE_ZONE){RST}")
        print(f"{C17}│ {C8}PROTOCOL  : {C2}{svc}{RST}")
        print(f"{C17}│ {C8}PAYLOAD   : {C17}{size} bytes / pkt{RST}")
        print(f"{C17}│ {C8}ACTION    : {C17}{BLD}TCP_RESET SENT | PACKET DROPPED{RST}")
        print(f"{C17}└{'─'*55}{RST}\n")
        time.sleep(0.5)

# ==========================================
# SIMULATION: LIVE PACKET SNIFFING
# ==========================================
def run_traffic_simulation():
    sangha_banner_anim()
    sentry = NetworkSentry()
    
    # Simulated Traffic Flow
    packets = [
        ("192.168.1.10", "192.168.1.50", 443, 1200),
        ("192.168.1.50", "8.8.8.8", 80, 500),
        ("10.0.0.12", "154.22.1.9", 21, 85000), # SUSPICIOUS FTP
        ("192.168.1.10", "192.168.1.11", 3389, 2500),
        ("192.168.1.50", "203.45.1.2", 443, 120000) # SUSPICIOUS HTTPS
    ]
    
    print(f"{C15}{BLD}ID   | TIMESTAMP    | FLOW DIRECTION      | PORT | SIZE   | VERDICT{RST}")
    print(f"{C10}{'━'*75}{RST}")
    
    for i, (src, dst, port, size) in enumerate(packets):
        time.sleep(secrets.randbelow(2) + 0.5)
        sentry.analyze_packet(src, dst, port, size)

if __name__ == "__main__":
    try:
        run_traffic_simulation()
        print(f"{C3}[✔] Sangha-Network monitoring stabilized. Buffer clean.{RST}")
    except KeyboardInterrupt:
        print(f"\n{C17}[!] Sniffer Offline.{RST}")