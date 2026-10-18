import os
import time
import sys

# ==========================================
# UPANISHAD-DETECTOR: DECRYPTION COLOR THEME
# ==========================================
GLD = '\033[93m'  # Gold/Yellow (Truth/Detection)
GRY = '\033[90m'  # Dark Grey (Encrypted/Raw Text)
WHT = '\033[97m'  # White (System)
RED = '\033[91m'  # Red (Critical Pattern)
RST = '\033[0m'   # Reset
BLD = '\033[1m'

# ==========================================
# DATA-ORIENTED TRIE ALGORITHM
# ==========================================
# Instead of objects, the Trie is a massive, highly-optimized nested dictionary.

def compile_trie_matrix(keywords):
    """Compiles a list of sensitive keywords into a Prefix Tree (Trie)."""
    print(f"{WHT}[*] Compiling algorithmic Prefix Tree matrix...{RST}")
    root = {}
    for word in keywords:
        current_node = root
        for char in word.lower():
            # Create a new nested dictionary for the character if it doesn't exist
            current_node = current_node.setdefault(char, {})
        # Mark the end of a valid keyword sequence
        current_node['__END__'] = word.upper()
    
    time.sleep(0.5)
    print(f"{GLD}[+] Matrix compilation complete. O(N) traversal ready.{RST}\n")
    return root

def algorithmic_scan(trie_root, text):
    """Scans text in linear time using the pre-compiled Trie."""
    text_lower = text.lower()
    text_length = len(text_lower)
    detections = []
    
    # Simulating deep memory analysis for terminal aesthetic
    print(f"{GRY}--- COMMENCING DEEP PATTERN TRAVERSAL ---{RST}")
    
    for i in range(text_length):
        current_node = trie_root
        
        # Check forward from the current character
        for j in range(i, text_length):
            char = text_lower[j]
            if char not in current_node:
                break # Pattern broken, move to next starting character
            
            current_node = current_node[char]
            
            # If we hit an endpoint, we found a match
            if '__END__' in current_node:
                match_word = current_node['__END__']
                detections.append((match_word, i, j))
                
                # Aesthetic terminal output for a "hit"
                sys.stdout.write(f"\r{RED}[!] PATTERN MATCH DETECTED AT OFFSET 0x{i:04X}: {BLD}{match_word}{RST}    \n")
                time.sleep(0.1)
                
        # Aesthetic progress indicator
        if i % 15 == 0:
            sys.stdout.write(f"\r{GRY}Traversing sector {i}/{text_length}...{RST}")
            sys.stdout.flush()
            time.sleep(0.01)

    print(f"\r{GLD}[+] Traversal complete. End of file reached.       {RST}\n")
    return detections

# ==========================================
# SYSTEM EXECUTION & AESTHETICS
# ==========================================

def display_upanishad_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = f"""{GLD}{BLD}
     _   _                   _     _               _ 
    | | | |                 (_)   | |             | |
    | | | |_ __   __ _ _ __  _ ___| |__   __ _  __| |
    | | | | '_ \ / _` | '_ \| / __| '_ \ / _` |/ _` |
    | |_| | |_) | (_| | | | | \__ \ | | | (_| | (_| |
     \___/| .__/ \__,_|_| |_|_|___/_| |_|\__,_|\__,_|
          | |      D E T E C T O R                   
          |_|                                        
    {RST}"""
    print(banner)
    print(f"{WHT}>> ALGORITHM: PREFIX TREE (TRIE) DATA STRUCTURE{RST}")
    print(f"{WHT}>> COMPLEXITY: O(N) LINEAR TIME TRAVERSAL{RST}")
    print(f"{WHT}>> DIRECTIVE: SENSITIVE PATTERN MATCHING{RST}\n")

def setup_payload():
    """Generates the dummy text to be scanned."""
    return (
        "The server migration is scheduled for tonight. Ensure all firewall rules "
        "are updated. The backdoor admin password is 'phoenix_protocol'. Also, "
        "the financial ledger containing the offshore account routing data is "
        "saved in the root directory. Do not expose the private key."
    )

def run_detector():
    display_upanishad_banner()
    
    # 1. Define the sensitive patterns to look for
    threat_keywords = [
        "password", "backdoor", "routing data", 
        "private key", "financial ledger", "exploit"
    ]
    
    # 2. Build the Trie Data Structure
    trie_matrix = compile_trie_matrix(threat_keywords)
    
    # 3. Load Payload
    payload = setup_payload()
    print(f"{WHT}[*] Target payload loaded into memory ({len(payload)} bytes).{RST}\n")
    time.sleep(1)
    
    # 4. Execute Scan
    results = algorithmic_scan(trie_matrix, payload)
    
    # 5. Output Summary
    print(f"{GLD}{BLD}============== EXTRACTION SUMMARY =============={RST}")
    if results:
        print(f"{RED}Total Critical Patterns Found: {len(results)}{RST}")
        for match, start, end in results:
            print(f" - {match} (Offset: {start})")
    else:
        print(f"{WHT}No sensitive patterns detected.{RST}")
    print(f"{GLD}{BLD}=============================================={RST}")

if __name__ == "__main__":
    try:
        run_detector()
    except KeyboardInterrupt:
        print(f"\n{RED}[!] Traversal forcefully terminated by operator.{RST}")