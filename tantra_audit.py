import os
import sys
import time
import math
import secrets
import base64
from concurrent.futures import ThreadPoolExecutor, as_completed

# ==========================================
# TANTRA-AUDIT: NEON MATRIX HACKER THEME
# (Exactly 10 Unique ANSI 256 Colors)
# ==========================================
TOXIC_GRN   = '\033[38;5;82m'   # Matrix Green
CYBER_CYAN  = '\033[38;5;51m'   # Bright Cyan
BLOOD_RED   = '\033[38;5;196m'  # Bright Red
HOT_PINK    = '\033[38;5;198m'  # Hot Pink
WARNING_ORG = '\033[38;5;208m'  # Neon Orange
RAD_YEL     = '\033[38;5;226m'  # Radioactive Yellow
DEEP_AZURE  = '\033[38;5;39m'   # Deep Blue
DEEP_PURP   = '\033[38;5;165m'  # Purple
LILAC       = '\033[38;5;135m'  # Soft Lilac
SILVER_GRY  = '\033[38;5;250m'  # Silver
RST         = '\033[0m'
BLD         = '\033[1m'

# ==========================================
# ANIMATION: HACKER TERMINAL INJECTION
# ==========================================
def tantra_boot_sequence():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{DEEP_PURP}{BLD}>> TANTRA CRYPTO-AUDIT FRAMEWORK v2.0 <<{RST}\n")
    
    # Fast scrolling hex animation to simulate deep scanning
    print(f"{CYBER_CYAN}[*] Injecting Multi-Threaded Payload Scanners...{RST}")
    for _ in range(8):
        hex_dump = " ".join(secrets.token_hex(2) for _ in range(8))
        sys.stdout.write(f"\r{TOXIC_GRN}[MEM_ADDR: 0x{secrets.token_hex(4).upper()}] {SILVER_GRY}{hex_dump}{RST}")
        sys.stdout.flush()
        time.sleep(0.08)
    print(f"\r{TOXIC_GRN}[+] TANTRA ENGINE ONLINE. SHANNON ENTROPY MODULE LOADED.           {RST}\n")
    time.sleep(0.5)

# ==========================================
# ENVIRONMENT SETUP: GENERATING DUMMY TARGETS
# ==========================================
def prepare_target_files():
    """Generates 3 different files simulating different encryption strengths."""
    print(f"{DEEP_AZURE}┌──[ TARGET ACQUISITION ]{'─'*40}{RST}")
    
    # Target 1: Plaintext (No Encryption)
    with open("target_alpha.dat", "wb") as f:
        f.write(b"CONFIDENTIAL: User passwords are stored in the main database.")
    print(f"{DEEP_AZURE}│ {LILAC}Target Alpha  : target_alpha.dat (Unknown Cipher){RST}")

    # Target 2: Weak Encryption (Base64 / XOR Simulation)
    with open("target_beta.dat", "wb") as f:
        msg = b"TOP SECRET MISSION DATA REQUIRING ENCRYPTION" * 10
        f.write(base64.b64encode(msg))
    print(f"{DEEP_AZURE}│ {LILAC}Target Beta   : target_beta.dat  (Unknown Cipher){RST}")

    # Target 3: Strong Encryption (Simulating AES-256 random bytes)
    with open("target_omega.dat", "wb") as f:
        f.write(secrets.token_bytes(2048)) # Pure cryptographic randomness
    print(f"{DEEP_AZURE}│ {LILAC}Target Omega  : target_omega.dat (Unknown Cipher){RST}")
    print(f"{DEEP_AZURE}└{'─'*64}{RST}\n")
    
    return ["target_alpha.dat", "target_beta.dat", "target_omega.dat"]

# ==========================================
# ARCHITECTURE: INFORMATION THEORY & THREAD POOLING
# ==========================================
class InformationTheoryAnalyzer:
    @staticmethod
    def calculate_shannon_entropy(data: bytes) -> float:
        """
        Mathematical formula for Shannon Entropy. 
        Returns a value between 0.0 and 8.0.
        8.0 = Perfect encryption/compression.
        """
        if not data: return 0.0
        entropy = 0
        for x in range(256):
            p_x = float(data.count(x)) / len(data)
            if p_x > 0:
                entropy += - p_x * math.log(p_x, 2)
        return entropy

def audit_file_worker(filepath: str):
    """
    The concurrent worker function. This runs in an isolated thread.
    Simulates intensive cryptographic analysis.
    """
    thread_id = secrets.token_hex(2).upper()
    print(f"{HOT_PINK}[THREAD-{thread_id}] Starting deep scan on {filepath}...{RST}")
    time.sleep(0.5) # Simulate processing time
    
    with open(filepath, "rb") as f:
        data = f.read()

    entropy = InformationTheoryAnalyzer.calculate_shannon_entropy(data)
    
    # Hacker Heuristics Analysis
    status_color = SILVER_GRY
    verdict = ""
    weakness_type = ""

    if entropy < 5.0:
        status_color = BLOOD_RED
        verdict = "CRITICAL VULNERABILITY"
        weakness_type = "PLAINTEXT DETECTED. Zero Cryptographic Protection."
    elif 5.0 <= entropy <= 7.5:
        status_color = WARNING_ORG
        verdict = "WEAK CIPHER IDENTIFIED"
        weakness_type = "Base64/XOR Padding signature detected. Highly crackable."
    else:
        status_color = TOXIC_GRN
        verdict = "STRONG ENCRYPTION"
        weakness_type = "Military-grade entropy (Likely AES-256/ChaCha20). Uncrackable."

    # Return results as a formatted dictionary
    return {
        "file": filepath,
        "tid": thread_id,
        "entropy": round(entropy, 4),
        "verdict": verdict,
        "weakness": weakness_type,
        "color": status_color
    }

# ==========================================
# MAIN EXECUTION ENGINE
# ==========================================
def run_tantra_engine():
    tantra_boot_sequence()
    targets = prepare_target_files()
    
    print(f"{RAD_YEL}[*] INITIALIZING CONCURRENT THREAD POOL EXECUTOR...{RST}\n")
    time.sleep(0.5)
    
    results = []
    # Spin up concurrent worker threads (Real-World High-Performance Python)
    with ThreadPoolExecutor(max_workers=3) as executor:
        # Map targets to threads
        future_to_file = {executor.submit(audit_file_worker, target): target for target in targets}
        
        # As threads complete their mathematical analysis, process results
        for future in as_completed(future_to_file):
            results.append(future.result())
            
    print(f"\n{DEEP_PURP}{BLD}═════════════════[ AUDIT RESULTS ]═════════════════{RST}")
    
    # Display Results in Hacker Tool Format
    for res in sorted(results, key=lambda x: x['file']):
        c = res['color']
        print(f"{CYBER_CYAN}TARGET: {LILAC}{res['file']} {SILVER_GRY}(Scanned by T-{res['tid']}){RST}")
        print(f"{DEEP_AZURE} ├─ ENTROPY INDEX : {RAD_YEL}{res['entropy']} / 8.0000{RST}")
        print(f"{DEEP_AZURE} ├─ THREAT STATE  : {c}{BLD}{res['verdict']}{RST}")
        print(f"{DEEP_AZURE} └─ SIGNATURE     : {c}{res['weakness']}{RST}\n")
        time.sleep(0.3)

    # Cleanup generated files
    for target in targets:
        if os.path.exists(target): os.remove(target)

if __name__ == "__main__":
    try:
        run_tantra_engine()
    except KeyboardInterrupt:
        print(f"\n{BLOOD_RED}[!] AUDIT ABORTED BY USER.{RST}")