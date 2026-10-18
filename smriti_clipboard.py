import os
import sys
import time
import secrets
import re
from datetime import datetime

# ==========================================
# SMRITI-CLIPBOARD: NEURAL MEMORY 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;33m', '\033[38;5;220m', '\033[38;5;244m', '\033[38;5;51m', '\033[38;5;255m'
C6, C7, C8, C9, C10  = '\033[38;5;93m', '\033[38;5;196m', '\033[38;5;46m', '\033[38;5;208m', '\033[38;5;232m'
C11, C12, C13, C14, C15 = '\033[38;5;147m', '\033[38;5;121m', '\033[38;5;18m', '\033[38;5;214m', '\033[38;5;60m'
C16, C17, C18, C19, C20 = '\033[38;5;37m', '\033[38;5;160m', '\033[38;5;27m', '\033[38;5;29m', '\033[38;5;252m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE NEURAL NETWORK (SMRITI)
# ==========================================
def smriti_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C1}          o---o---o
    {C1}         / \ / \ / \\
    {C4}        o---{C2}(S){C4}---o
    {C1}         \ / \ / \ /
    {C1}          o---o---o
    {C13}     [ MEMORY SENTRY v4.5 ]
    """
    print(logo)
    print(f"{C1}{BLD}   SMRITI-CLIPBOARD: UNAUTHORIZED COPY PROTECTION{RST}\n")
    
    # Pulse animation
    for i in range(12):
        sys.stdout.write(f"\r{C3}[{C9}SCAN{C3}] {C5}Monitoring RAM Clipboard Buffer... {C4}{'|/-\\'[i%4]}{RST}")
        sys.stdout.flush()
        time.sleep(0.1)
    print(f"\n{C8}[+] Ring-Fence Active. Real-time Buffer Scrubbing Enabled.{RST}\n")

# ==========================================
# ARCHITECTURE: CLIPBOARD SCRUBBER ENGINE
# ==========================================
class ClipboardSentry:
    """Simulates a secure clipboard manager for CUI protection."""
    def __init__(self):
        self.sensitive_patterns = [
            r"CUI//", r"CONFIDENTIAL", r"INTERNAL-ONLY", 
            r"PASS-", r"KEY-", r"\b\d{4}-\d{4}-\d{4}\b"
        ]
        self.virtual_clipboard = ""

    def copy_to_clipboard(self, content):
        """Simulates the 'Ctrl+C' action with inspection."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"{C3}[{timestamp}] {C5}Capture Event: User triggered COPY command.{RST}")
        
        is_sensitive = any(re.search(p, content, re.IGNORECASE) for p in self.sensitive_patterns)
        
        if is_sensitive:
            self._handle_sensitive_copy(content)
        else:
            self.virtual_clipboard = content
            print(f"{C8}[✔] ALLOWED: Non-sensitive data stored in buffer.{RST}\n")

    def _handle_sensitive_copy(self, content):
        """Logic for protecting sensitive data in the clipboard."""
        print(f"{C7}{BLD}!!! ALERT: SENSITIVE DATA DETECTED IN CLIPBOARD !!!{RST}")
        
        # Masking: Show only first 4 chars
        masked = content[:4] + "*" * (len(content) - 4)
        self.virtual_clipboard = masked
        
        print(f"{C7}│ {C5}ORIGINAL : {C10}{content}{RST}")
        print(f"{C7}│ {C2}MASKED   : {C2}{masked}{RST}")
        print(f"{C7}│ {C9}ACTION   : {C9}{BLD}AUTO-FLUSH SCHEDULED IN 5 SECONDS.{RST}")
        print(f"{C7}└{'─'*55}{RST}\n")
        
        # Simulate Auto-Flush
        time.sleep(2)
        print(f"{C15}[*] T-minus 3s to Memory Scrubbing...")
        time.sleep(2)
        self._flush_memory()

    def _flush_memory(self):
        """Overwrites the clipboard with random noise to prevent recovery."""
        noise = secrets.token_hex(16)
        self.virtual_clipboard = ""
        print(f"{C4}[✔] MEMORY SCRUBBED: Clipboard buffer cleared and randomized.{RST}\n")

# ==========================================
# SIMULATION: USER WORKFLOW
# ==========================================
def run_user_simulation():
    smriti_banner_anim()
    sentry = ClipboardSentry()
    
    workflow = [
        "Normal meeting notes for Project Alpha.",
        "CUI//NUCLEAR-SPECS-2026-VOID",
        "Lunch menu: Pizza and Coke",
        "INTERNAL-ONLY: Admin password is 'Smriti@123'"
    ]
    
    for item in workflow:
        time.sleep(1)
        sentry.copy_to_clipboard(item)

if __name__ == "__main__":
    try:
        run_user_simulation()
        print(f"{C8}[*] Smriti session complete. System RAM is clean.{RST}")
    except KeyboardInterrupt:
        print(f"\n{C7}[!] Watchdog Terminated.{RST}")