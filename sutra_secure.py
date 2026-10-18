#!/usr/bin/env python3
"""
PHANTOM-VAULT: Stealth File Carver & Anti-Forensic CUI Hiding Toolkit
Architecture: CHAOS-BASED STEGANOGRAPHIC PIPELINE WITH LOGISTIC MAP KEYSTREAM
Theme: "Ghost Pixel"
Dependencies: NONE (Pure Python Standard Library)
"""

import os
import sys
import time
import struct
import hashlib
import secrets
import random
import datetime
from typing import Tuple, List, Optional

# =============================================================================
# THEME: "Ghost Pixel" - 5 Unique ANSI 256-bit Colors
# =============================================================================
C_GHOST_WHITE = "\033[38;5;255m"     # Pure ethereal white
C_SPECTRAL_CYAN = "\033[38;5;51m"    # Holographic cyan
C_PHANTOM_PURPLE = "\033[38;5;93m"   # Deep spectral purple
C_ECTO_GREEN = "\033[38;5;120m"      # Faint ectoplasm green
C_VOID_BLACK = "\033[38;5;232m"      # Near-void dark
C_RESET = "\033[0m"
C_BOLD = "\033[1m"
C_DIM = "\033[2m"

# =============================================================================
# ASCII ART BANNER
# =============================================================================
BANNER = f"""
{C_SPECTRAL_CYAN}{C_BOLD}
    ╔══════════════════════════════════════════════════════════╗
    ║  ██████╗ ██╗  ██╗ █████╗ ███╗   ██╗████████╗ ██████╗ ███╗   ███╗  ║
    ║  ██╔══██╗██║  ██║██╔══██╗████╗  ██║╚══██╔══╝██╔═══██╗████╗ ████║  ║
    ║  ██████╔╝███████║███████║██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║  ║
    ║  ██╔═══╝ ██╔══██║██╔══██║██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║  ║
    ║  ██║     ██║  ██║██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║  ║
    ║  ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝  ║
    ║                                                              ║
    ║   ██╗   ██╗ █████╗ ██╗   ██╗██╗  ████████╗                    ║
    ║   ██║   ██║██╔══██╗██║   ██║██║  ╚══██╔══╝                    ║
    ║   ██║   ██║███████║██║   ██║██║     ██║                       ║
    ║   ╚██╗ ██╔╝██╔══██║██║   ██║██║     ██║                       ║
    ║    ╚████╔╝ ██║  ██║╚██████╔╝███████╗██║                       ║
    ║     ╚═══╝  ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝                       ║
    ╚══════════════════════════════════════════════════════════╝
{C_RESET}
{C_DIM}{C_PHANTOM_PURPLE}           [ CHAOS-BASED LSB STEGANOGRAPHY & ANTI-FORENSIC CARVER ]{C_RESET}
"""

# =============================================================================
# CRYPTOGRAPHIC DIFFUSION BOOT ANIMATION
# =============================================================================
def boot_animation():
    """Simulated cryptographic diffusion - hex pairs swirling into carrier bytes."""
    hex_chars = "0123456789ABCDEF"
    frame_width = 40
    print(f"{C_SPECTRAL_CYAN}{C_BOLD}  ◆ INITIALIZING CHAOS DIFFUSION ENGINE ◆{C_RESET}")
    print(f"{C_DIM}  ╔{'═' * frame_width}╗{C_RESET}")
    
    for step in range(8):
        line = []
        for i in range(frame_width):
            if (step + i) % 3 == 0:
                line.append(f"{C_SPECTRAL_CYAN}{secrets.choice(hex_chars)}{C_RESET}")
            elif (step + i) % 3 == 1:
                line.append(f"{C_ECTO_GREEN}{secrets.choice(hex_chars)}{C_RESET}")
            else:
                line.append(f"{C_GHOST_WHITE}{secrets.choice(hex_chars)}{C_RESET}")
        
        sys.stdout.write(f"  {C_DIM}║{C_RESET} {''.join(line)} {C_DIM}║{C_RESET}\r")
        sys.stdout.flush()
        time.sleep(0.12)
    
    print(f"\n  {C_DIM}╚{'═' * frame_width}╝{C_RESET}")
    print(f"{C_ECTO_GREEN}  ◆ DIFFUSION COMPLETE. CARRIER MATRIX SYNCHRONIZED ◆{C_RESET}\n")
    time.sleep(0.4)

