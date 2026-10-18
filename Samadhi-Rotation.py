import os
import time
import sys
import secrets
import hashlib
import base64
import threading

# ==========================================
# SAMADHI-ROTATION: COSMIC 20-COLOR PALETTE
# (Strictly 20 unique non-repeating ANSI colors)
# ==========================================
C1  = '\033[38;5;17m'  # Abyss Blue
C2  = '\033[38;5;53m'  # Deep Purple
C3  = '\033[38;5;89m'  # Wine Red
C4  = '\033[38;5;125m' # Dark Magenta
C5  = '\033[38;5;161m' # Ruby
C6  = '\033[38;5;197m' # Neon Pink
C7  = '\033[38;5;203m' # Coral
C8  = '\033[38;5;209m' # Orange
C9  = '\033[38;5;215m' # Bright Peach
C10 = '\033[38;5;221m' # Gold
C11 = '\033[38;5;227m' # Yellow
C12 = '\033[38;5;191m' # Yellow-Green
C13 = '\033[38;5;155m' # Lime
C14 = '\033[38;5;119m' # Mint
C15 = '\033[38;5;83m'  # Sea Green
C16 = '\033[38;5;47m'  # Spring Green
C17 = '\033[38;5;45m'  # Cyan
C18 = '\033[38;5;33m'  # Azure
C19 = '\033[38;5;27m'  # Blue
C20 = '\033[38;5;255m' # Pure White
RST = '\033[0m'
BLD = '\033[1m'

# ==========================================
# ANIMATION: THE 20-COLOR CHAKRA SPIN
# ==========================================
def samadhi_boot_animation():
    os.system('cls' if os.name == 'nt' else 'clear')
    palette = [C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14, C15, C16, C17, C18, C19, C20]
    
    print(f"{C20}{BLD}>> INITIALIZING SAMADHI KEY ROTATION ENGINE <<{RST}\n")
    
    # Render a multi-color spectrum bar
    sys.stdout.write("  ")
    for color in palette:
        sys.stdout.write(f"{color}██{RST}")
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n")
    
    # Render Samadhi ASCII
    ascii_art = [
        f"       {C14}.{C15}o{C16}O{C17}0{C18}O{C19}o{C20}.       ",
        f"     {C12}o{C20} SAMADHI  {C1}o     ",
        f"   {C11}O{C20}  EPOCH-RING  {C2}O   ",
        f"     {C10}o{C20} K M S v1 {C3}o     ",
        f"       {C9}.{C8}o{C7}O{C6}0{C5}O{C4}o{C3}.       "
    ]
    
    for line in ascii_art:
        print(line)
        time.sleep(0.1)
    print(f"\n{C16}[+] Engine Synchronized with Cryptographic Time-Wheel.{RST}\n")

# ==========================================
# ARCHITECTURE: EPOCH KEYRING & TOMBSTONING
# ==========================================
class EpochKey:
    """Represents a single cryptographic key for a specific time window."""
    def __init__(self, version_id):
        self.version = version_id
        self.material = secrets.token_bytes(32)
        self.status = "ACTIVE" # States: ACTIVE, RETIRED, REVOKED
        self.created_at = time.strftime("%H:%M:%S")

class SamadhiKeyRing:
    """Manages the lifecycle, rotation, and tombstoning of encryption keys."""
    def __init__(self):
        self.keys = {}
        self.active_version = 0
        self.rotate_key() # Initialize Epoch 1

    def rotate_key(self):
        """Generates a new key and retires the old one (Tombstoning)."""
        # Retire the current active key if it exists
        if self.active_version > 0:
            self.keys[self.active_version].status = "RETIRED"
            
        # Create new active key
        self.active_version += 1
        new_key = EpochKey(self.active_version)
        self.keys[self.active_version] = new_key
        
        # UI Log (Background thread safe print)
        sys.stdout.write(f"\r\033[K{C11}[AUTORUN] {C16}System Rotated to Epoch {self.active_version}. Older keys Tombstoned.{RST}\n> ")
        sys.stdout.flush()

    def get_key_for_encryption(self):
        """Always returns the currently active key for new data."""
        return self.keys[self.active_version]

    def get_key_for_decryption(self, version):
        """Fetches historical keys to read old data, unless compromised."""
        key = self.keys.get(version)
        if not key:
            raise ValueError(f"Epoch {version} key not found in KeyRing.")
        if key.status == "REVOKED":
            raise PermissionError(f"CRITICAL: Epoch {version} key was COMPROMISED and REVOKED.")
        return key

    def revoke_key(self, version):
        """Permanently destroys a key if a breach is suspected."""
        if version in self.keys:
            self.keys[version].status = "REVOKED"
            self.keys[version].material = b'\x00' * 32 # Cryptographic wipe

