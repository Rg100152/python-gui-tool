import os
import time
from datetime import datetime

# ==========================================
# KARUNA-ENFORCE: THE EMERALD GUARDIAN THEME
# ==========================================
EMERALD = '\033[38;5;48m'
FOREST = '\033[38;5;34m'
WHITE = '\033[97m'
BOLD = '\033[1m'
RST = '\033[0m'
RED = '\033[91m'
YLW = '\033[93m'

# ==========================================
# SECURITY KERNEL & CUSTOM EXCEPTIONS
# ==========================================

class SecurityViolation(Exception):
    """Triggered when a granular permission check fails."""
    pass

class KarunaSentinel:
    """
    The Sentinel Proxy: Acts as a gatekeeper for file operations.
    Implements Granular Permission Enforcement.
    """
    def __init__(self):
        # Permissions Matrix: { 'Filename': { 'Role': ['PERMS'] } }
        self._acl_matrix = {
            "cui_blueprint.pdf": {"ANALYST": ["READ"], "ADMIN": ["READ", "WRITE", "DELETE"]},
            "financial_audit.xlsx": {"AUDITOR": ["READ"], "ADMIN": ["READ", "WRITE"]},
            "system_logs.db": {"GUEST": [], "ADMIN": ["READ"]}
        }
        self.current_session_role = "GUEST"

    def set_session_role(self, role):
        self.current_session_role = role.upper()
        self._trace_call(f"Session Privilege Level Escalated to: {self.current_session_role}")

    def _trace_call(self, action):
        """Simulates kernel-level system call tracing."""
        ts = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        print(f"{FOREST}[TRACE_{ts}] >> {WHITE}{action}{RST}")
        time.sleep(0.2)

    def request_access(self, resource, operation):
        """
        The Granular Enforcement Logic.
        Checks if the current role has the specific operation right for the resource.
        """
        self._trace_call(f"Intercepting {operation} request for {resource}...")
        
        # Check if resource exists in ACL
        if resource not in self._acl_matrix:
            self._trace_call("Resource unknown. Defaulting to DENY-ALL.")
            return False

        allowed_ops = self._acl_matrix[resource].get(self.current_session_role, [])
        
        if operation.upper() in allowed_ops:
            self._trace_call(f"Permission Match: {operation} authorized for {self.current_session_role}.")
            return True
        else:
            self._trace_call(f"Permission Mismatch: {self.current_session_role} lacks {operation} rights.")
            return False

# ==========================================
# COMMAND MODULES
# ==========================================

guard = KarunaSentinel()

def cmd_help():
    print(f"\n{WHITE}{BOLD}--- KARUNA-ENFORCE: SENTINEL COMMANDS ---{RST}")
    print(f" {EMERALD}set-role <role>{RST}    : Set identity (ADMIN, ANALYST, AUDITOR, GUEST)")
    print(f" {EMERALD}list-files{RST}        : List managed CUI resources")
    print(f" {EMERALD}access <file> <op>{RST} : Attempt an operation (READ, WRITE, DELETE)")
    print(f" {EMERALD}help{RST}               : View this manual")
    print(f" {EMERALD}exit{RST}               : Shutdown security kernel")
    print(f"{WHITE}{'-'*40}{RST}")

def cmd_access(args):
    if len(args) < 2:
        print(f"{RED}[!] Usage: access <filename> <operation>{RST}")
        return
    
    file, op = args[0], args[1].upper()
    
    print(f"\n{EMERALD}{BOLD}[I/O GATEKEEPER]{RST} Processing Request...")
    if guard.request_access(file, op):
        print(f"{EMERALD}{BOLD}[✔] ACCESS GRANTED.{RST} Initializing {op} stream on {file}.\n")
    else:
        print(f"{RED}{BOLD}[✘] ACCESS DENIED.{RST} Security Violation Logged for {file}.\n")

# ==========================================
# INTERACTIVE KERNEL SHELL
# ==========================================

def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = f"""{EMERALD}{BOLD}
    ██╗  ██╗ █████╗ ██████╗ ██╗   ██╗███╗   ██╗ █████╗ 
    ██║ ██╔╝██╔══██╗██╔══██╗██║   ██║████╗  ██║██╔══██╗
    █████╔╝ ███████║██████╔╝██║   ██║██╔██╗ ██║███████║
    ██╔═██╗ ██╔══██║██╔══██╗██║   ██║██║╚██╗██║██╔══██║
    ██║  ██╗██║  ██║██║  ██║╚██████╔╝██║ ╚████║██║  ██║
    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝ {WHITE}E N F O R C E{RST}
    """
    print(banner)
    print(f"{WHITE}>> ARCHITECTURE: SENTINEL PROXY / GRANULAR PERMISSION KERNEL{RST}")
    print(f"{WHITE}>> SESSION: {guard.current_session_role} PRIVILEGES ACTIVE{RST}\n")

def run_kernel():
    print_banner()
    while True:
        try:
            prompt = f"{FOREST}karuna{RST}@{WHITE}guardian{RST}:{EMERALD}~/kernel{RST}# "
            raw = input(prompt).strip().split()
            if not raw: continue
            
            cmd = raw[0].lower()
            args = raw[1:]

            if cmd == "help":
                cmd_help()
            elif cmd == "set-role":
                if args: guard.set_session_role(args[0])
                else: print(f"{RED}[!] Role required.{RST}")
            elif cmd == "list-files":
                print(f"\n{WHITE}Managed CUI Files:{RST}")
                for f in guard._acl_matrix.keys(): print(f" - {f}")
                print("")
            elif cmd == "access":
                cmd_access(args)
            elif cmd == "exit":
                print(f"{FOREST}[*] Security kernel flushing buffers... Goodbye.{RST}")
                break
            else:
                print(f"{RED}[!] Signal '{cmd}' not recognized by kernel.{RST}")
        except Exception as e:
            print(f"{RED}[!] Kernel Panic: {e}{RST}")

if __name__ == "__main__":
    run_kernel()