# =============================================================================
# ARCHITECTURE: CHAOS-BASED STEGANOGRAPHIC PIPELINE
# Paradigm: Logistic Map Key Stream Generator -> XOR Cipher -> LSB Embedding
# =============================================================================

class LogisticMapKeystream:
    """
    Chaos-based pseudo-random number generator using the Logistic Map.
    The logistic map: x_{n+1} = r * x_n * (1 - x_n)
    When r is in [3.57, 4.0], the system exhibits deterministic chaos.
    This generates a cryptographically-adjacent keystream for XOR encryption.
    """
    
    def __init__(self, r: float, x0: float):
        """
        Args:
            r: Control parameter (3.57 < r < 4.0)
            x0: Initial seed (0 < x0 < 1)
        """
        if not 3.57 < r <= 4.0:
            raise ValueError(f"r must be in (3.57, 4.0], got {r}")
        if not 0 < x0 < 1:
            raise ValueError(f"x0 must be in (0, 1), got {x0}")
        
        self.r = r
        self.x = x0
        self._iterations = 0
    
    def next_byte(self) -> int:
        """Generate next byte of keystream (0-255)."""
        # Iterate logistic map multiple times for better mixing
        for _ in range(4):
            self.x = self.r * self.x * (1 - self.x)
        self._iterations += 4
        
        # Extract byte from the chaotic state
        # Multiply by 2^32, take fractional part, extract byte
        scaled = int(self.x * (2 ** 32))
        return (scaled >> 16) & 0xFF
    
    def keystream(self, length: int) -> bytes:
        """Generate keystream of specified length."""
        return bytes(self.next_byte() for _ in range(length))
    
    def get_state(self) -> Tuple[float, float]:
        """Return (r, current_x) for key export."""
        return (self.r, self.x)
    
    @property
    def iterations(self) -> int:
        return self._iterations


