import os
import time
import sys

# ==========================================
# ASHRAMA-ROLES: COPPER HIERARCHY THEME
# ==========================================
COPPER = '\033[38;5;173m'
CRIMSON = '\033[38;5;160m'
GOLD = '\033[93m'
WHITE = '\033[97m'
BOLD = '\033[1m'
RST = '\033[0m'

# ==========================================
# ARCHITECTURE: DIRECTED ACYCLIC GRAPH (DAG)
# ==========================================

class RoleNode:
    """A single node in the IAM Graph representing a Role and its direct privileges."""
    def __init__(self, name, direct_privileges=None):
        self.name = name.upper()
        self.direct_privileges = set(direct_privileges) if direct_privileges else set()
        self.parents = [] # Roles that THIS role inherits FROM

    def inherit_from(self, parent_node):
        """Creates a Directed Edge in the graph."""
        if parent_node not in self.parents:
            self.parents.append(parent_node)

class AshramaIAMGraph:
    """
    The Core Engine. Manages the nodes and performs Graph Traversal 
    to calculate Effective Permissions.
    """
    def __init__(self):
        self.nodes = {}
        self._build_base_graph()

    def _build_base_graph(self):
        """Constructs the default Ashrama security hierarchy."""
        # 1. Create Nodes (Direct Permissions Only)
        self.nodes["GUEST"] = RoleNode("GUEST", ["read:public_data"])
        
        # Brahmacharya (Student/Analyst)
        self.nodes["BRAHMACHARYA"] = RoleNode("BRAHMACHARYA", ["read:cui_basic", "write:cui_basic"])
        
        # Grihastha (Householder/Manager)
        self.nodes["GRIHASTHA"] = RoleNode("GRIHASTHA", ["approve:cui_transfer", "delete:cui_basic"])
        
        # Vanaprastha (Retiree/Auditor)
        self.nodes["VANAPRASTHA"] = RoleNode("VANAPRASTHA", ["audit:system_logs", "read:cui_restricted"])
        
        # Sannyasa (Renunciate/Root Admin)
        self.nodes["SANNYASA"] = RoleNode("SANNYASA", ["grant:system_access", "destroy:network"])

        # 2. Build the Directed Edges (Inheritance)
        # Sannyasa inherits everything from Vanaprastha and Grihastha
        self.nodes["SANNYASA"].inherit_from(self.nodes["VANAPRASTHA"])
        self.nodes["SANNYASA"].inherit_from(self.nodes["GRIHASTHA"])
        
        # Vanaprastha and Grihastha both inherit from Brahmacharya
        self.nodes["VANAPRASTHA"].inherit_from(self.nodes["BRAHMACHARYA"])
        self.nodes["GRIHASTHA"].inherit_from(self.nodes["BRAHMACHARYA"])
        
        # Brahmacharya inherits from Guest
        self.nodes["BRAHMACHARYA"].inherit_from(self.nodes["GUEST"])

    def resolve_effective_permissions(self, role_name, visited=None, depth=0):
        """
        Uses Recursive Depth-First Search (DFS) to traverse the graph
        and collect all inherited privileges.
        """
        if visited is None:
            visited = set()

        role_name = role_name.upper()
        if role_name not in self.nodes:
            return set()

        node = self.nodes[role_name]
        
        # Prevent infinite loops in case of cyclic graph errors
        if node.name in visited:
            return set()
            
        visited.add(node.name)
        
        # Terminal aesthetic: Visualizing the Graph Traversal
        indent = "  " * depth
        time.sleep(0.2)
        print(f"{COPPER}{indent}↳ [GRAPH-TRACE] Traversing Node: {GOLD}{node.name}{RST}")

        # Start with this node's direct permissions
        effective_privs = set(node.direct_privileges)

        # Recursively visit all parent nodes and merge their permissions
        for parent in node.parents:
            effective_privs.update(
                self.resolve_effective_permissions(parent.name, visited, depth + 1)
            )

        return effective_privs

# ==========================================
# INTERACTIVE CLI SHELL
# ==========================================

