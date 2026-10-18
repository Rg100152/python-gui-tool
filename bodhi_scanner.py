import asyncio
import os
import random
import sys

# ==========================================
# BODHI-SCANNER: TERMINAL COLOR SCHEME
# ==========================================
C = '\033[96m'  # Cyan (System/Workers)
G = '\033[92m'  # Green (Compliant/Safe)
Y = '\033[93m'  # Yellow (Warning)
R = '\033[91m'  # Red (Violation/Breach)
E = '\033[0m'   # Reset
W = '\033[97m'  # White

# ==========================================
# SYSTEM SETUP & AESTHETICS
# ==========================================

def display_banner():
    """Renders the Bodhi-Scanner visual banner."""
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = f"""{C}
    ██████╗  ██████╗ ██████╗ ██╗  ██╗██╗
    ██╔══██╗██╔═══██╗██╔══██╗██║  ██║██║
    ██████╔╝██║   ██║██║  ██║███████║██║
    ██╔══██╗██║   ██║██║  ██║██╔══██║██║
    ██████╔╝╚██████╔╝██████╔╝██║  ██║██║
    ╚═════╝  ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝ {W}S C A N N E R{E}
    """
    print(banner)
    print(f"{C}[*] ARCHITECTURE: ASYNCHRONOUS CONCURRENT I/O{E}")
    print(f"{C}[*] ENGINE: COMPLIANCE & UNCLASSIFIED DATA DETECTION{E}")
    print(f"{Y}[!] WARNING: DEPLOYING MULTIPLE WORKER THREADS{E}\n")

def setup_target_environment():
    """Generates a mix of compliant and non-compliant files for the scanner to audit."""
    targets = {
        "node_alpha.txt": "Public marketing copy. Nothing sensitive here.",
        "node_beta.txt": "--- BEGIN ASHOKA METADATA ---\nClassification: CUI//SP-PRVT\n--- END ---\nEmployee salary and Aadhar data.",
        "node_gamma.txt": "URGENT: Project firewall zero-day exploit details inside. Do not share." # Violation! Sensitive, but no tags.
    }
    
    print(f"{C}[SYSTEM] Initializing virtual file system...{E}")
    for filename, content in targets.items():
        with open(filename, "w") as f:
            f.write(content)
    return list(targets.keys())

# ==========================================
# ASYNCHRONOUS SCANNING ENGINE
# ==========================================

async def analyze_file(filepath, worker_id):
    """
    The core async worker function. 
    Simulates deep scanning and checks compliance logic.
    """
    prefix = f"{C}[WORKER-{worker_id}]{E}"
    print(f"{prefix} Assigned to target: {W}{filepath}{E}")
    
    # Simulate network latency or large file processing
    await asyncio.sleep(random.uniform(0.5, 1.5))
    print(f"{prefix} Extracting sector data from {filepath}...")
    
    try:
        with open(filepath, "r") as f:
            content = f.read().lower()
    except Exception as e:
        print(f"{prefix} {R}ERROR: {e}{E}")
        return

    # Simulate deep logic parsing
    await asyncio.sleep(random.uniform(1.0, 2.0))
    
    # -----------------------------------------
    # COMPLIANCE LOGIC MATRIX
    # -----------------------------------------
    sensitive_keywords = ["aadhar", "salary", "zero-day", "exploit", "ssn", "financial"]
    cui_tags = ["classification: cui", "ashoka metadata", "restricted", "confidential"]
    
    contains_sensitive_data = any(word in content for word in sensitive_keywords)
    contains_security_tags = any(tag in content for tag in cui_tags)
    
    print(f"{prefix} Analysis complete for {filepath}. Generating report...")
    await asyncio.sleep(0.5)

    # Output Results
    print("\n" + "-"*50)
    print(f"{W}REPORT FOR: {filepath}{E}")
    if contains_sensitive_data and not contains_security_tags:
        print(f"{R}[!] CRITICAL VIOLATION: UNCLASSIFIED CUI DETECTED!{E}")
        print(f"{R}[!] Sensitive data found without proper marking headers.{E}")
    elif contains_sensitive_data and contains_security_tags:
        print(f"{G}[+] COMPLIANT: Sensitive data detected, but proper CUI tags are present.{E}")
    else:
        print(f"{G}[+] CLEAR: No sensitive data detected. Public routing allowed.{E}")
    print("-" * 50 + "\n")

async def orchestrator():
    """Main async function to manage all concurrent tasks."""
    display_banner()
    
    # 1. Setup Environment
    target_files = setup_target_environment()
    await asyncio.sleep(1)
    
    # 2. Build the task list
    print(f"\n{Y}>>> INITIATING ASYNC SWARM SCAN <<< {E}\n")
    tasks = []
    
    # We assign a different "Worker ID" to each file to track them concurrently
    for i, file in enumerate(target_files, start=1):
        task = asyncio.create_task(analyze_file(file, worker_id=f"00{i}"))
        tasks.append(task)
        
    # 3. Execute all tasks SIMULTANEOUSLY (This is the magic of asyncio)
    await asyncio.gather(*tasks)
    
    print(f"{C}[SYSTEM] All worker threads terminated. Swarm scan complete.{E}")

# ==========================================
# EXECUTION TRIGGER
# ==========================================
if __name__ == "__main__":
    try:
        # In modern Python, this is how we start an async program
        asyncio.run(orchestrator())
    except KeyboardInterrupt:
        print(f"\n{R}[SYSTEM] Emergency halt. Killing all worker threads...{E}")