import ast
import os
import time
import sys

# ==========================================
# CHAKRAVYUH-SAST: CYBER-MATRIX THEME
# ==========================================
CYAN   = '\033[38;5;51m'   
VIOLET = '\033[38;5;93m'   
CRIM   = '\033[38;5;197m'  
AMBER  = '\033[38;5;214m'  
M_GRN  = '\033[38;5;46m'   
RST    = '\033[0m'
BLD    = '\033[1m'

# ==========================================
# 1. PAYLOAD GENERATOR (VULNERABLE CODE)
# ==========================================
def generate_vulnerable_target():
    """Generates a Python file containing hidden security vulnerabilities."""
    code = """
def secure_login(user_input):
    secret_key = "admin_super_password_123"  # VULN: Hardcoded Secret
    if user_input == secret_key:
        print("Logged in!")
        
def run_system_command(cmd):
    eval(cmd)  # VULN: Remote Code Execution (RCE)
    exec("import os; os.system(cmd)") # VULN: RCE
    
db_password = 'root' # VULN: Hardcoded Secret
"""
    with open("target_app.py", "w") as f:
        f.write(code)
    return "target_app.py"

# ==========================================
# 2. COMPILER-LEVEL AST VISITOR (THE ENGINE)
# ==========================================
class SecurityAuditor(ast.NodeVisitor):
    """
    Traverses the Abstract Syntax Tree (AST) of the target Python file.
    Does NOT run the code; mathematically analyzes its structure.
    """
    def __init__(self):
        self.vulnerabilities = []
        self.suspicious_vars = ['password', 'secret', 'key', 'token', 'api']

    def visit_Assign(self, node):
        """Triggered every time a variable is assigned (e.g., x = 10)."""
        # Looking for target = "string"
        for target in node.targets:
            if isinstance(target, ast.Name) and isinstance(node.value, ast.Constant):
                var_name = target.id.lower()
                # Check if variable name hints at a secret and value is a string
                if any(sec in var_name for sec in self.suspicious_vars) and isinstance(node.value.value, str):
                    self.vulnerabilities.append({
                        "type": "Hardcoded Secret",
                        "line": node.lineno,
                        "details": f"Variable '{target.id}' contains exposed string: '{node.value.value}'"
                    })
        self.generic_visit(node) # Continue traversing the tree

    def visit_Call(self, node):
        """Triggered every time a function is called (e.g., print())."""
        if isinstance(node.func, ast.Name):
            func_name = node.func.id
            if func_name in ['eval', 'exec']:
                self.vulnerabilities.append({
                    "type": "Arbitrary Code Execution (RCE)",
                    "line": node.lineno,
                    "details": f"Dangerous function '{func_name}()' detected. High risk of injection."
                })
        self.generic_visit(node)

# ==========================================
# 3. EXECUTION & UI MATRIX
# ==========================================
def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = f"""{VIOLET}{BLD}
     ╔═╗╦ ╦╔═╗╦╔═╦═╗╔═╗╦  ╦╦ ╦╦ ╦╦ ╦
     ║  ╠═╣╠═╣╠╩╗╠╦╝╠═╣╚╗╔╝╚╦╝║ ║║ ║
     ╚═╝╩ ╩╩ ╩╩ ╩╩╚═╩ ╩ ╚╝  ╩ ╚═╝╚═╝ {CYAN}S A S T{RST}
    """
    print(banner)
    print(f"{CYAN}>> ARCHITECTURE: ABSTRACT SYNTAX TREE (AST) PARSER{RST}")
    print(f"{CYAN}>> TARGET: STATIC APPLICATION SECURITY TESTING{RST}\n")

def analyze_target(filepath):
    print(f"{VIOLET}[*] Initiating AST Compilation for: {filepath}{RST}")
    time.sleep(0.5)
    
    with open(filepath, "r") as source:
        tree = ast.parse(source.read())
        
    print(f"{M_GRN}[+] Source compiled to memory map successfully.{RST}")
    print(f"{VIOLET}[*] Deploying NodeVisitor to traverse compiler tree...{RST}\n")
    time.sleep(1)
    
    auditor = SecurityAuditor()
    auditor.visit(tree) # This triggers the magical AST traversal
    
    # Render Results
    print(f"{CYAN}{BLD}┌──[ CHAKRAVYUH AUDIT REPORT ]{'─'*30}{RST}")
    if not auditor.vulnerabilities:
        print(f"{CYAN}│ {M_GRN}No security flaws detected at AST level.{RST}")
    else:
        for vuln in auditor.vulnerabilities:
            color = CRIM if "RCE" in vuln['type'] else AMBER
            print(f"{CYAN}│ {RST}Line {vuln['line']:<3} : {color}{BLD}[{vuln['type']}]{RST}")
            print(f"{CYAN}│ {RST}        {vuln['details']}")
            print(f"{CYAN}├{'─'*58}{RST}")
            time.sleep(0.2)
            
    print(f"{CYAN}└──[ EOF ]{'─'*50}{RST}\n")

if __name__ == "__main__":
    print_banner()
    target_file = generate_vulnerable_target()
    analyze_target(target_file)