import os
import sys
import time
import secrets
import re
from datetime import datetime

# ==========================================
# TATHAGATA-EMAIL: TRUTH & CLARITY 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;255m', '\033[38;5;196m', '\033[38;5;220m', '\033[38;5;232m', '\033[38;5;254m'
C6, C7, C8, C9, C10  = '\033[38;5;39m', '\033[38;5;250m', '\033[38;5;93m', '\033[38;5;244m', '\033[38;5;45m'
C11, C12, C13, C14, C15 = '\033[38;5;202m', '\033[38;5;121m', '\033[38;5;18m', '\033[38;5;165m', '\033[38;5;242m'
C16, C17, C18, C19, C20 = '\033[38;5;37m', '\033[38;5;203m', '\033[38;5;214m', '\033[38;5;28m', '\033[38;5;17m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE FLYING ENVELOPE (TATHAGATA)
# ==========================================
def tathagata_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C7}          _______
    {C7}         /\\      \\
    {C6}        /  \\  {C3}*   {C6}\\
    {C10}       /    \\______\\
    {C10}      /     /      /
    {C1}     /_____/______/
    {C13}   [ EMAIL GUARD v4.4 ]
    """
    print(logo)
    print(f"{C6}{BLD}   TATHAGATA-EMAIL: OUTGOING CONTENT INSPECTION{RST}\n")
    
    # Scanning animation
    for i in range(12):
        sys.stdout.write(f"\r{C9}[{C3}SCAN{C9}] {C1}Analyzing MIME Structure... {C6}{'|/-\\'[i%4]}{RST}")
        sys.stdout.flush()
        time.sleep(0.1)
    print(f"\n{C12}[+] SMTP Proxy Active. Heuristic Engine Primed.{RST}\n")

# ==========================================
# ARCHITECTURE: HEURISTIC EMAIL SCANNER
# ==========================================
class EmailSentry:
    """Simulates a secure email gateway for CUI protection."""
    def __init__(self):
        # Weighted keywords (Keyword: Threat Score)
        self.risk_patterns = {
            r"CUI": 40,
            r"CONFIDENTIAL": 30,
            r"PROPRIETARY": 25,
            r"INTERNAL ONLY": 20,
            r"NUCLEAR": 50,
            r"PASSWORD": 30
        }
        self.threshold = 50 # Score above this will block the email

    def scan_email(self, sender, recipient, subject, body, attachments):
        """Calculates total risk score of an outgoing email."""
        total_score = 0
        findings = []
        combined_text = (subject + " " + body).upper()

        # Check Subject and Body
        for pattern, score in self.risk_patterns.items():
            if re.search(pattern, combined_text):
                total_score += score
                findings.append(pattern)

        # Check Attachments (Simulated metadata check)
        for attachment in attachments:
            if "CUI" in attachment.upper() or ".DB" in attachment.upper():
                total_score += 45
                findings.append(f"FILE:{attachment}")

        self._display_scan_result(sender, recipient, subject, total_score, findings)
        return total_score < self.threshold

    def _display_scan_result(self, s, r, sub, score, findings):
        ts = datetime.now().strftime("%H:%M:%S")
        status_color = C20 if score >= self.threshold else C19
        verdict = f"{C2}BLOCKED{RST}" if score >= self.threshold else f"{C12}ALLOWED{RST}"
        
        print(f"{C9}┌──[ EMAIL OUTBOUND ANALYSIS ]{'─'*25}{RST}")
        print(f"{C9}│ {C1}FROM    : {C6}{s}{RST}")
        print(f"{C9}│ {C1}TO      : {C10}{r}{RST}")
        print(f"{C9}│ {C1}SUBJECT : {C7}{sub}{RST}")
        print(f"{C9}│ {C1}RISK    : {status_color}{BLD}{score}/100{RST}")
        print(f"{C9}│ {C1}FINDINGS: {C18}{', '.join(findings) if findings else 'None'}{RST}")
        print(f"{C9}│ {C1}VERDICT : {verdict}{RST}")
        print(f"{C9}└{'─'*55}{RST}\n")

# ==========================================
# SIMULATION: OUTGOING MAIL SPOOL
# ==========================================
def simulate_mail_traffic():
    tathagata_banner_anim()
    guard = EmailSentry()
    
    outbox = [
        ("raj@vsspu.edu", "shani@partner.com", "Project Update", "The meeting is at 5 PM.", []),
        ("admin@vsspu.edu", "competitor@gmail.com", "CUI Data Export", "Attached are the internal nuclear specs.", ["cui_data_v1.xlsx"]),
        ("raj@vsspu.edu", "professor@edu.in", "Research Paper", "Draft for your review.", ["research.pdf"]),
        ("guest_x", "unknown@darkweb.org", "INTERNAL ONLY INFO", "Here is the proprietary info.", ["server_passwords.txt"])
    ]
    
    print(f"{C13}[!] INTERCEPTING OUTBOUND SMTP TRAFFIC...{RST}\n")
    
    for sender, rec, sub, body, att in outbox:
        time.sleep(1.5)
        guard.scan_email(sender, rec, sub, body, att)

if __name__ == "__main__":
    try:
        simulate_mail_traffic()
        print(f"{C12}[✔] Tathagata-Email monitoring complete. All leaks plugged.{RST}")
    except KeyboardInterrupt:
        print(f"\n{C17}[!] Proxy Offline.{RST}")