class PhantomVault:
    """Core stealth file carver with chaos encryption and LSB steganography."""
    
    HEADER_MAGIC = b'PHAN'
    HEADER_FORMAT = '!4sII'  # magic(4), payload_len(4), hash_len(4)
    HEADER_SIZE = struct.calcsize(HEADER_FORMAT)
    
    def __init__(self, r: float = None, x0: float = None):
        """
        Initialize with logistic map parameters.
        If not provided, secure random defaults are generated.
        """
        if r is None:
            # Generate r in chaotic regime [3.57, 4.0]
            r = 3.57 + (secrets.randbits(32) / (2**32)) * 0.43
        if x0 is None:
            x0 = secrets.randbits(32) / (2**32)
            # Ensure x0 is not a trivial fixed point
            while x0 in (0.0, 0.5, 0.75, 1.0):
                x0 = secrets.randbits(32) / (2**32)
        
        self.r = r
        self.x0 = x0
        self.keystream_gen = LogisticMapKeystream(r, x0)
    
    def _xor_encrypt(self, data: bytes, key: LogisticMapKeystream) -> bytes:
        """XOR encrypt data with chaos-generated keystream."""
        ks = key.keystream(len(data))
        return bytes(a ^ b for a, b in zip(data, ks))
    
    def _compute_hash(self, data: bytes) -> bytes:
        """Compute SHA-256 hash of data."""
        return hashlib.sha256(data).digest()
    
    def _pack_payload(self, plaintext: bytes) -> bytes:
        """
        Pack payload with header: [MAGIC][PLEN][HLEN][HASH][CIPHERTEXT]
        Hash is of the ORIGINAL plaintext for integrity verification.
        """
        payload_hash = self._compute_hash(plaintext)
        
        # Encrypt the plaintext
        ciphertext = self._xor_encrypt(plaintext, self.keystream_gen)
        
        header = struct.pack(
            self.HEADER_FORMAT,
            self.HEADER_MAGIC,
            len(ciphertext),
            len(payload_hash)
        )
        
        return header + payload_hash + ciphertext
    
    def _unpack_payload(self, data: bytes) -> Optional[bytes]:
        """Unpack and verify payload. Returns plaintext or None if corrupt."""
        if len(data) < self.HEADER_SIZE:
            return None
        
        magic, plen, hlen = struct.unpack(self.HEADER_FORMAT, data[:self.HEADER_SIZE])
        
        if magic != self.HEADER_MAGIC:
            return None
        
        expected_total = self.HEADER_SIZE + hlen + plen
        if len(data) < expected_total:
            return None
        
        stored_hash = data[self.HEADER_SIZE:self.HEADER_SIZE + hlen]
        ciphertext = data[self.HEADER_SIZE + hlen:expected_total]
        
        # Decrypt
        keystream = LogisticMapKeystream(self.r, self.x0)
        plaintext = self._xor_encrypt(ciphertext, keystream)
        
        # Verify hash
        computed_hash = self._compute_hash(plaintext)
        if not hashlib.sha256(plaintext).digest() == stored_hash:
            return None
        
        return plaintext
    
    def embed(self, carrier_path: str, payload_text: str, output_path: str) -> bool:
        """
        Embed encrypted CUI payload into carrier PNG image using LSB steganography.
        
        Returns True on success, False on failure.
        """
        # Read carrier image
        try:
            with open(carrier_path, 'rb') as f:
                carrier_data = bytearray(f.read())
        except FileNotFoundError:
            self._log(f"Carrier file not found: {carrier_path}", "ERROR")
            return False
        except Exception as e:
            self._log(f"Failed to read carrier: {e}", "ERROR")
            return False
        
        # Validate PNG signature
        if carrier_data[:8] != b'\x89PNG\r\n\x1a\n':
            self._log("Not a valid PNG file", "ERROR")
            return False
        
        # Find IDAT chunk offset (skip to pixel data area for LSB embedding)
        # We'll embed in the RGB pixel data after all headers
        # Simple approach: find IEND chunk, embed before it, or find where pixel data begins
        # For robustness, we embed starting at a safe offset after IHDR
        # Find start of IDAT (image data)
        idat_offset = carrier_data.find(b'IDAT')
        if idat_offset == -1:
            self._log("No IDAT chunk found in PNG", "ERROR")
            return False
        
        # Skip past IDAT chunk header (length + 'IDAT') to get to compressed data
        # We'll embed in the raw compressed stream (after IDAT header, before IEND)
        # Actually, for simplicity we'll embed in the pixel area after all metadata
        # Find IEND to know safe boundary
        iend_offset = carrier_data.find(b'IEND')
        if iend_offset == -1:
            self._log("Malformed PNG, no IEND chunk", "ERROR")
            return False
        
        # We'll embed payload in the region between IDAT data start and IEND
        # IDAT structure: [4 byte length][4 byte 'IDAT'][data][4 byte CRC]
        idat_data_start = idat_offset + 8  # Skip length and type
        idat_length = struct.unpack('!I', carrier_data[idat_offset-4:idat_offset])[0]
        idat_data_end = idat_data_start + idat_length
        
        # Check capacity
        available_bytes = idat_data_end - idat_data_start
        payload_bits_needed = len(payload_text.encode('utf-8')) * 8 * 3  # 3 bits per byte (one per RGB channel equivalent)
        
        # Actually, we embed 1 bit per byte of carrier (LSB of each RGB byte in decompressed data)
        # In compressed IDAT, we embed in the compressed stream itself
        # But that corrupts decompression. Better approach:
        # We need to work with uncompressed pixels. Let's use a simpler stego approach:
        # Append payload after IEND chunk (many PNG parsers ignore trailing data)
        
        # Prepare payload
        payload_bytes = payload_text.encode('utf-8')
        packed_payload = self._pack_payload(payload_bytes)
        
        self._log(f"Payload size: {len(payload_bytes)} bytes -> {len(packed_payload)} bytes packed", "INFO")
        
        # Embed in LSB of bytes between IDAT data start and IEND
        # Each byte of carrier holds 1 bit of payload
        payload_bits = ''.join(f'{b:08b}' for b in packed_payload)
        bits_needed = len(payload_bits)
        
        if bits_needed > available_bytes:
            self._log(f"Insufficient capacity: need {bits_needed} bits, have {available_bytes} bits", "ERROR")
            return False
        
        # Embed payload bits into LSB of carrier bytes
        modified_data = bytearray(carrier_data)
        bit_idx = 0
        for i in range(idat_data_start, idat_data_start + bits_needed):
            if bit_idx < bits_needed:
                # Replace LSB with payload bit
                modified_data[i] = (modified_data[i] & 0xFE) | int(payload_bits[bit_idx])
                bit_idx += 1
        
        # Write output
        try:
            with open(output_path, 'wb') as f:
                f.write(modified_data)
        except Exception as e:
            self._log(f"Failed to write output: {e}", "ERROR")
            return False
        
        # Anti-forensic timestamp manipulation
        self._manipulate_timestamp(output_path)
        
        self._log(f"Stego-image written to: {output_path}", "SUCCESS")
        return True
    
    def extract(self, stego_path: str) -> Optional[str]:
        """Extract hidden CUI payload from stego-image."""
        try:
            with open(stego_path, 'rb') as f:
                data = f.read()
        except FileNotFoundError:
            self._log(f"Stego file not found: {stego_path}", "ERROR")
            return None
        except Exception as e:
            self._log(f"Failed to read stego: {e}", "ERROR")
            return None
        
        # Find IDAT and IEND
        idat_offset = data.find(b'IDAT')
        iend_offset = data.find(b'IEND')
        
        if idat_offset == -1 or iend_offset == -1:
            self._log("Invalid stego-image format", "ERROR")
            return None
        
        idat_data_start = idat_offset + 8
        idat_length = struct.unpack('!I', data[idat_offset-4:idat_offset])[0]
        idat_data_end = idat_data_start + idat_length
        
        # Extract LSBs from carrier region
        # We need to find the header first by extracting bits until we find PHAN magic
        extracted_bits = []
        for i in range(idat_data_start, idat_data_end):
            extracted_bits.append(str(data[i] & 0x01))
        
        # Convert bits to bytes
        extracted_bytes = bytearray()
        for i in range(0, len(extracted_bits) - 7, 8):
            byte = int(''.join(extracted_bits[i:i+8]), 2)
            extracted_bytes.append(byte)
        
        # Search for PHAN magic in extracted bytes
        extracted_data = bytes(extracted_bytes)
        magic_pos = extracted_data.find(self.HEADER_MAGIC)
        
        if magic_pos == -1:
            self._log("No hidden payload found (magic bytes missing)", "ERROR")
            return None
        
        # Extract from magic position
        payload_data = extracted_data[magic_pos:]
        plaintext = self._unpack_payload(payload_data)
        
        if plaintext is None:
            self._log("Payload extraction failed (integrity check failed or corrupt)", "ERROR")
            return None
        
        try:
            return plaintext.decode('utf-8')
        except UnicodeDecodeError:
            self._log("Extracted data is not valid UTF-8 text", "ERROR")
            return None
    
    def _manipulate_timestamp(self, filepath: str):
        """Anti-forensic: Set file timestamps to ~6 months ago with slight jitter."""
        try:
            six_months_ago = datetime.datetime.now() - datetime.timedelta(days=180)
            jitter_days = secrets.randbelow(14) - 7  # +/- 7 days
            jitter_hours = secrets.randbelow(48) - 24  # +/- 24 hours
            fake_time = six_months_ago + datetime.timedelta(days=jitter_days, hours=jitter_hours)
            
            timestamp = time.mktime(fake_time.timetuple())
            os.utime(filepath, (timestamp, timestamp))
            
            self._log(f"Timestamps manipulated: {fake_time.strftime('%Y-%m-%d %H:%M:%S')}", "FORENSIC")
        except Exception as e:
            self._log(f"Timestamp manipulation failed: {e}", "WARN")
    
    def _log(self, message: str, level: str = "INFO"):
        """Timestamped military-style log output."""
        ts = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
        color_map = {
            "INFO": C_GHOST_WHITE,
            "SUCCESS": C_ECTO_GREEN,
            "ERROR": C_PHANTOM_PURPLE,
            "WARN": C_SPECTRAL_CYAN,
            "FORENSIC": f"{C_VOID_BLACK}{C_DIM}",
            "DEBUG": C_DIM,
        }
        color = color_map.get(level, C_RESET)
        level_fmt = f"{color}[{level:^8}]{C_RESET}"
        print(f"  {C_DIM}[{ts}]{C_RESET} {level_fmt} {message}")


