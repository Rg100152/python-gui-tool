import os
import sys
import time
import hashlib
import hmac
import secrets
import base64

# ==========================================
# RAJ-CRYPTO: MILITARY CIPHER THEME
# ==========================================
D_ASH  = '\033[38;5;238m'  
BLOOD  = '\033[38;5;124m'  
MINT   = '\033[38;5;48m'   
PURP   = '\033[38;5;55m'   
ICE    = '\033[38;5;117m'  
RST    = '\033[0m'
BLD    = '\033[1m'

# ==========================================
# ANIMATION: CRYPTOGRAPHIC LOCK
# ==========================================
def lock_animation():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{PURP}{BLD}>> INITIATING MILITARY-GRADE ENCRYPTION ENGINE <<{RST}")
    
    lock_frames = [
        "[ / ] Generating PBKDF2 Keys...",
        "[ - ] Salting Entropy Pools...",
        "[ \\ ] Calculating HMAC Signatures...",
        "[ | ] Securing Payload..."
    ]
    for frame in lock_frames:
        sys.stdout.write(f"\r{ICE}{frame}{RST}")
        sys.stdout.flush()
        time.sleep(0.4)
    print(f"\r{MINT}[+] CRYPTO ENGINE SECURED AND ONLINE.       {RST}\n")

# ==========================================
# ARCHITECTURE: AUTHENTICATED ENCRYPTION (ENCRYPT-THEN-MAC)
# ==========================================

class RajCryptoProtocol:
    """
    Implements a custom stream cipher with HMAC-SHA256 authentication.
    Simulates AES-256-GCM behavior using strictly Python built-ins.
    """
    def __init__(self):
        self.ITERATIONS = 100_000 # High iteration count to thwart Brute-Force
        self.HASH_ALGO = 'sha256'

    def _derive_keys(self, password: str, salt: bytes):
        """
        Derives two separate 256-bit keys from one password:
        1. Encryption Key (for data)
        2. MAC Key (for integrity signature)
        """
        master_key = hashlib.pbkdf2_hmac(
            self.HASH_ALGO, password.encode(), salt, self.ITERATIONS, dklen=64
        )
        return master_key[:32], master_key[32:] # Split into two 32-byte (256-bit) keys

    def encrypt(self, plaintext: str, password: str) -> str:
        """Encrypts data and generates a tamper-proof HMAC signature."""
        print(f"{D_ASH}│ {ICE}Generating Cryptographic Salt...{RST}")
        salt = secrets.token_bytes(16)
        nonce = secrets.token_bytes(16) # Prevents pattern recognition
        
        print(f"{D_ASH}│ {ICE}Deriving 256-bit Keys via PBKDF2...{RST}")
        enc_key, mac_key = self._derive_keys(password, salt)
        
        # Simulated AES-CTR (Stream Cipher using SHA256 as PRF)
        pt_bytes = plaintext.encode()
        ciphertext = bytearray()
        
        print(f"{D_ASH}│ {PURP}Streaming Cipher Encryption...{RST}")
        for i in range(len(pt_bytes)):
            # Generate keystream block
            counter = i.to_bytes(4, 'big')
            stream_block = hashlib.sha256(enc_key + nonce + counter).digest()
            # XOR plaintext with keystream
            ciphertext.append(pt_bytes[i] ^ stream_block[i % 32])

        print(f"{D_ASH}│ {PURP}Generating HMAC-SHA256 Signature...{RST}")
        signature = hmac.new(mac_key, salt + nonce + ciphertext, hashlib.sha256).digest()
        
        # Package: [SALT (16)] + [NONCE (16)] + [MAC (32)] + [CIPHERTEXT]
        payload = salt + nonce + signature + ciphertext
        return base64.b64encode(payload).decode('utf-8')

    def decrypt(self, encoded_payload: str, password: str) -> str:
        """Authenticates and decrypts the package."""
        try:
            payload = base64.b64decode(encoded_payload.encode('utf-8'))
            
            # Unpack the fixed-length headers
            salt = payload[:16]
            nonce = payload[16:32]
            signature = payload[32:64]
            ciphertext = payload[64:]
            
            enc_key, mac_key = self._derive_keys(password, salt)
            
            print(f"{D_ASH}│ {ICE}Verifying HMAC Signature (Integrity Check)...{RST}")
            expected_signature = hmac.new(mac_key, salt + nonce + ciphertext, hashlib.sha256).digest()
            
            # Constant-time comparison prevents Timing Attacks
            if not hmac.compare_digest(signature, expected_signature):
                raise ValueError("TAMPERING DETECTED: MAC Signature Verification Failed!")
            
            print(f"{D_ASH}│ {MINT}Signature Valid. Decrypting Ciphertext...{RST}")
            pt_bytes = bytearray()
            for i in range(len(ciphertext)):
                counter = i.to_bytes(4, 'big')
                stream_block = hashlib.sha256(enc_key + nonce + counter).digest()
                pt_bytes.append(ciphertext[i] ^ stream_block[i % 32])
                
            return pt_bytes.decode('utf-8')
            
        except Exception as e:
            print(f"{D_ASH}│ {BLOOD}{BLD}[FATAL] {e}{RST}")
            return None

# ==========================================
# EXECUTION & DEMO
# ==========================================
if __name__ == "__main__":
    lock_animation()
    crypto = RajCryptoProtocol()
    
    secret_data = "CUI_BLUEPRINT: Project Vajra source code and API keys."
    password = "SuperSecretPassword123"
    
    print(f"{D_ASH}┌──[ ENCRYPTION PHASE ]{'─'*40}{RST}")
    encrypted_data = crypto.encrypt(secret_data, password)
    print(f"{D_ASH}│ {MINT}SUCCESS: Data mathematically locked.{RST}")
    print(f"{D_ASH}└{'─'*62}{RST}")
    
    print(f"\n{ICE}[BASE64 CIPHERTEXT]:\n{encrypted_data[:60]}...{RST}\n")
    
    time.sleep(1)
    
    print(f"{D_ASH}┌──[ DECRYPTION PHASE (Valid Password) ]{'─'*25}{RST}")
    decrypted_data = crypto.decrypt(encrypted_data, password)
    print(f"{D_ASH}│ {MINT}RECOVERED DATA:{RST} {decrypted_data}")
    print(f"{D_ASH}└{'─'*62}{RST}")
    
    time.sleep(1)
    
    # Simulating a Hacker Tampering with the Ciphertext (Changing 1 letter)
    print(f"\n{BLOOD}{BLD}[!] SIMULATING HACKER TAMPERING (Bit-Flipping Attack)...{RST}")
    tampered_data = encrypted_data[:-5] + "XXXXX" 
    
    print(f"{D_ASH}┌──[ DECRYPTION PHASE (Tampered Data) ]{'─'*26}{RST}")
    failed_data = crypto.decrypt(tampered_data, password)
    print(f"{D_ASH}└{'─'*62}{RST}")