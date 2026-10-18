import os
import time
import sys

# ==========================================
# CHAKRA-MAPPER: SOLAR TERMINAL THEME
# ==========================================
ORANGE = '\033[38;5;208m'
BLUE = '\033[94m'
BOLD = '\033[1m'
RST = '\033[0m'
GRN = '\033[92m'
RED = '\033[91m'

# ==========================================
# COMMAND REGISTRY (CLOSURE ARCHITECTURE)
# ==========================================
# This dictionary stores our "Chakra" commands.
COMMAND_REGISTRY = {}

def register_command(name, description):
    """A decorator-style closure to register system commands."""
    def wrapper(func):
        COMMAND_REGISTRY[name] = {"func": func, "help": description}
        return func
    return wrapper

# ==========================================
# SYSTEM CORE LOGIC & MAPPING DATA
# ==========================================
# Mapping CUI categories to sensitivity levels
CATEGORY_MAP = {
    "FIN": "CUI//FINANCIAL - Level 3 Protection",
    "TEC": "CUI//TECHNICAL - Level 4 Protection",
    "LEG": "CUI//LEGAL - Level 2 Protection",
    "PII": "CUI//PRIVACY - Level 5 Protection"
}

# ==========================================
# REGISTERED COMMANDS
# ==========================================

@register_command("help", "Displays the command reference guide.")
def cmd_help(args):
    print(f"\n{ORANGE}{BOLD}--- CHAKRA-MAPPER COMMAND REFERENCE ---{RST}")
    for cmd, info in COMMAND_REGISTRY.items():
        print(f" {BLUE}{cmd:<10}{RST} : {info['help']}")
    print(f"{ORANGE}{'-'*40}{RST}")

@register_command("ls-cat", "Lists all available CUI mapping categories.")
def cmd_list_categories(args):
    print(f"\n{BLUE}[*] Available Mapping Schema:{RST}")
    for code, desc in CATEGORY_MAP.items():
        print(f" {ORANGE}{code}{RST} -> {desc}")

@register_command("map", "Maps a file to a category. Usage: map <file> <cat>")
def cmd_map_file(args):
    if len(args) < 2:
        print(f"{RED}[-] Error: Missing arguments. Use: map <filename> <category_code>{RST}")
        return
    
    filename, cat_code = args[0], args[1].upper()
    
    if cat_code not in CATEGORY_MAP:
        print(f"{RED}[-] Error: Invalid category code '{cat_code}'. Run 'ls-cat' for list.{RST}")
        return

    print(f"{BLUE}[*] Indexing {filename}...{RST}")
    time.sleep(0.6)
    print(f"{GRN}[+] SUCCESS: {filename} mapped to {CATEGORY_MAP[cat_code]}{RST}")

@register_command("status", "Check system link and environment health.")
def cmd_status(args):
    print(f"{BLUE}[*] SYSTEM STATUS: {GRN}OPTIMAL{RST}")
    print(f"{BLUE}[*] KERNEL: CHAKRA-MAPPER v1.0{RST}")
    print(f"{BLUE}[*] TARGET PATH: {os.getcwd()}{RST}")

@register_command("exit", "Gracefully terminates the Chakra session.")
def cmd_exit(args):
    print(f"{ORANGE}[!] Closing Chakra-Mapper shell. Disconnecting...{RST}")
    sys.exit()

# ==========================================
# SHELL INTERFACE & EXECUTION
# ==========================================

def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = f"""{ORANGE}{BOLD}
      ____ _           _                    
     / ___| |__   __ _| | ___ __ __ _      
    | |   | '_ \ / _` | |/ / '__/ _` |     
    | |___| | | | (_| |   <| | | (_| |     
     \____|_| |_|\__,_|_|\_\_|  \__,_|     
     {BLUE}M A P P E R   S Y S T E M   v 1 . 0{RST}
    """
    print(banner)
    print(f"{BLUE}>> STYLE: CLOSURE-BASED COMMAND REGISTRY{RST}")
    print(f"{BLUE}>> Ready for operator input. Type 'help' to begin.{RST}\n")

def run_shell():
    print_banner()
    
    while True:
        try:
            # Prompt looking like a Linux terminal
            user_input = input(f"{ORANGE}chakra@root{RST}:{BLUE}~/mapper{RST}# ").strip().split()
            
            if not user_input:
                continue
                
            command = user_input[0].lower()
            arguments = user_input[1:]
            
            if command in COMMAND_REGISTRY:
                # Execute the function associated with the command
                COMMAND_REGISTRY[command]["func"](arguments)
            else:
                print(f"{RED}[-] Unknown command: '{command}'. Type 'help' for assistance.{RST}")
                
        except KeyboardInterrupt:
            print("\n")
            cmd_exit(None)

if __name__ == "__main__":
    run_shell()