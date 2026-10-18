import os
import sys
import time
import secrets
import threading

# ==========================================
# SHILA-BLOCKER: MOUNTAIN MONOLITH 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;244m', '\033[38;5;236m', '\033[38;5;253m', '\033[38;5;255m', '\033[38;5;232m'
C6, C7, C8, C9, C10  = '\033[38;5;240m', '\033[38;5;238m', '\033[38;5;130m', '\033[38;5;220m', '\033[38;5;250m'
C11, C12, C13, C14, C15 = '\033[38;5;64m', '\033[38;5;112m', '\033[38;5;67m', '\033[38;5;178m', '\033[38;5;95m'
C16, C17, C18, C19, C20 = '\033[38;5;248m', '\033[38;5;160m', '\033[38;5;242m', '\033[38;5;15m', '\033[38;5;233m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE IMPREGENABLE MOUNTAIN
# ==========================================
def shila_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C2}           {C19}/\\
    {C2}          {C19}/  \\
    {C7}         {C1}/    \\{C7}
    {C7}    {C2}____/{C1}      \\{C2}____
    {C2}   /   {C10}S H I L A{C2}      \\
    {C2}  /__________________\\
    {C5}  [ BLOCKER v4.2 ACTIVE ]
    """
    print(logo)
    print(f"{C1}{BLD}   SHILA-BLOCKER: PERIPHERAL LOCKDOWN & USB SENTRY{RST}\n")
    
    # Secure mount-point scanning animation
    for i in range(12):
        sys.stdout.write(f"\r{C6}[{C9}{'#' * (i%4)}{C6}] {C13}Monitoring Hardware Bus (USB-C/3.0)...{RST}")
        sys.stdout.flush()
        time.sleep(0.1)
    print(f"\n{C11}[+] System-Level Peripheral Interceptor Initialized.{RST}\n")

# ==========================================
# ARCHITECTURE: HARDWARE WHITE-LISTING ENGINE
# ==========================================
class ShilaSentry:
    """Manages USB connection events and enforces white-list policies."""
    def __init__(self):
        # White-list of Authorized Device IDs (VID:PID)
        self.authorized_devices = {
            "0951:1666": "Kingston_Secure_Data",
            "0781:5581": "SanDisk_Ultra_CUI",
            "1038:12AD": "SteelSeries_Admin_Keyboard"
        }

    def process_connection_event(self, vid_pid, device_name):
        """Logic for approving or ejecting hardware devices."""
        print(f"{C10}[*] EVENT: New Peripheral Detected -> {C4}{device_name} ({vid_pid}){RST}")
        time.sleep(1)
        
        if vid_pid in self.authorized_devices:
            self._allow_device(vid_pid)
            return True
        else:
            self._block_device(vid_pid, device_name)
            return False

    def _allow_device(self, vid_pid):
        print(f"{C11}{BLD}[✔] ACCESS GRANTED: {self.authorized_devices[vid_pid]} is authorized.{RST}")
        print(f"{C11}│ Mount-Point: /media/secure_cui_drive{RST}\n")

    def _block_device(self, vid_pid, name):
        print(f"{C17}{BLD}!!! SECURITY BREACH: UNAUTHORIZED USB DETECTED !!!{RST}")
        print(f"{C17}│ DEVICE : {C4}{name}{RST}")
        print(f"{C17}│ VID:PID: {C17}{vid_pid}{RST}")
        print(f"{C17}│ ACTION : {C17}{BLD}I/O BUS DISCONNECTED | LOGGED TO PRITHVI-INCIDENT{RST}")
        print(f"{C17}└{'─'*55}{RST}\n")
        # In a real scenario, this would call 'udevadm' or 'devcon.exe' to disable the port
        time.sleep(0.5)

# ==========================================
# SIMULATION: HARDWARE BUS MONITORING
# ==========================================
def hardware_simulation():
    shila_banner_anim()
    sentry = ShilaSentry()
    
    # Simulated sequence of USB insertions
    sim_events = [
        ("0951:1666", "Kingston DataTraveler"),    # Authorized
        ("413C:2107", "Dell USB Optical Mouse"),   # Unauthorized/Generic
        ("1038:12AD", "SteelSeries Keyboard"),    # Authorized
        ("ABCD:1234", "Unknown 128GB Flash Drive") # Unauthorized/Attacker
    ]
    
    print(f"{C13}[!] SENTRY MODE: PERIPHERAL LOCKDOWN IS ON.{RST}\n")
    
    for vid_pid, name in sim_events:
        time.sleep(1.5) # Simulate physical insertion time
        sentry.process_connection_event(vid_pid, name)

if __name__ == "__main__":
    try:
        hardware_simulation()
        print(f"{C11}[*] Shila session stabilized. Port monitoring continues.{RST}")
    except KeyboardInterrupt:
        print(f"\n{C17}[!] Sentry Offline.{RST}")