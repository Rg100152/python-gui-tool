import os
import sys
import time
import secrets
from datetime import datetime

# ==========================================
# DIPA-PRINT: LUMINESCENT INK 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;226m', '\033[38;5;20m', '\033[38;5;232m', '\033[38;5;196m', '\033[38;5;244m'
C6, C7, C8, C9, C10  = '\033[38;5;255m', '\033[38;5;51m', '\033[38;5;93m', '\033[38;5;46m', '\033[38;5;214m'
C11, C12, C13, C14, C15 = '\033[38;5;39m', '\033[38;5;121m', '\033[38;5;18m', '\033[38;5;160m', '\033[38;5;60m'
C16, C17, C18, C19, C20 = '\033[38;5;37m', '\033[38;5;124m', '\033[38;5;28m', '\033[38;5;250m', '\033[38;5;233m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE ILLUMINATED PRINTER (DIPA)
# ==========================================
def dipa_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C1}           _______
    {C1}          /      /|
    {C7}         /______/ |
    {C7}         |      | |
    {C10}         |  {C1}*{C10}   | /
    {C10}         |______|/
    {C11}    [ PRINT SENTINEL v4.6 ]
    """
    print(logo)
    print(f"{C1}{BLD}   DIPA-PRINT: SECURE WATERMARKING & SPOOLER CONTROL{RST}\n")
    
    # Paper feeding animation
    for i in range(10):
        sys.stdout.write(f"\r{C5}[{C9}OK{C5}] {C6}Feeding Page {i+1}/10 into Secure Spooler... {C7}>>>{RST}")
        sys.stdout.flush()
        time.sleep(0.1)
    print(f"\n{C9}[+] Laser Integrity Check Passed. Watermark Engine Online.{RST}\n")

# ==========================================
# ARCHITECTURE: PRINT CONTROL ENGINE
# ==========================================
class PrintSentry:
    """Manages document printing rights and enforces watermarking."""
    def __init__(self):
        self.restricted_tags = ["CUI", "SECRET", "CONFIDENTIAL", "RESTRICTED"]

    def intercept_job(self, doc_name, user_id, content):
        """Intercepts a print job and applies security policies."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{C11}[*] Intercepting Job: {C6}'{doc_name}'{RST} from User: {C10}{user_id}{RST}")
        time.sleep(1)

        # 1. Content Inspection
        is_restricted = any(tag in content.upper() for tag in self.restricted_tags)
        
        if is_restricted:
            self._deny_print(doc_name, user_id)
            return False
        else:
            self._approve_and_watermark(doc_name, user_id, timestamp)
            return True

    def _approve_and_watermark(self, doc, user, ts):
        """Applies dynamic watermarking before 'printing'."""
        watermark_id = f"DIPA-{secrets.token_hex(4).upper()}"
        print(f"{C9}{BLD}✔ PRINT APPROVED. Applying Forensic Watermark...{RST}")
        print(f"{C5}┌─────────────────────────────────────────────────────┐")
        print(f"{C5}│ {C6}DOCUMENT  : {doc:<30}      {C5}│")
        print(f"{C5}│ {C6}USER      : {user:<30}      {C5}│")
        print(f"{C5}│ {C1}WATERMARK : {C1}{BLD}{watermark_id:<30}{RST}      {C5}│")
        print(f"{C5}│ {C10}TIMESTAMP : {ts:<30}      {C5}│")
        print(f"{C5}└─────────────────────────────────────────────────────┘{RST}")
        print(f"{C12}[*] Status: Sent to Physical Printer Service.{RST}\n")

    def _deny_print(self, doc, user):
        print(f"{C4}{BLD}!!! SECURITY VIOLATION: PRINT BLOCKED !!!{RST}")
        print(f"{C4}│ {C6}REASON: {RST}Document contains Restricted CUI Metadata.")
        print(f"{C4}│ {C6}TARGET: {RST}{doc}")
        print(f"{C4}│ {C6}USER  : {RST}{user}")
        print(f"{C4}└{'─'*55}{RST}\n")

# ==========================================
# SIMULATION: PRINT QUEUE
# ==========================================
def run_print_simulation():
    dipa_banner_anim()
    sentry = PrintSentry()
    
    queue = [
        ("Project_Alpha_Memo.txt", "Raj_G", "This is a regular project update."),
        ("CUI_Nuclear_Draft.pdf", "Guest_X", "Highly CUI Restricted nuclear specifications."),
        ("Staff_Meeting_Notes.docx", "Shani_V", "Discussion on library updates."),
        ("CONFIDENTIAL_Sutra.txt", "Admin_R", "The confidential sutra of the backend.")
    ]
    
    print(f"{C8}[!] MONITORING SYSTEM PRINT SPOOLER (LPT1/USB)...{RST}\n")
    
    for doc, user, body in queue:
        time.sleep(1.5)
        sentry.intercept_job(doc, user, body)

if __name__ == "__main__":
    try:
        run_print_simulation()
        print(f"{C9}[*] Dipa-Print monitoring stabilized. Spooler empty.{RST}")
    except KeyboardInterrupt:
        print(f"\n{C4}[!] Spooler Offline.{RST}")