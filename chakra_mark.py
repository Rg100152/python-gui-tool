import os
import time
import sys

# ==========================================
# TERMINAL COLOR PALETTE (ANSI ESCAPE CODES)
# ==========================================
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'
BOLD = '\033[1m'

# ==========================================
# CORE FUNCTIONS (FUNCTIONAL ARCHITECTURE)
# ==========================================

def clear_screen():
    """Clears the console for a clean terminal look."""
    os.system('cls' if os.name == 'nt' else 'clear')
    # Thonny shell hack to simulate clear screen
    print("\n" * 50)

def print_banner():
    """Displays the Chakra-Mark system banner."""
    banner = f"""{CYAN}{BOLD}
      ___ _         _                  __  __         _   
     / __| |_  __ _| |___ _ _ __ _ ___|  \/  |__ _ _ _| |__
    | (__| ' \/ _` | / / '_/ _` |___| |\/| / _` | '_| / /
     \___|_||_\__,_|_\_\_| \__,_|   |_|  |_\__,_|_| |_\_\
    {RESET}"""
    print(banner)
    print(f"{YELLOW}[*] SYSTEM: CHAKRA-MARK CUI INJECTOR{RESET}")
    print(f"{YELLOW}[*] ARCHITECTURE: FUNCTIONAL STATE-MACHINE{RESET}")
    print(f"{YELLOW}[*] STATUS: AWAITING OPERATOR INPUT{RESET}\n")

def slow_print(text, delay=0.03, color=RESET):
    """Simulates a teletype/hacker terminal output effect."""
    for char in text:
        sys.stdout.write(f"{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def generate_target_file(filename="intel_report.txt"):
    """Generates a dummy file if the target does not exist."""
    if not os.path.exists(filename):
        slow_print(f"[!] Target '{filename}' not found. Generating dummy payload...", 0.02, YELLOW)
        with open(filename, "w") as f:
            f.write("Operation details:\nTarget coordinates acquired.\nAwaiting further instruction.\n")
        slow_print(f"[+] Dummy file '{filename}' generated.", 0.02, GREEN)
    else:
        slow_print(f"[+] Target '{filename}' located and locked.", 0.02, GREEN)

def read_file_contents(filename):
    """Reads and displays the current file contents."""
    try:
        with open(filename, "r") as f:
            content = f.read()
        print(f"\n{CYAN}--- BEGIN FILE: {filename} ---{RESET}")
        print(content.strip())
        print(f"{CYAN}--- END FILE ---{RESET}\n")
    except FileNotFoundError:
        print(f"{RED}[-] Error: File not found.{RESET}")

def inject_cui_markers(filename, classification):
    """Injects the selected classification into the header and footer."""
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            
        # Clean existing markers to prevent duplication
        if lines and classification in lines[0]:
            slow_print("[-] File already marked with this classification. Aborting injection.", 0.02, RED)
            return

        # Prepare marker formatting
        marker = f"========== [ {classification.upper()} ] ==========\n"
        
        # Inject Header and Footer
        lines.insert(0, marker + "\n")
        lines.append("\n" + marker)
        
        with open(filename, "w") as f:
            f.writelines(lines)
            
        slow_print(f"[+] Injection successful. {classification} markers applied to Header and Footer.", 0.03, GREEN)
        
    except Exception as e:
        print(f"{RED}[-] Critical Error during injection: {e}{RESET}")

# ==========================================
# INTERACTIVE STATE-MACHINE (THE "CHAKRA" LOOP)
# ==========================================

def run_terminal_loop():
    """Main execution loop providing the user with an interactive menu."""
    target_file = "intel_report.txt"
    current_classification = "UNCLASSIFIED"
    
    clear_screen()
    print_banner()
    generate_target_file(target_file)
    time.sleep(1)
    
    while True:
        print(f"\n{BOLD}============== COMMAND MENU =============={RESET}")
        print(f" 1. Select Classification Level (Current: {RED}{current_classification}{RESET})")
        print(" 2. Execute Marker Injection")
        print(" 3. View Target File Contents")
        print(" 4. Reset Target File (Clear file)")
        print(" 5. Exit System")
        print(f"{BOLD}=========================================={RESET}")
        
        choice = input(f"{CYAN}root@chakra-mark:~# {RESET}")
        
        if choice == '1':
            print(f"\n{YELLOW}Select Sensitivity Level:{RESET}")
            print("  A. CUI//SP-PRVT (Controlled Unclassified Info)")
            print("  B. RESTRICTED")
            print("  C. TOP SECRET // NOFORN")
            sub_choice = input(f"{CYAN}Select (A/B/C): {RESET}").upper()
            
            if sub_choice == 'A': current_classification = "CUI//SP-PRVT"
            elif sub_choice == 'B': current_classification = "RESTRICTED"
            elif sub_choice == 'C': current_classification = "TOP SECRET // NOFORN"
            else: print(f"{RED}[-] Invalid selection.{RESET}")
            
        elif choice == '2':
            slow_print("[*] Initiating header/footer injection protocol...", 0.02, YELLOW)
            inject_cui_markers(target_file, current_classification)
            
        elif choice == '3':
            read_file_contents(target_file)
            
        elif choice == '4':
            slow_print("[!] Overwriting target file with base template...", 0.02, YELLOW)
            if os.path.exists(target_file): os.remove(target_file)
            generate_target_file(target_file)
            
        elif choice == '5':
            slow_print("[*] Terminating Chakra-Mark session. Disconnecting...", 0.04, RED)
            break
        else:
            print(f"{RED}[-] Unrecognized command. Try again.{RESET}")

# Trigger execution
if __name__ == "__main__":
    run_terminal_loop()