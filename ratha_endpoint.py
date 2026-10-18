import os
import sys
import time
import secrets
import threading
from datetime import datetime

# ==========================================
# RATHA-ENDPOINT: THE CHARIOT GUARD 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;244m', '\033[38;5;67m', '\033[38;5;130m', '\033[38;5;94m', '\033[38;5;196m'
C6, C7, C8, C9, C10  = '\033[38;5;252m', '\033[38;5;220m', '\033[38;5;52m', '\033[38;5;226m', '\033[38;5;39m'
C11, C12, C13, C14, C15 = '\033[38;5;160m', '\033[38;5;46m', '\033[38;5;18m', '\033[38;5;202m', '\033[38;5;240m'
C16, C17, C18, C19, C20 = '\033[38;5;232m', '\033[38;5;121m', '\033[38;5;170m', '\033[38;5;214m', '\033[38;5;233m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE PROTECTIVE CHARIOT (RATHA)
# ==========================================
def ratha_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C1}             _________
    {C1}            |_|_|_|_|_|
    {C3}         ____|_______|____
    {C4}        /  {C7}O{C4}           {C7}O{C4}  \\
    {C4}       |   {C5}[ RATHA ]{C4}     |
    {C15}     ___{C4}\\___________/{C15}___
    {C15}    ({C16} @ {C15})             ({C16} @ {C15})
    {C13}    [ ENDPOINT PROTECTION v4.9 ]
    """
    print(logo)
    print(f"{C1}{BLD}   RATHA-ENDPOINT: HOST-BASED INTRUSION PREVENTION{RST}\n")
    
    # Kernel-level initialization animation
    for i in range(12):
        sys.stdout.write(f"\r{C15}[{C12}OK{C15}] {C6}Hooking System Calls: {C10}SYS_READ, SYS_WRITE, SYS_EXEC... {C7}{'|/-\\'[i%4]}{RST}")
        sys.stdout.flush()
        time.sleep(0.1)
    print(f"\n{C12}[+] Host Intrusion Prevention System (HIPS) Active.{RST}\n")

# ==========================================
# ARCHITECTURE: ENDPOINT PROTECTION ENGINE
# ==========================================
class RathaHIPS:
    """Simulates Host-based protection by monitoring process and file activity."""
    def __init__(self):
        self.verified_processes = ["svchost.exe", "explorer.exe", "cui_tool.exe"]
        self.sensitive_dirs = ["C:\\CUI_Vault", "\\\\Internal_Server\\CUI"]
        self.incident_log = []

    def inspect_process_activity(self, pid, proc_name, target_file, action):
        """Analyzes every file I/O request on the endpoint."""
        ts = datetime.now().strftime("%H:%M:%S")
        
        # Policy Check: Is the process trusted to touch CUI?
        is_trusted = proc_name.lower() in self.verified_processes
        is_cui_path = any(d in target_file for d in self.sensitive_dirs)
        
        # Color coding based on risk
        risk_color = C12 if (is_trusted or not is_cui_path) else C11
        status = "VERIFIED" if (is_trusted or not is_cui_path) else "SUSPICIOUS"

        print(f"{C15}[{ts}] PID:{pid:<5} | PROC:{C10}{proc_name:<14}{RST} | ACTION:{C7}{action:<8}{RST} | STATE:{risk_color}{status}{RST}")

        if is_cui_path and not is_trusted:
            self._trigger_endpoint_lockdown(pid, proc_name, target_file)
            return False
        return True

    def _trigger_endpoint_lockdown(self, pid, name, path):
        """Terminates suspicious process and protects the memory buffer."""
        print(f"\n{C11}{BLD}!!! RATHA-ENDPOINT: UNAUTHORIZED CUI ACCESS INTERCEPTED !!!{RST}")
        print(f"{C11}│ {C6}VIOLATOR : {C10}{name} (PID: {pid}){RST}")
        print(f"{C11}│ {C6}TARGET   : {C14}{path}{RST}")
        print(f"{C11}│ {C6}POLICY   : {C1}Untrusted Application Access Denied{RST}")
        print(f"{C11}│ {C6}ACTION   : {C11}{BLD}PROCESS_KILLED | I/O_HANDLE_REVOKED | RAM_FLUSHED{RST}")
        print(f"{C11}└{'─'*55}{RST}\n")
        time.sleep(0.5)

# ==========================================
# SIMULATION: REAL-TIME ENDPOINT ACTIVITY
# ==========================================
def start_endpoint_monitor():
    ratha_banner_anim()
    hips = RathaHIPS()
    
    # Simulated Host Activity Log
    host_events = [
        (1024, "explorer.exe", "C:\\Users\\Raj\\Docs", "OPEN"),
        (4452, "cui_tool.exe", "C:\\CUI_Vault\\data.pdf", "READ"),    # Authorized
        (9920, "malware_script.py", "C:\\CUI_Vault\\pass.key", "READ"), # VIOLATION
        (1024, "explorer.exe", "C:\\Windows\\System32", "LIST"),
        (5501, "unknown_app.exe", "\\\\Internal_Server\\CUI\\spec.docx", "WRITE"), # VIOLATION
        (2201, "svchost.exe", "C:\\Windows\\Temp", "CLEANUP")
    ]
    
    print(f"{C13}[!] MONITORING LOCAL PROCESS BUS & SYSTEM CALLS...{RST}\n")
    
    for pid, proc, path, action in host_events:
        time.sleep(1.2)
        hips.inspect_process_activity(pid, proc, path, action)

if __name__ == "__main__":
    try:
        start_endpoint_monitor()
        print(f"{C12}[✔] Ratha-Endpoint session secure. Protection persists in background.{RST}")
    except KeyboardInterrupt:
        print(f"\n{C11}[!] HIPS Service Terminated.{RST}")
        