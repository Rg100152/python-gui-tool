import os
import time
import secrets
import hashlib
from abc import ABC, abstractmethod

# ==========================================
# NAMASTE-AUTH: THE SAFFRON GUARDIAN THEME
# ==========================================
SAFFRON = '\033[38;5;208m'
GOLD = '\033[93m'
WHITE = '\033[97m'
BOLD = '\033[1m'
RST = '\033[0m'
RED = '\033[91m'
CYAN = '\033[96m'

# ==========================================
# ARCHITECTURE: STRATEGY PATTERN & METACLASS
# ==========================================

class AuthMeta(type):
    """Metaclass that automatically registers authentication strategies."""
    def __init__(cls, name, bases, nmspc):
        super(AuthMeta, cls).__init__(name, bases, nmspc)
        if not hasattr(cls, 'registry'):
            cls.registry = {}
        if name != "AuthStrategy":
            cls.registry[name.replace("Auth", "").lower()] = cls

class AuthStrategy(metaclass=AuthMeta):
    """Abstract Strategy base for different authentication methods."""
    @abstractmethod
    def authenticate(self, credential):
        pass

# --- CONCRETE STRATEGIES ---

class PasswordAuth(AuthStrategy):
    def authenticate(self, cred):
        # Simulated logic: checking against a hashed shadow file
        return cred == "admin123"

class TokenAuth(AuthStrategy):
    def authenticate(self, cred):
        # Simulated logic: checking for a 16-character hex token
        return len(cred) == 16 and all(c in "0123456789abcdef" for c in cred)

# ==========================================
# CORE SESSION MANAGER
# ==========================================

class SessionManager:
    """Handles the lifecycle of authenticated clearance tokens."""
    def __init__(self):
        self.active_session = None
        self.clearance_level = 0
        self.token = None

    def create_session(self, user, level):
        self.active_session = user
        self.clearance_level = level
        self.token = secrets.token_hex(8)
        self._log(f"Session established for {user}. Token issued: {self.token}", "SUCCESS")

    def destroy_session(self):
        self.active_session = None
        self.clearance_level = 0
        self.token = None
        self._log("Session terminated. Clearance revoked.", "WARN")

    def _log(self, msg, type="INFO"):
        colors = {"INFO": CYAN, "SUCCESS": GOLD, "WARN": SAFFRON}
        c = colors.get(type, WHITE)
        print(f"{c}[{type}] {msg}{RST}")

# ==========================================
# COMMAND MODULES
# ==========================================

session = SessionManager()

def cmd_help():
    """Detailed help guide for the Namaste-Auth system."""
    print(f"\n{SAFFRON}{BOLD}--- NAMASTE-AUTH: COMMAND REFERENCE GUIDE ---{RST}")
    print(f" {GOLD}login <method> <cred>{RST} : Authenticate using a strategy.")
    print(f"                             Methods: {WHITE}password, token{RST}")
    print(f"                             Example: {WHITE}login password admin123{RST}")
    print(f" {GOLD}whoami{RST}               : Check current session identity and token.")
    print(f" {GOLD}logout{RST}               : Clear current session data.")
    print(f" {GOLD}clearance{RST}            : View current CUI clearance level status.")
    print(f" {GOLD}help{RST}                 : Display this help guide.")
    print(f" {GOLD}exit{RST}                 : Shutdown the authentication gateway.")
    print(f"{SAFFRON}{'-'*45}{RST}")

def cmd_login(args):
    if len(args) < 2:
        print(f"{RED}[!] Usage: login <method> <credential>{RST}")
        return
    
    method, cred = args[0].lower(), args[1]
    
    if method in AuthStrategy.registry:
        strategy = AuthStrategy.registry[method]()
        print(f"{CYAN}[*] Attempting authentication via {method.upper()} provider...{RST}")
        time.sleep(0.8)
        
        if strategy.authenticate(cred):
            # Assigning clearance levels based on method
            lvl = 5 if method == "password" else 3
            session.create_session("ROOT_USER", lvl)
        else:
            print(f"{RED}[✘] AUTHENTICATION FAILED: Invalid credentials.{RST}")
    else:
        print(f"{RED}[!] Error: Unknown provider '{method}'.{RST}")

def cmd_whoami():
    if session.active_session:
        print(f"\n{GOLD}{BOLD}ACTIVE IDENTITY:{RST} {WHITE}{session.active_session}{RST}")
        print(f"{GOLD}{BOLD}SESSION TOKEN:  {RST} {CYAN}{session.token}{RST}")
        print(f"{GOLD}{BOLD}CLEARANCE:      {RST} {SAFFRON}LEVEL {session.clearance_level}{RST}\n")
    else:
        print(f"{RED}[!] No active session. Please login.{RST}")

# ==========================================
# INTERACTIVE GATEWAY SHELL
# ==========================================

def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = f"""{SAFFRON}{BOLD}
    ███╗   ██╗ █████╗ ███╗   ███╗ █████╗ ███████╗████████╗███████╗
    ████╗  ██║██╔══██╗████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝
    ██╔██╗ ██║███████║██╔████╔██║███████║███████╗   ██║   █████╗  
    ██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  
    ██║ ╚████║██║  ██║██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗
    ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝ {GOLD}AUTH{RST}
    """
    print(banner)
    print(f"{WHITE}>> ARCHITECTURE: STRATEGY PATTERN / METACLASS REGISTRY{RST}")
    print(f"{WHITE}>> PROTOCOL: SECURE CLEARANCE VERIFICATION GATEWAY{RST}\n")

def run_gateway():
    print_banner()
    while True:
        try:
            prompt = f"{SAFFRON}namaste{RST}@{GOLD}guardian{RST}:{SAFFRON}~/auth{RST}$ "
            raw = input(prompt).strip().split()
            if not raw: continue
            
            cmd = raw[0].lower()
            args = raw[1:]

            if cmd == "help": cmd_help()
            elif cmd == "login": cmd_login(args)
            elif cmd == "whoami": cmd_whoami()
            elif cmd == "logout": session.destroy_session()
            elif cmd == "clearance": 
                status = "AUTHORIZED" if session.clearance_level > 0 else "RESTRICTED"
                print(f"{CYAN}[*] Clearance Status: {SAFFRON}{status} (Level {session.clearance_level}){RST}")
            elif cmd == "exit":
                print(f"{SAFFRON}[*] Shutting down gateway... Namaste.{RST}")
                break
            else:
                print(f"{RED}[!] Unknown command: '{cmd}'. Type 'help' for manual.{RST}")
        except Exception as e:
            print(f"{RED}[!] Gateway Error: {e}{RST}")

if __name__ == "__main__":
    run_gateway()