# ==========================================
# ENCRYPTION / DECRYPTION ENGINE
# ==========================================
class StreamCipherEngine:
    """Uses the KeyRing to encrypt/decrypt with versioned headers."""
    
    @staticmethod
    def process_bytes(data: bytes, key: bytes) -> bytes:
        result = bytearray()
        for i in range(len(data)):
            stream = hashlib.sha256(key + i.to_bytes(4, 'big')).digest()
            result.append(data[i] ^ stream[i % 32])
        return bytes(result)

    @staticmethod
    def encrypt(text: str, keyring: SamadhiKeyRing) -> str:
        # Get the CURRENT active key
        current_key = keyring.get_key_for_encryption()
        ciphertext = StreamCipherEngine.process_bytes(text.encode(), current_key.material)
        b64_data = base64.b64encode(ciphertext).decode()
        
        # Format: [EPOCH_ID]:[CIPHERTEXT]
        return f"EPOCH_{current_key.version}:{b64_data}"

    @staticmethod
    def decrypt(payload: str, keyring: SamadhiKeyRing) -> str:
        try:
            # Extract the Epoch ID from the header
            header, b64_data = payload.split(':', 1)
            version = int(header.split('_')[1])
            
            # Fetch the SPECIFIC historical key needed for this file
            target_key = keyring.get_key_for_decryption(version)
            
            ciphertext = base64.b64decode(b64_data)
            plaintext = StreamCipherEngine.process_bytes(ciphertext, target_key.material)
            return plaintext.decode()
        except Exception as e:
            return f"{C6}ERROR: {e}{RST}"

# ==========================================
# DAEMON ROTATION SCHEDULER
# ==========================================
def background_rotator(keyring, interval=20):
    """Simulates a cron job that automatically rotates keys every X seconds."""
    while True:
        time.sleep(interval)
        keyring.rotate_key()

# ==========================================
# INTERACTIVE CLI
# ==========================================
def run_cli():
    samadhi_boot_animation()
    keyring = SamadhiKeyRing()
    engine = StreamCipherEngine()
    
    # Start auto-rotation daemon (Runs every 20 seconds for demo)
    t = threading.Thread(target=background_rotator, args=(keyring, 20), daemon=True)
    t.start()
    
    print(f"{C20}--- SAMADHI CONSOLE ---{RST}")
    print(f"{C17}Commands: {C18}encrypt <txt>{C17}, {C18}decrypt <hash>{C17}, {C18}status{C17}, {C18}revoke <id>{C17}, {C6}exit{RST}\n")
    
    while True:
        try:
            cmd_raw = input(f"{C10}> {RST}").strip().split(maxsplit=1)
            if not cmd_raw: continue
            
            cmd = cmd_raw[0].lower()
            arg = cmd_raw[1] if len(cmd_raw) > 1 else ""
            
            if cmd == "encrypt":
                if not arg: print(f"{C8}Usage: encrypt <text>{RST}"); continue
                enc_data = engine.encrypt(arg, keyring)
                print(f"{C14}[+] Encrypted Payload: {C20}{enc_data}{RST}")
                
            elif cmd == "decrypt":
                if not arg: print(f"{C8}Usage: decrypt <payload>{RST}"); continue
                dec_data = engine.decrypt(arg, keyring)
                print(f"{C16}[*] Decrypted Text: {C20}{BLD}{dec_data}{RST}")
                
            elif cmd == "status":
                print(f"\n{C20}┌──[ KEYRING VAULT STATUS ]{'─'*20}{RST}")
                for v, k in keyring.keys.items():
                    color = C14 if k.status == "ACTIVE" else (C8 if k.status == "RETIRED" else C6)
                    print(f"{C20}│ {C18}Epoch {v} {C20}| {color}{k.status:<8}{C20} | Created: {k.created_at}{RST}")
                print(f"{C20}└{'─'*46}{RST}\n")
                
            elif cmd == "revoke":
                if not arg.isdigit(): print(f"{C8}Usage: revoke <epoch_number>{RST}"); continue
                keyring.revoke_key(int(arg))
                print(f"{C6}[!] CRITICAL: Epoch {arg} Key has been cryptographically wiped.{RST}")
                
            elif cmd == "exit":
                print(f"{C5}[*] Terminating Samadhi Cycles. Goodbye.{RST}")
                break
            else:
                print(f"{C8}[!] Unknown command.{RST}")
                
        except KeyboardInterrupt:
            print(f"\n{C6}[!] Aborted by user.{RST}")
            break

if __name__ == "__main__":
    run_cli()