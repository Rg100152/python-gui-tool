import os
import time
import random
from datetime import datetime

# ==========================================
# ASHOKA-TAGGER: TERMINAL COLOR SCHEME
# ==========================================
M = '\033[95m'  # Magenta (Primary Theme)
B = '\033[94m'  # Blue (Information)
G = '\033[92m'  # Green (Success)
Y = '\033[93m'  # Yellow (Warning)
R = '\033[91m'  # Red (Alert)
E = '\033[0m'   # Reset
BOLD = '\033[1m'

# ==========================================
# SYSTEM INITIALIZATION & AESTHETICS
# ==========================================

def print_banner():
    """Renders the Ashoka-Tagger system banner."""
    print(f"{M}{BOLD}")
    print("    ___   _____ __  __ ____  _  __  ___      ")
    print("   /   | / ___// / / / __ \/ |/ / /   |      ")
    print("  / /| | \__ \/ /_/ / / / /   /  / /| |      ")
    print(" / ___ |___/ / __  / /_/ /   |  / ___ |      ")
    print("/_/  |_/____/_/ /_/\____/_/|_| /_/  |_|      ")
    print("        T A G G E R   S Y S T E M            ")
    print(f"{E}")
    print(f"{B}[*] PIPELINE: GENERATOR-BASED STREAM PROCESSING{E}")
    print(f"{B}[*] PROTOCOL: CUI METADATA STAMPING & INJECTION{E}\n")

def simulate_processing(task_name, duration=0.8):
    """Simulates a hacking-style progress indicator."""
    print(f"{B}[~] {task_name}...{E}", end=" ", flush=True)
    chars = "/-\\|"
    for i in range(int(duration * 10)):
        print(f"\b{chars[i % len(chars)]}", end="", flush=True)
        time.sleep(0.1)
    print(f"\b{G}DONE{E}")

def generate_test_target(filepath):
    """Ensures a file exists for the pipeline to process."""
    if not os.path.exists(filepath):
        print(f"{Y}[!] Target missing. Synthesizing test payload: {filepath}{E}")
        with open(filepath, "w") as f:
            f.write("PROJECT GHOST-PROTOCOL: Financial audit for Q3.\nIncludes offshore account routing numbers.\n")
    return filepath

# ==========================================
# THE PIPELINE ARCHITECTURE (GENERATORS)
# ==========================================
# Notice the use of 'yield'. Data flows through these functions one step at a time.

def stage1_file_scanner(directory="."):
    """Stage 1: Scans directory for targets and yields them."""
    simulate_processing("Scanning local sector for target files", 1.2)
    # For this script, we target our specific test file
    target = generate_test_target("ghost_protocol_audit.txt")
    yield target

def stage2_metadata_extractor(file_stream):
    """Stage 2: Extracts OS-level metadata from the files."""
    for filepath in file_stream:
        simulate_processing(f"Extracting raw metadata from {filepath}", 0.9)
        
        # Gathering real file stats
        file_stats = os.stat(filepath)
        
        metadata = {
            "file_size": file_stats.st_size,
            "created_timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "author_id": f"SYS_ADMIN_{random.randint(100,999)}",
            "encryption_hash": f"SHA256-{random.randint(100000, 999999)}"
        }
        yield (filepath, metadata)

def stage3_cui_classifier(metadata_stream):
    """Stage 3: Determines CUI level based on file size and random entropy."""
    for filepath, metadata in metadata_stream:
        simulate_processing("Running heuristic classification algorithm", 1.5)
        
        # Simulated logic for tagging
        if metadata["file_size"] > 50:
            classification = "CUI // SP-FINANCIAL // RESTRICTED"
            clearance = "LEVEL_4_REQUIRED"
        else:
            classification = "UNCLASSIFIED // PUBLIC"
            clearance = "NO_RESTRICTION"
            
        metadata["cui_level"] = classification
        metadata["clearance"] = clearance
        yield (filepath, metadata)

def stage4_tag_injector(classified_stream):
    """Stage 4: Injects the YAML-style metadata frontmatter into the actual file."""
    for filepath, metadata in classified_stream:
        simulate_processing("Injecting encrypted metadata block", 1.0)
        
        with open(filepath, "r") as f:
            original_content = f.read()
            
        # Prevent double-tagging
        if "--- BEGIN ASHOKA METADATA ---" in original_content:
            print(f"{Y}[!] File {filepath} is already tagged. Bypassing injection.{E}")
            yield (filepath, False)
            continue

        # Constructing the Frontmatter
        frontmatter = f"""--- BEGIN ASHOKA METADATA ---
Classification: {metadata['cui_level']}
Clearance_Req:  {metadata['clearance']}
Author_ID:      {metadata['author_id']}
Timestamp:      {metadata['created_timestamp']}
Hash_Verify:    {metadata['encryption_hash']}
--- END ASHOKA METADATA ---

"""
        # Overwrite file with new metadata at the top
        with open(filepath, "w") as f:
            f.write(frontmatter + original_content)
            
        yield (filepath, True)

# ==========================================
# MAIN EXECUTION SINK
# ==========================================

def run_pipeline():
    """Connects the pipeline stages and consumes the final output."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_banner()
    
    # Building the pipeline stream
    stream_1 = stage1_file_scanner()
    stream_2 = stage2_metadata_extractor(stream_1)
    stream_3 = stage3_cui_classifier(stream_2)
    final_stream = stage4_tag_injector(stream_3)
    
    # Consuming the stream (This triggers the whole process)
    print(f"{M}{BOLD}>>> COMMENCING PIPELINE EXECUTION <<<{E}")
    
    for filepath, success in final_stream:
        print("\n" + "="*50)
        if success:
            print(f"{G}[+] OPERATION SUCCESSFUL.{E}")
            print(f"{G}[+] Target {filepath} has been permanently tagged.{E}")
            print(f"{B}[*] Run 'type {filepath}' (Windows) or 'cat {filepath}' (Linux) to view the injected metadata.{E}")
        else:
            print(f"{R}[-] OPERATION ABORTED: Tagging skipped.{E}")
        print("="*50 + "\n")

if __name__ == "__main__":
    run_pipeline()