import os
import sys
import time
import secrets
import hashlib
import json
import base64
import random

# ==========================================
# SHANKAR-PGP: THE TRIDENT THEME
# (5 Unique Non-Repeating Colors)
# ==========================================
BHASMA = '\033[38;5;251m'  # Ash White
RUDRA  = '\033[38;5;130m'  # Brown
GANGA  = '\033[38;5;81m'   # Cyan
KALA   = '\033[38;5;88m'   # Dark Red
SILVR  = '\033[38;5;145m'  # Silver/Grey
RST    = '\033[0m'
BLD    = '\033[1m'

# ==========================================
# ANIMATION: OPENING THE THIRD EYE
# ==========================================
def trishul_boot_animation():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    trishul_ascii = [
        f"{SILVR}       _/\_       {RST}",
        f"{SILVR}      \\  |  /      {RST}",
        f"{SILVR}       \\ | /       {RST}",
        f"{RUDRA}       --|--       {RST}",
        f"{RUDRA}         |         {RST}  {GANGA}S H A N K A R{RST}",
        f"{RUDRA}         |         {RST}  {BHASMA}PGP Encryption Wrapper{RST}"
    ]
    
    for line in trishul_ascii:
        print(line)
        time.sleep(0.1)
        
    sys.stdout.write(f"\n{BHASMA}[*] Generating Mathematical Primes ")
    sys.stdout.flush()
    for _ in range(5):
        sys.stdout.write(f"{GANGA}.{RST}")
        sys.stdout.flush()
        time.sleep(0.2)
    print(f" {SILVR}[OK]{RST}\n")

# ==========================================
# ARCHITECTURE: HYBRID CRYPTOSYSTEM (RSA + STREAM)
# ==========================================
class RSAMathEngine:
    """Pure Python Asymmetric Cryptography Simulation (RSA)."""
    @staticmethod
    def _is_prime(num):
        if num < 2: return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0: return False
        return True

    @staticmethod
    def generate_keypair():
        """Generates Public (e, n) and Private (d, n) keys using math."""
        # 1. Pick two random primes (Small for terminal speed, math is same as 2048-bit)
        primes = [i for i in range(100, 1000) if RSAMathEngine._is_prime(i)]
        p, q = random.sample(primes, 2)
        
        n = p * q
        phi = (p - 1) * (q - 1)
        
        # 2. Choose public exponent 'e' (typically 65537, we use a smaller co-prime)
        e = 3
        while phi % e == 0:
            e += 2
            
        # 3. Calculate modular inverse for private key 'd'
        d = pow(e, -1, phi) 
        
        # Format keys into Hex for PGP-like appearance
        public_key = f"{hex(e)[2:]}:{hex(n)[2:]}"
        private_key = f"{hex(d)[2:]}:{hex(n)[2:]}"
        
        return public_key, private_key

