import sqlite3
import os
import time
import sys

# ==========================================
# MAITRI-ACCESS: THE CITADEL THEME
# ==========================================
PURPLE = '\033[38;5;141m'
WHITE = '\033[97m'
BOLD = '\033[1m'
RST = '\033[0m'
GRN = '\033[92m'
RED = '\033[91m'
YLW = '\033[93m'

# ==========================================
# DATABASE REPOSITORY ARCHITECTURE
# ==========================================

class AccessVault:
    """Handles all SQL transactions and data persistence."""
    def __init__(self, db_name="maitri_vault.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._initialize_schema()

    def _initialize_schema(self):
        """Creates the RBAC structure if it doesn't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS roles (
                id INTEGER PRIMARY KEY,
                role_name TEXT UNIQUE,
                clearance_level INTEGER
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE,
                role_id INTEGER,
                FOREIGN KEY(role_id) REFERENCES roles(id)
            )
        """)
        # Seed default roles
        roles = [('ADMIN', 5), ('ANALYST', 3), ('AUDITOR', 2), ('GUEST', 1)]
        self.cursor.executemany("INSERT OR IGNORE INTO roles (role_name, clearance_level) VALUES (?, ?)", roles)
        self.conn.commit()

    def add_user(self, username, role_name):
        try:
            self.cursor.execute("SELECT id FROM roles WHERE role_name = ?", (role_name.upper(),))
            role_id = self.cursor.fetchone()
            if not role_id:
                return False, f"Role {role_name} not found."
            
            self.cursor.execute("INSERT INTO users (username, role_id) VALUES (?, ?)", (username.lower(), role_id[0]))
            self.conn.commit()
            return True, f"User {username} successfully registered in Citadel."
        except sqlite3.IntegrityError:
            return False, "User already exists in the database."

    def get_users(self):
        self.cursor.execute("""
            SELECT users.username, roles.role_name, roles.clearance_level 
            FROM users 
            JOIN roles ON users.role_id = roles.id
        """)
        return self.cursor.fetchall()

    def check_access(self, username, required_level):
        self.cursor.execute("""
            SELECT roles.clearance_level FROM users 
            JOIN roles ON users.role_id = roles.id 
            WHERE users.username = ?
        """, (username.lower(),))
        result = self.cursor.fetchone()
        if result:
            return result[0] >= required_level
        return None

# ==========================================
# SYSTEM CORE & COMMANDS
# ==========================================

vault = AccessVault()

def log_transaction(msg, type="INFO"):
    colors = {"INFO": PURPLE, "SUCCESS": GRN, "FAIL": RED, "WARN": YLW}
    c = colors.get(type, WHITE)
    print(f"{c}[{type}] {msg}{RST}")
    time.sleep(0.3)

def cmd_help():
    print(f"\n{WHITE}{BOLD}--- MAITRI-ACCESS COMMAND MANUAL ---{RST}")
    print(f" {PURPLE}adduser <name> <role>{RST} : Register a new entity (Roles: ADMIN, ANALYST, AUDITOR)")
    print(f" {PURPLE}list{RST}                 : Display all registered entities in the vault")
    print(f" {PURPLE}verify <name> <lvl>{RST}  : Test if a user has access to a CUI Level (1-5)")
    print(f" {PURPLE}clear{RST}                : Wipe the terminal screen")
    print(f" {PURPLE}help{RST}                 : Show this manual")
    print(f" {PURPLE}exit{RST}                 : Securely disconnect from database")
    print(f"{WHITE}{'-'*38}{RST}")

def cmd_add_user(args):
    if len(args) < 2:
        log_transaction("Usage: adduser <username> <role>", "FAIL")
        return
    success, msg = vault.add_user(args[0], args[1])
    log_transaction(msg, "SUCCESS" if success else "FAIL")

def cmd_list():
    users = vault.get_users()
    print(f"\n{BOLD}{WHITE}{'IDENTITY':<15} | {'ROLE':<10} | {'CLEARANCE'}{RST}")
    print("-" * 40)
    for u, r, l in users:
        print(f"{u:<15} | {r:<10} | Lvl {l}")
    print("-" * 40)

def cmd_verify(args):
    if len(args) < 2:
        log_transaction("Usage: verify <username> <required_level>", "FAIL")
        return
    username, level = args[0], int(args[1])
    access = vault.check_access(username, level)
    
    if access is True:
        log_transaction(f"ACCESS GRANTED: User {username} meets CUI Level {level} criteria.", "SUCCESS")
    elif access is False:
        log_transaction(f"ACCESS DENIED: Insufficient clearance for User {username}.", "FAIL")
    else:
        log_transaction(f"ACCESS ERROR: Identity {username} not found in database.", "WARN")

# ==========================================
# TERMINAL SHELL
# ==========================================

def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = f"""{PURPLE}{BOLD}
    ███╗   ███╗ █████╗ ██╗████████╗██████╗ ██╗
    ████╗ ████║██╔══██╗██║╚══██╔══╝██╔══██╗██║
    ██╔████╔██║███████║██║   ██║   ██████╔╝██║
    ██║╚██╔╝██║██╔══██║██║   ██║   ██╔══██╗██║
    ██║ ╚═╝ ██║██║  ██║██║   ██║   ██║  ██║██║
    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝ {WHITE}A C C E S S{RST}
    """
    print(banner)
    print(f"{WHITE}>> ARCHITECTURE: REPOSITORY PATTERN / SQLITE3 PERSISTENCE{RST}")
    print(f"{WHITE}>> DATABASE: maitri_vault.db (ACTIVE){RST}\n")

def run_shell():
    print_banner()
    while True:
        try:
            raw = input(f"{PURPLE}maitri{RST}@{WHITE}citadel{RST}:{PURPLE}~/access{RST}$ ").strip().split()
            if not raw: continue
            
            cmd = raw[0].lower()
            args = raw[1:]

            if cmd == "help": cmd_help()
            elif cmd == "adduser": cmd_add_user(args)
            elif cmd == "list": cmd_list()
            elif cmd == "verify": cmd_verify(args)
            elif cmd == "clear": print_banner()
            elif cmd == "exit": 
                log_transaction("Closing database connection. Goodbye.", "INFO")
                break
            else:
                log_transaction(f"Command '{cmd}' not recognized.", "FAIL")
        except Exception as e:
            log_transaction(f"System Error: {e}", "FAIL")

if __name__ == "__main__":
    run_shell()