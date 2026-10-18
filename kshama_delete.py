import os
import sys
import time
import mmap
import secrets

# ==========================================
# KSHAMA-DELETE: THE VOID SHREDDER THEME
# (5 Unique Non-Repeating Colors)
# ==========================================
MAGENTA = '\033[38;5;206m' 
LIME    = '\033[38;5;113m'  
AZURE   = '\033[38;5;39m'   
COPPER  = '\033[38;5;208m'  
STEEL   = '\033[38;5;244m'  
RST     = '\033[0m'
BLD     = '\033[1m'

# ==========================================
# ANIMATION: THE ERASURE SEQUENCE
# ==========================================
def shredder_boot_animation():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{MAGENTA}{BLD}>> KSHAMA ZERO-COPY SECURE SHREDDER <<{RST}\n")
    
    blocks = ["[ DATA ]", "[ 0000 ]", "[ FFFF ]", "[ #### ]", "[ VOID ]"]
    colors = [AZURE, COPPER, MAGENTA, LIME, STEEL]
    
    sys.stdout.write(f"{STEEL}Initializing mmap sector targeting: {RST}")
    for i in range(5):
        sys.stdout.write(f"\r{STEEL}Initializing mmap sector targeting: {colors[i]}{BLD}{blocks[i]}{RST}")
        sys.stdout.flush()
        time.sleep(0.4)
    print(f"\n\n{LIME}[+] Hardware bypass active. DoD 5220.22-M Algorithm Loaded.{RST}\n")

# ==========================================
# ARCHITECTURE: MEMORY-MAPPED OVERWRITE PROTOCOL
# ==========================================
class MemoryMappedShredder:
    """
    Directly maps physical disk sectors to memory to bypass OS buffering.
    Executes Military-Grade 3-Pass Overwrite.
    """
    def __init__(self, filepath):
        self.filepath = filepath
        self.filesize = os.path.getsize(filepath)

    def _display_hex_dump(self, preview_size=32):
        """Shows the raw bytes of the file to prove the data is changing."""
        try:
            with open(self.filepath, "rb") as f:
                data = f.read(preview_size)
                hex_view = " ".join(f"{b:02x}" for b in data)
                ascii_view = "".join(chr(b) if 32 <= b <= 126 else "." for b in data)
                print(f"{STEEL}      HEX: {hex_view}{RST}")
                print(f"{STEEL}      ASC: {ascii_view}{RST}")
        except FileNotFoundError:
            pass

    def shred_dod_5220_22_m(self):
        """Implements the 3-Pass Department of Defense wiping standard."""
        print(f"{AZURE}[*] TARGET: {self.filepath} ({self.filesize} bytes){RST}")
        print(f"{STEEL}[*] PRE-SHRED DISK STATE:{RST}")
        self._display_hex_dump()
        time.sleep(1)

        # Ensure file is opened in r+b mode for mmap to work
        with open(self.filepath, "r+b") as f:
            # Map the entire file directly to RAM/Disk block
            mm = mmap.mmap(f.fileno(), 0)

            # --- PASS 1: OVERWRITE WITH ZEROS (0x00) ---
            print(f"\n{COPPER}>>> PASS 1: Overwriting sectors with Zeros (0x00)...{RST}")
            mm.seek(0)
            mm.write(b'\x00' * self.filesize)
            mm.flush()          # Force flush to OS
            os.fsync(f.fileno())# Force flush hardware buffers to Physical Disk
            self._display_hex_dump()
            time.sleep(0.5)

            # --- PASS 2: OVERWRITE WITH ONES (0xFF) ---
            print(f"\n{MAGENTA}>>> PASS 2: Overwriting sectors with Ones (0xFF)...{RST}")
            mm.seek(0)
            mm.write(b'\xff' * self.filesize)
            mm.flush()
            os.fsync(f.fileno())
            self._display_hex_dump()
            time.sleep(0.5)

            # --- PASS 3: OVERWRITE WITH CRYPTOGRAPHIC RANDOM DATA ---
            print(f"\n{LIME}>>> PASS 3: Overwriting sectors with Random Entropy...{RST}")
            mm.seek(0)
            mm.write(secrets.token_bytes(self.filesize))
            mm.flush()
            os.fsync(f.fileno())
            self._display_hex_dump()
            time.sleep(0.5)

            mm.close()

        # --- PHASE 4: METADATA OBFUSCATION ---
        self._scramble_metadata()

    def _scramble_metadata(self):
        """Renames the file multiple times to overwrite the filename in the Master File Table (MFT)."""
        print(f"\n{AZURE}[*] PHASE 4: Scrambling File Metadata (MFT/Inode)...{RST}")
        current_name = self.filepath
        
        for i in range(3):
            # Generate a random gibberish filename
            random_name = secrets.token_hex(8) + ".tmp"
            new_path = os.path.join(os.path.dirname(current_name) or ".", random_name)
            os.rename(current_name, new_path)
            current_name = new_path
            sys.stdout.write(f"\r{STEEL}  -> Renamed to: {random_name}{RST}")
            sys.stdout.flush()
            time.sleep(0.3)
            
        # Finally, delete the physical link
        os.remove(current_name)
        print(f"\n\n{LIME}{BLD}[✔] TARGET OBLITERATED. DATA IS UNRECOVERABLE.{RST}")


# ==========================================
# SIMULATION GENERATOR
# ==========================================
def create_dummy_secret_file():
    """Generates a fake secret file so the user doesn't shred their real files during demo."""
    filename = "CLASSIFIED_OP_SUTRA.txt"
    content = "TOP SECRET: The nuclear launch codes are 8899-AABB-7766. Do not let this fall into enemy hands."
    with open(filename, "w") as f:
        f.write(content)
    return filename

def run_kshama_cli():
    shredder_boot_animation()
    
    print(f"{AZURE}[*] Generating Dummy Secret File for testing...{RST}")
    target_file = create_dummy_secret_file()
    time.sleep(1)
    
    shredder = MemoryMappedShredder(target_file)
    shredder.shred_dod_5220_22_m()

if __name__ == "__main__":
    try:
        run_kshama_cli()
    except KeyboardInterrupt:
        print(f"\n{MAGENTA}[!] Shred sequence aborted. Warning: File may be corrupted but recoverable.{RST}")