iam_engine = AshramaIAMGraph()
users_db = {"raj": "SANNYASA", "shani": "GRIHASTHA", "rishab": "BRAHMACHARYA"}

def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = f"""{COPPER}{BOLD}
       ___        __                            
      / _ | ___  / /  _______ ___ _  ___ _      
     / __ |(_-< / _ \/ __/ _ `/  ' \/ _ `/      
    /_/ |_/___//_//_/_/  \_,_/_/_/_/\_,_/       
     {CRIMSON}R O L E   H I E R A R C H Y   E N G I N E{RST}
    """
    print(banner)
    print(f"{WHITE}>> ARCHITECTURE: DIRECTED ACYCLIC GRAPH (DAG){RST}")
    print(f"{WHITE}>> ALGORITHM: RECURSIVE DEPTH-FIRST SEARCH (DFS){RST}\n")

def cmd_help():
    print(f"\n{COPPER}{BOLD}--- ASHRAMA-ROLES: COMMANDS ---{RST}")
    print(f" {GOLD}users{RST}           : Show registered users and their base roles.")
    print(f" {GOLD}resolve <user>{RST}  : Calculate effective permissions using Graph Traversal.")
    print(f" {GOLD}graph{RST}           : Display the underlying DAG inheritance structure.")
    print(f" {GOLD}clear{RST}           : Wipe terminal screen.")
    print(f" {GOLD}exit{RST}            : Disconnect IAM Engine.")
    print(f"{COPPER}{'-'*31}{RST}")

def cmd_graph():
    print(f"\n{CRIMSON}{BOLD}[ THE ASHRAMA INHERITANCE DAG ]{RST}")
    print(f"{WHITE}SANNYASA (Root){RST}")
    print(f"{COPPER} ├── inherits -> {WHITE}VANAPRASTHA{RST}")
    print(f"{COPPER} │    └── inherits -> {WHITE}BRAHMACHARYA{RST}")
    print(f"{COPPER} │         └── inherits -> {WHITE}GUEST{RST}")
    print(f"{COPPER} └── inherits -> {WHITE}GRIHASTHA{RST}")
    print(f"{COPPER}      └── inherits -> {WHITE}BRAHMACHARYA{RST}")
    print(f"{COPPER}           └── inherits -> {WHITE}GUEST{RST}\n")

def run_shell():
    print_banner()
    while True:
        try:
            raw = input(f"{COPPER}iam{RST}@{CRIMSON}ashrama{RST}:{COPPER}~/roles{RST}$ ").strip().split()
            if not raw: continue
            
            cmd = raw[0].lower()
            args = raw[1:]

            if cmd == "help": cmd_help()
            elif cmd == "users":
                print(f"\n{WHITE}{BOLD}{'USER':<10} | {'BASE ROLE'}{RST}")
                print("-" * 25)
                for u, r in users_db.items(): print(f"{GOLD}{u:<10}{RST} | {r}")
                print()
            elif cmd == "graph": cmd_graph()
            elif cmd == "resolve":
                if not args or args[0].lower() not in users_db:
                    print(f"{CRIMSON}[!] Error: Provide a valid username (try 'users' command).{RST}")
                    continue
                
                target_user = args[0].lower()
                base_role = users_db[target_user]
                
                print(f"\n{WHITE}[*] Initiating DFS Graph Traversal for user '{target_user}'...{RST}")
                time.sleep(0.5)
                
                # Execute the Graph Algorithm
                privileges = iam_engine.resolve_effective_permissions(base_role)
                
                print(f"\n{GOLD}{BOLD}[+] TRAVERSAL COMPLETE. EFFECTIVE PERMISSIONS:{RST}")
                for priv in sorted(privileges):
                    print(f" {CRIMSON}• {WHITE}{priv}{RST}")
                print()
                
            elif cmd == "clear": print_banner()
            elif cmd == "exit": break
            else: print(f"{CRIMSON}[!] Unknown command. Type 'help'.{RST}")
        except Exception as e:
            print(f"{CRIMSON}[!] IAM Fault: {e}{RST}")

if __name__ == "__main__":
    run_shell()