class ShankarPGPWrapper:
    """Combines Asymmetric RSA Key Encapsulation with Symmetric Encryption."""
    
    @staticmethod
    def _stream_cipher(data: bytes, key: bytes) -> bytes:
        """Symmetric encryption for the actual document payload."""
        result = bytearray()
        for i in range(len(data)):
            stream = hashlib.sha256(key + i.to_bytes(4, 'big')).digest()
            result.append(data[i] ^ stream[i % 32])
        return bytes(result)

    def encrypt_message(self, message: str, public_key_hex: str) -> str:
        """
        1. Generate random session key.
        2. Encrypt document with session key.
        3. Encrypt session key with Asymmetric Public Key.
        """
        e_hex, n_hex = public_key_hex.split(':')
        e, n = int(e_hex, 16), int(n_hex, 16)
        
        print(f"{BHASMA}│ {SILVR}Generating ephemeral symmetric session key...{RST}")
        session_key = secrets.token_bytes(32)
        
        print(f"{BHASMA}│ {SILVR}Encrypting document payload...{RST}")
        encrypted_doc = self._stream_cipher(message.encode(), session_key)
        
        print(f"{BHASMA}│ {GANGA}Encapsulating session key with RSA Public Key...{RST}")
        session_key_int = int.from_bytes(session_key, 'big')
        enc_session_key_int = pow(session_key_int, e, n) # RSA Math: (m^e) mod n
        enc_session_key_hex = hex(enc_session_key_int)[2:]
        
        # Build the final payload
        payload = {
            "session_key": enc_session_key_hex,
            "data": base64.b64encode(encrypted_doc).decode()
        }
        
        # Create PGP ASCII Armor
        raw_b64 = base64.b64encode(json.dumps(payload).encode()).decode()
        armor = f"-----BEGIN SHANKAR PGP MESSAGE-----\nVersion: 1.0.0\n\n"
        # Wrap at 64 characters
        for i in range(0, len(raw_b64), 64):
            armor += raw_b64[i:i+64] + "\n"
        armor += "-----END SHANKAR PGP MESSAGE-----"
        
        return armor

    def decrypt_message(self, ascii_armor: str, private_key_hex: str) -> str:
        """Decrypts the session key using Private Key, then decrypts the document."""
        try:
            d_hex, n_hex = private_key_hex.split(':')
            d, n = int(d_hex, 16), int(n_hex, 16)
            
            print(f"{BHASMA}│ {SILVR}Stripping ASCII Armor...{RST}")
            # Extract base64 part
            b64_data = "".join(ascii_armor.split('\n')[3:-1])
            payload = json.loads(base64.b64decode(b64_data).decode())
            
            print(f"{BHASMA}│ {KALA}Decapsulating session key with RSA Private Key...{RST}")
            enc_session_key_int = int(payload["session_key"], 16)
            session_key_int = pow(enc_session_key_int, d, n) # RSA Math: (c^d) mod n
            
            # Reconstruct the 32-byte session key
            session_key = session_key_int.to_bytes(32, 'big')
            
            print(f"{BHASMA}│ {SILVR}Decrypting document payload...{RST}")
            encrypted_doc = base64.b64decode(payload["data"])
            decrypted_doc = self._stream_cipher(encrypted_doc, session_key)
            
            return decrypted_doc.decode()
        except Exception as e:
            return f"{KALA}DECRYPTION FAILED. Invalid Private Key or corrupted data. ({e}){RST}"

# ==========================================
# INTERACTIVE CLI SHELL
# ==========================================
def run_pgp_cli():
    trishul_boot_animation()
    pgp = ShankarPGPWrapper()
    
    print(f"{RUDRA}┌──[ STEP 1: KEY GENERATION ]{'─'*30}{RST}")
    print(f"{BHASMA}│ Generating Asymmetric Keypair...{RST}")
    pub_key, priv_key = RSAMathEngine.generate_keypair()
    
    print(f"{BHASMA}│ {BLD}Your Public Key (Share with sender):{RST}\n{BHASMA}│ {GANGA}{pub_key}{RST}")
    print(f"{BHASMA}│ {BLD}Your Private Key (KEEP SECRET!):{RST}\n{BHASMA}│ {KALA}{priv_key}{RST}")
    print(f"{RUDRA}└{'─'*56}{RST}\n")
    
    time.sleep(1)
    
    # --- ENCRYPTION PHASE ---
    print(f"{RUDRA}┌──[ STEP 2: ENCRYPTION (SENDER) ]{'─'*25}{RST}")
    secret_message = input(f"{BHASMA}│ Enter secret CUI message: {SILVR}")
    print(f"{BHASMA}│ Using Receiver's Public Key: {GANGA}{pub_key}{RST}")
    
    armored_message = pgp.encrypt_message(secret_message, pub_key)
    print(f"{RUDRA}└{'─'*56}{RST}")
    
    print(f"\n{SILVR}{armored_message}{RST}\n")
    time.sleep(1)
    
    # --- DECRYPTION PHASE ---
    print(f"{RUDRA}┌──[ STEP 3: DECRYPTION (RECEIVER) ]{'─'*23}{RST}")
    print(f"{BHASMA}│ Receiver applies their Private Key: {KALA}{priv_key}{RST}")
    
    decrypted_msg = pgp.decrypt_message(armored_message, priv_key)
    
    print(f"{BHASMA}│ {BLD}RECOVERED MESSAGE: {GANGA}{decrypted_msg}{RST}")
    print(f"{RUDRA}└{'─'*56}{RST}\n")

if __name__ == "__main__":
    run_pgp_cli()