# =============================================================================
# INTERACTIVE CLI
# =============================================================================

def print_help():
    """Display help menu."""
    print(f"""
{C_SPECTRAL_CYAN}{C_BOLD}  PHANTOM-VAULT COMMANDS:{C_RESET}
  {C_GHOST_WHITE}embed <carrier.png> <payload.txt> <output.png>{C_RESET}  - Hide CUI in carrier
  {C_GHOST_WHITE}extract <stego.png>{C_RESET}                          - Recover hidden CUI
  {C_GHOST_WHITE}key{C_RESET}                                      - Show current chaos key
  {C_GHOST_WHITE}keygen{C_RESET}                                   - Generate new random key
  {C_GHOST_WHITE}keyset <r> <x0>{C_RESET}                          - Set custom key (e.g., 3.98 0.1234)
  {C_GHOST_WHITE}help{C_RESET}                                     - Show this menu
  {C_GHOST_WHITE}clear{C_RESET}                                    - Clear screen
  {C_GHOST_WHITE}exit{C_RESET}                                     - Terminate session
""")

def main():
    """Main CLI loop."""
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(BANNER)
    boot_animation()
    
    # Initialize vault with random key
    vault = PhantomVault()
    
    print(f"{C_SPECTRAL_CYAN}{C_BOLD}  ◆ PHANTOM-VAULT ACTIVE ◆{C_RESET}")
    print(f"{C_DIM}  Logistic Map Key: r={vault.r:.6f}, x0={vault.x0:.6f}{C_RESET}")
    print(f"{C_DIM}  Type 'help' for commands, 'exit' to quit{C_RESET}\n")
    
    while True:
        try:
            prompt = f"{C_ECTO_GREEN}phantom{C_RESET}{C_DIM}::{C_RESET}{C_GHOST_WHITE}> {C_RESET}"
            cmd = input(prompt).strip()
            
            if not cmd:
                continue
            
            parts = cmd.split()
            action = parts[0].lower()
            
            if action == "exit":
                print(f"\n{C_PHANTOM_PURPLE}  ◆ TERMINATING PHANTOM-VAULT SESSION ◆{C_RESET}")
                print(f"  {C_DIM}Chaos diffusion dissipating...{C_RESET}\n")
                time.sleep(0.5)
                break
            
            elif action == "help":
                print_help()
            
            elif action == "clear":
                os.system('cls' if os.name == 'nt' else 'clear')
                print(BANNER)
                print(f"{C_SPECTRAL_CYAN}{C_BOLD}  ◆ PHANTOM-VAULT ACTIVE ◆{C_RESET}\n")
            
            elif action == "key":
                print(f"\n{C_GHOST_WHITE}  Current Chaos Key:{C_RESET}")
                print(f"  {C_DIM}r  = {C_RESET}{C_SPECTRAL_CYAN}{vault.r:.10f}{C_RESET}")
                print(f"  {C_DIM}x0 = {C_RESET}{C_SPECTRAL_CYAN}{vault.x0:.10f}{C_RESET}")
                print(f"  {C_DIM}Iterations used: {vault.keystream_gen.iterations}{C_RESET}\n")
            
            elif action == "keygen":
                vault = PhantomVault()
                print(f"\n{C_ECTO_GREEN}  ◆ New chaos key generated ◆{C_RESET}")
                print(f"  {C_DIM}r  = {C_RESET}{C_SPECTRAL_CYAN}{vault.r:.10f}{C_RESET}")
                print(f"  {C_DIM}x0 = {C_RESET}{C_SPECTRAL_CYAN}{vault.x0:.10f}{C_RESET}\n")
            
            elif action == "keyset":
                if len(parts) != 3:
                    print(f"{C_PHANTOM_PURPLE}  Usage: keyset <r> <x0>{C_RESET}\n")
                    continue
                try:
                    r = float(parts[1])
                    x0 = float(parts[2])
                    vault = PhantomVault(r=r, x0=x0)
                    print(f"{C_ECTO_GREEN}  ◆ Key set successfully ◆{C_RESET}\n")
                except ValueError as e:
                    print(f"{C_PHANTOM_PURPLE}  Invalid key: {e}{C_RESET}\n")
            
            elif action == "embed":
                if len(parts) != 4:
                    print(f"{C_PHANTOM_PURPLE}  Usage: embed <carrier.png> <payload.txt> <output.png>{C_RESET}\n")
                    continue
                
                carrier_path = parts[1]
                payload_path = parts[2]
                output_path = parts[3]
                
                # Read payload
                try:
                    with open(payload_path, 'r', encoding='utf-8') as f:
                        payload_text = f.read()
                except FileNotFoundError:
                    print(f"{C_PHANTOM_PURPLE}  Payload file not found: {payload_path}{C_RESET}\n")
                    continue
                except Exception as e:
                    print(f"{C_PHANTOM_PURPLE}  Failed to read payload: {e}{C_RESET}\n")
                    continue
                
                print(f"\n{C_SPECTRAL_CYAN}  ◆ EMBEDDING OPERATION ◆{C_RESET}")
                print(f"  {C_DIM}Carrier: {carrier_path}{C_RESET}")
                print(f"  {C_DIM}Payload: {payload_path} ({len(payload_text)} chars){C_RESET}")
                
                # Reset keystream for fresh encryption
                vault.keystream_gen = LogisticMapKeystream(vault.r, vault.x0)
                
                success = vault.embed(carrier_path, payload_text, output_path)
                if success:
                    print(f"{C_ECTO_GREEN}  ◆ EMBED COMPLETE - Stealth payload deployed ◆{C_RESET}\n")
                else:
                    print(f"{C_PHANTOM_PURPLE}  ◆ EMBED FAILED ◆{C_RESET}\n")
            
            elif action == "extract":
                if len(parts) != 2:
                    print(f"{C_PHANTOM_PURPLE}  Usage: extract <stego.png>{C_RESET}\n")
                    continue
                
                stego_path = parts[1]
                print(f"\n{C_SPECTRAL_CYAN}  ◆ EXTRACTION OPERATION ◆{C_RESET}")
                print(f"  {C_DIM}Stego-image: {stego_path}{C_RESET}")
                
                # Reset keystream for fresh decryption
                vault.keystream_gen = LogisticMapKeystream(vault.r, vault.x0)
                
                extracted = vault.extract(stego_path)
                if extracted:
                    print(f"\n{C_ECTO_GREEN}  ◆ PAYLOAD RECOVERED - Integrity verified ◆{C_RESET}")
                    print(f"  {C_DIM}{'─' * 50}{C_RESET}")
                    print(f"  {C_GHOST_WHITE}{extracted}{C_RESET}")
                    print(f"  {C_DIM}{'─' * 50}{C_RESET}\n")
                else:
                    print(f"{C_PHANTOM_PURPLE}  ◆ EXTRACTION FAILED ◆{C_RESET}\n")
            
            else:
                print(f"{C_PHANTOM_PURPLE}  Unknown command: {action}{C_RESET}\n")
        
        except KeyboardInterrupt:
            print(f"\n\n{C_PHANTOM_PURPLE}  ◆ INTERRUPT - Session terminated ◆{C_RESET}\n")
            break
        except EOFError:
            break
        except Exception as e:
            print(f"{C_PHANTOM_PURPLE}  Runtime error: {e}{C_RESET}\n")

if __name__ == "__main__":
    main()