import os
import time
import base64
import binascii

# ==========================================
# VEDANTA-INJECTOR: STEALTH COLOR THEME
# ==========================================
PRP = '\033[95m'  # Purple (Stealth/System)
CYN = '\033[96m'  # Cyan (Data)
GRN = '\033[92m'  # Green (Success)
RED = '\033[91m'  # Red (Alert)
GRY = '\033[90m'  # Grey (Hex Dumps)
RST = '\033[0m'   # Reset
BLD = '\033[1m'

# ==========================================
# FLUENT BUILDER ARCHITECTURE & BINARY LOGIC
# ==========================================
class VedantaInjector:
    """
    Implements the Fluent Builder Pattern.
    Notice how every method returns 'self', allowing us to chain commands 
    like: injector.set_target().build_payload().inject()
    """
    def __init__(self):
        self.target_file = None
        self.metadata = {}
        self.encoded_payload = b""
        # "VEDA" in hexadecimal acts as our hidden file signature
        self.magic_bytes = b'\x56\x45\x44\x41' 

    def set_target(self, filepath):
        """Locks onto the target file."""
        print(f"{PRP}[*] Locking target acquisition: {BLD}{filepath}{RST}")
        self.target_file = filepath
        time.sleep(0.3)
        return self

    def add_cui_tag(self, level):
        """Adds classification data to the builder dictionary."""
        print(f"{CYN}[+] Appending CUI routing tag: {level}{RST}")
        self.metadata['CUI_LEVEL'] = level
        time.sleep(0.2)
        return self

    def add_operator(self, operator_id):
        """Adds operator ID to the builder dictionary."""
        print(f"{CYN}[+] Appending Operator Signature: {operator_id}{RST}")
        self.metadata['OPERATOR'] = operator_id
        time.sleep(0.2)
        return self

    def compile_payload(self):
        """Converts the dictionary into a Base64 encrypted binary payload."""
        print(f"{PRP}[*] Compiling metadata into binary payload...{RST}")
        raw_string = "|".join([f"{k}:{v}" for k, v in self.metadata.items()])
        
        # Convert to bytes, then Base64 encode for obfuscation
        b64_bytes = base64.b64encode(raw_string.encode('utf-8'))
        
        # Construct final payload: [MAGIC_BYTES] + [BASE64_DATA] + [MAGIC_BYTES]
        self.encoded_payload = self.magic_bytes + b64_bytes + self.magic_bytes
        
        print(f"{GRY}    ↳ HEX DUMP: {binascii.hexlify(self.encoded_payload).decode('utf-8').upper()}{RST}")
        time.sleep(0.5)
        return self

    def inject_eof(self):
        """Opens file in APPEND BINARY ('ab') mode to inject without corrupting original data."""
        if not self.target_file or not os.path.exists(self.target_file):
            print(f"{RED}[-] Error: Target lost or does not exist.{RST}")
            return False
            
        print(f"{PRP}[*] Opening {self.target_file} in raw binary mode...{RST}")
        try:
            with open(self.target_file, 'ab') as f:
                f.write(self.encoded_payload)
            print(f"{GRN}{BLD}[+] INJECTION SUCCESSFUL. {len(self.encoded_payload)} bytes appended to EOF.{RST}\n")
            return True
        except Exception as e:
            print(f"{RED}[-] Critical fault during injection: {e}{RST}")
            return False

# ==========================================
# FORENSIC EXTRACTION (VERIFICATION)
# ==========================================
def extract_vedanta_metadata(filepath):
    """Reads the binary file backwards to find our hidden VEDA magic bytes."""
    print(f"{CYN}{BLD}>>> INITIATING FORENSIC VERIFICATION SCALPEL <<<{RST}")
    time.sleep(0.5)
    
    try:
        # Open in READ BINARY ('rb') mode
        with open(filepath, 'rb') as f:
            content = f.read()
            
        # Search for our custom Magic Bytes sequence
        magic_signature = b'\x56\x45\x44\x41'
        
        # Find the first and last occurrence of the magic bytes
        start_idx = content.find(magic_signature)
        if start_idx == -1:
            print(f"{RED}[-] No Vedanta signature found in target memory.{RST}")
            return
            
        # Extract the data sandwiched between the magic bytes
        end_idx = content.rfind(magic_signature)
        raw_b64 = content[start_idx + 4 : end_idx]
        
        print(f"{GRY}[*] Signature matched at offset 0x{start_idx:04X}{RST}")
        print(f"{PRP}[*] Decoding Base64 extracted payload...{RST}")
        time.sleep(0.5)
        
        decoded_data = base64.b64decode(raw_b64).decode('utf-8')
        
        print(f"{GRN}[+] RECOVERED EMBEDDED METADATA:{RST}")
        print(f"{CYN}{'-'*40}{RST}")
        for item in decoded_data.split('|'):
            print(f" {BLD}{item}{RST}")
        print(f"{CYN}{'-'*40}{RST}\n")
        
    except Exception as e:
        print(f"{RED}[-] Extraction failed: {e}{RST}")

# ==========================================
# SYSTEM EXECUTION & AESTHETICS
# ==========================================
def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = f"""{PRP}{BLD}
    __     __        _             _          
    \ \   / /__   __| | __ _ _ __ | |_ __ _   
     \ \ / / _ \ / _` |/ _` | '_ \| __/ _` |  
      \ V /  __/ (_| | (_| | | | | || (_| |  
       \_/ \___|\__,_|\__,_|_| |_|\__\__,_|  
       {CYN}I N J E C T O R   P R O T O C O L{RST}
    """
    print(banner)
    print(f"{CYN}>> ARCHITECTURE: FLUENT BUILDER / METHOD CHAINING{RST}")
    print(f"{CYN}>> OPERATION: RAW BINARY/BYTE-LEVEL EOF INJECTION{RST}\n")

def create_carrier_file():
    """Generates a standard text file to act as the carrier for our binary payload."""
    filename = "vedanta_carrier.txt"
    with open(filename, "w") as f:
        f.write("This is a standard system configuration file.\nNothing to see here.\nEND OF CONFIGURATION.\n")
    return filename

if __name__ == "__main__":
    print_banner()
    
    # Generate the dummy target
    target = create_carrier_file()
    
    # ==========================================================
    # THE FLUENT BUILDER PATTERN IN ACTION
    # Notice how clean this looks. It reads like a sentence.
    # ==========================================================
    injector = VedantaInjector()
    
    (injector.set_target(target)
             .add_cui_tag("CUI // SP-PRVT")
             .add_operator("SYSTEM_ROOT_01")
             .compile_payload()
             .inject_eof())
             
    # Verify the injection worked without destroying the original text
    extract_vedanta_metadata(target)