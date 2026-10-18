import os
import sys
import time
import binascii
from datetime import datetime

# ==========================================
# SUSHUM-PACKET: NEURAL FLOW 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;33m', '\033[38;5;226m', '\033[38;5;255m', '\033[38;5;240m', '\033[38;5;93m'
C6, C7, C8, C9, C10  = '\033[38;5;196m', '\033[38;5;46m', '\033[38;5;232m', '\033[38;5;51m', '\033[38;5;208m'
C11, C12, C13, C14, C15 = '\033[38;5;153m', '\033[38;5;18m', '\033[38;5;214m', '\033[38;5;250m', '\033[38;5;137m'
C16, C17, C18, C19, C20 = '\033[38;5;252m', '\033[38;5;124m', '\033[38;5;21m', '\033[38;5;215m', '\033[38;5;233m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE CENTRAL NERVE (SUSHUM)
# ==========================================
def sushum_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C1}          {C3} ||
    {C1}          {C3} ||     {C1}S U S H U M
    {C5}         /  \\    {C10}P A C K E T
    {C5}        | {C2}(O){C5} |   {C15}v5.9 [DEEP_INSPECTION]
    {C1}         \\  /
    {C1}          {C3} ||
    """
    print(logo)
    print(f"{C1}{BLD}   SUSHUM-PACKET: LAYER-7 CONTENT RECONSTRUCTION{RST}\n")
    
    # DPI Initialization
    for i in range(12):
        sys.stdout.write(f"\r{C4}[{C7}OK{C4}] {C9}Priming DPI Engine: {C15}Fragment_Buffer_{i+1}... {C2}{'|/-\\'[i%4]}{RST}")
        sys.stdout.flush()
        time.sleep(0.1)
    print(f"\n{C7}[+] Reassembly-Layer Active. Inspecting Central Flow Channel.{RST}\n")

# ==========================================
# ARCHITECTURE: PACKET RECONSTRUCTION ENGINE
# ==========================================
class SushumDPI:
    """Simulates Deep Packet Inspection at the Reassembly layer."""
    def __init__(self):
        self.sensitive_signatures = [b"CUI//SECRET", b"NUCLEAR_API", b"ADMIN_PASS"]
        self.packet_buffer = []

    def ingest_fragment(self, fragment_hex):
        """Converts hex fragments to raw bytes and reassembles."""
        try:
            raw_bytes = binascii.unhexlify(fragment_hex.replace(" ", ""))
            self.packet_buffer.append(raw_bytes)
            self._inspect_stream()
        except binascii.Error:
            print(f"{C6}[!] ERROR: Corrupt hex fragment detected.{RST}")

    def _inspect_stream(self):
        """Assembles fragments and looks for CUI signatures."""
        ts = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        full_stream = b"".join(self.packet_buffer)
        
        # Inspection Complexity: $O(n)$ where $n$ is stream length
        for sig in self.sensitive_signatures:
            if sig in full_stream:
                self._trigger_neural_block(ts, sig, full_stream)
                self.packet_buffer = [] # Clear buffer after alert
                return
        
        print(f"{C4}[{ts}] {C7}DPI_STREAM: {C15}{len(full_stream):<4} bytes reconstructed | Status: {C1}Flowing...{RST}")

    def _trigger_neural_block(self, ts, sig, raw):
        print(f"\n{C6}{BLD}!!! SUSHUM-PACKET: SENSITIVE DATA DETECTED IN STREAM !!!{RST}")
        print(f"{C6}│ {C3}TIME      : {C10}{ts}{RST}")
        print(f"{C6}│ {C3}SIGNATURE : {C6}{BLD}{sig.decode()}{RST}")
        print(f"{C6}│ {C3}RAW_HEX   : {C4}{binascii.hexlify(raw)[:40]}...{RST}")
        print(f"{C6}│ {C3}ACTION    : {C6}{BLD}STREAM_TERMINATED | BUFFER_PURGED | KERNEL_ALRT{RST}")
        print(f"{C6}└{'─'*55}{RST}\n")
        time.sleep(1)

# ==========================================
# SIMULATION: FRAGMENTED CUI EXFILTRATION
# ==========================================
def simulate_flow():
    sushum_banner_anim()
    dpi = SushumDPI()
    
    # Fragments of "CUI//SECRET_SPECS" in Hex
    fragments = [
        "43 55 49 2f 2f",       # CUI//
        "53 45 43 52 45 54",    # SECRET
        "5f 53 50 45 43 53"     # _SPECS
    ]
    
    print(f"{C13}[!] MONITORING RAW PACKET BUFFER (Sushumna Channel)...{RST}\n")
    
    # 1. Normal traffic
    dpi.ingest_fragment("48 65 6c 6c 6f") # Hello
    time.sleep(1.2)
    
    # 2. Fragmented Sensitive Traffic
    for i, frag in enumerate(fragments):
        print(f"{C9}[*] Incoming Fragment {i+1} received...{RST}")
        time.sleep(1.5)
        dpi.ingest_fragment(frag)

if __name__ == "__main__":
    try:
        simulate_flow()
        print(f"{C7}[✔] Sushum-Packet session stabilized. Neural path cleared.{RST}")
    except KeyboardInterrupt:
        print(f"\n{C6}[!] DPI Monitoring Halted.{RST}")