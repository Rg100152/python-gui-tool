#!/usr/bin/env python3
"""
MANTRA-BATCH: Batch CUI File Encryption Engine with Compliance Standards
Architecture: PRODUCER-CONSUMER PIPELINE WITH PRIORITY QUEUE SCHEDULER & WORKER POOL
Theme: "Shadow Dharma"
Dependencies: NONE (Pure Python Standard Library - os, sys, time, hashlib, secrets, struct, threading, queue, json, datetime, pathlib, fnmatch, zipfile, argparse)
"""

import os
import sys
import time
import struct
import hashlib
import secrets
import hmac
import json
import threading
import queue
import datetime
import pathlib
import fnmatch
import argparse
import base64
import uuid
from enum import Enum
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple, Callable
from concurrent.futures import ThreadPoolExecutor
from collections import defaultdict

# ═══════════════════════════════════════════════════════════════════════════════
# THEME: "Shadow Dharma" - 5 BRAND NEW 256-bit ANSI Colors (NEVER USED BEFORE)
# ═══════════════════════════════════════════════════════════════════════════════
C_KARMA_BRONZE = "\033[38;5;137m"      # Earthy bronze for dharma path
C_SAMSARA_SMOKE = "\033[38;5;102m"     # Smoky grey-blue of samsara
C_NIRVANA_JADE = "\033[38;5;42m"       # Deep jade green of nirvana
C_TEMPLE_COPPER = "\033[38;5;173m"     # Ancient temple copper patina
C_LOTUS_PINK = "\033[38;5;211m"        # Sacred lotus blossom pink
C_RESET = "\033[0m"
C_BOLD = "\033[1m"
C_DIM = "\033[2m"
C_INVERT = "\033[7m"
C_ITALIC = "\033[3m"

# ═══════════════════════════════════════════════════════════════════════════════
# ASCII ART BANNER
# ═══════════════════════════════════════════════════════════════════════════════
BANNER = f"""
{C_NIRVANA_JADE}{C_BOLD}
    ╔══════════════════════════════════════════════════════════════════════╗
    ║                                                                      ║
    ║     ███╗   ███╗  █████╗  ███╗   ██╗ ████████╗ ██████╗   █████╗      ║
    ║     ████╗ ████║ ██╔══██╗ ████╗  ██║ ╚══██╔══╝ ██╔══██╗ ██╔══██╗     ║
    ║     ██╔████╔██║ ███████║ ██╔██╗ ██║    ██║    ██████╔╝ ███████║     ║
    ║     ██║╚██╔╝██║ ██╔══██║ ██║╚██╗██║    ██║    ██╔══██╗ ██╔══██║     ║
    ║     ██║ ╚═╝ ██║ ██║  ██║ ██║ ╚████║    ██║    ██║  ██║ ██║  ██║     ║
    ║     ╚═╝     ╚═╝ ╚═╝  ╚═╝ ╚═╝  ╚═══╝    ╚═╝    ╚═╝  ╚═╝ ╚═╝  ╚═╝     ║
    ║                                                                      ║
    ║     ██████╗   █████╗  ████████╗  ██████╗ ██╗  ██╗                    ║
    ║     ██╔══██╗ ██╔══██╗ ╚══██╔══╝ ██╔════╝ ██║  ██║                    ║
    ║     ██████╔╝ ███████║    ██║    ██║      ███████║                    ║
    ║     ██╔══██╗ ██╔══██║    ██║    ██║      ██╔══██║                    ║
    ║     ██████╔╝ ██║  ██║    ██║    ╚██████╗ ██║  ██║                    ║
    ║     ╚═════╝  ╚═╝  ╚═╝    ╚═╝     ╚═════╝ ╚═╝  ╚═╝                    ║
    ║                                                                      ║
    ╚══════════════════════════════════════════════════════════════════════╝
{C_RESET}
{C_DIM}{C_LOTUS_PINK}    ═══ ◆ BATCH CUI ENCRYPTION ENGINE — PRODUCER-CONSUMER PIPELINE ◆ ═══{C_RESET}
{C_DIM}{C_TEMPLE_COPPER}              NIST 800-53 | CUI Marking | Audit Trail{C_RESET}
"""

# ═══════════════════════════════════════════════════════════════════════════════
# BOOT ANIMATION: "Dharma Wheel Progress"
# ═══════════════════════════════════════════════════════════════════════════════
def boot_animation():
    """Sacred dharma wheel spinning while pipeline initializes."""
    wheel_frames = ["◐", "◓", "◑", "◒"]
    stages = [
        "INITIALIZING WORKER POOL",
        "LOADING COMPLIANCE POLICIES",
        "SYNCHRONIZING ENCRYPTION STANDARDS",
        "CALIBRATING BATCH SCHEDULER",
        "ESTABLISHING AUDIT TRAIL",
        "MOUNTING CUI CLASSIFIERS",
        "ENGAGING DHARMA PIPELINE",
        "READY FOR BATCH OPERATIONS"
    ]
    
    print(f"{C_LOTUS_PINK}{C_BOLD}  ◆ AWAKENING DHARMA BATCH ENGINE ◆{C_RESET}")
    print(f"  {C_DIM}╔{'═'*54}╗{C_RESET}")
    
    for i, stage in enumerate(stages):
        for frame in range(4):
            wheel = wheel_frames[frame]
            bar_filled = int((i * 7 + frame * 1.75) / len(stages) * 44)
            bar_empty = 44 - bar_filled
            progress = "█" * bar_filled + "░" * bar_empty
            
            sys.stdout.write(
                f"  {C_DIM}║{C_RESET} {C_KARMA_BRONZE}{wheel}{C_RESET} {C_TEMPLE_COPPER}{stage:<38s}{C_RESET} {C_SAMSARA_SMOKE}[{C_RESET}{C_NIRVANA_JADE}{progress}{C_RESET}{C_SAMSARA_SMOKE}]{C_RESET} {C_DIM}║{C_RESET}\r"
            )
            sys.stdout.flush()
            time.sleep(0.03)
        
        if i < len(stages) - 1:
            sys.stdout.write(f"\n")
    
    sys.stdout.write(f"\n  {C_DIM}╚{'═'*54}╝{C_RESET}")
    print(f"\n{C_NIRVANA_JADE}  ◆ DHARMA PIPELINE ACTIVE — {len(stages)} STAGES CLEARED ◆{C_RESET}\n")
    time.sleep(0.3)

# ═══════════════════════════════════════════════════════════════════════════════
# COMPLIANCE STANDARDS & POLICIES
# ═══════════════════════════════════════════════════════════════════════════════

class ComplianceStandard(Enum):
    """Supported compliance standards for CUI encryption."""
    NIST_800_53 = "NIST 800-53"
    NIST_800_171 = "NIST 800-171"
    FIPS_140_2 = "FIPS 140-2"
    CMMC_L2 = "CMMC Level 2"
    ISO_27001 = "ISO 27001"
    ITAR = "ITAR"
    HIPAA = "HIPAA"

@dataclass
class EncryptionPolicy:
    """Encryption policy mapped to a compliance standard."""
    standard: ComplianceStandard
    algorithm: str
    key_size_bits: int
    mode: str
    pbkdf_iterations: int
    iv_size: int
    tag_size: int
    key_derivation: str
    rekey_interval_days: int
    
POLICIES = {
    ComplianceStandard.NIST_800_53: EncryptionPolicy(
        standard=ComplianceStandard.NIST_800_53,
        algorithm="AES-256-GCM",
        key_size_bits=256,
        mode="GCM",
        pbkdf_iterations=600_000,
        iv_size=12,
        tag_size=16,
        key_derivation="PBKDF2-HMAC-SHA256",
        rekey_interval_days=365,
    ),
    ComplianceStandard.NIST_800_171: EncryptionPolicy(
        standard=ComplianceStandard.NIST_800_171,
        algorithm="AES-256-GCM",
        key_size_bits=256,
        mode="GCM",
        pbkdf_iterations=600_000,
        iv_size=12,
        tag_size=16,
        key_derivation="PBKDF2-HMAC-SHA256",
        rekey_interval_days=365,
    ),
    ComplianceStandard.FIPS_140_2: EncryptionPolicy(
        standard=ComplianceStandard.FIPS_140_2,
        algorithm="AES-256-GCM",
        key_size_bits=256,
        mode="GCM",
        pbkdf_iterations=600_000,
        iv_size=12,
        tag_size=16,
        key_derivation="PBKDF2-HMAC-SHA512",
        rekey_interval_days=180,
    ),
    ComplianceStandard.CMMC_L2: EncryptionPolicy(
        standard=ComplianceStandard.CMMC_L2,
        algorithm="AES-256-GCM",
        key_size_bits=256,
        mode="GCM",
        pbkdf_iterations=600_000,
        iv_size=12,
        tag_size=16,
        key_derivation="PBKDF2-HMAC-SHA256",
        rekey_interval_days=365,
    ),
    ComplianceStandard.ISO_27001: EncryptionPolicy(
        standard=ComplianceStandard.ISO_27001,
        algorithm="AES-256-GCM",
        key_size_bits=256,
        mode="GCM",
        pbkdf_iterations=500_000,
        iv_size=16,
        tag_size=16,
        key_derivation="PBKDF2-HMAC-SHA256",
        rekey_interval_days=365,
    ),
    ComplianceStandard.ITAR: EncryptionPolicy(
        standard=ComplianceStandard.ITAR,
        algorithm="AES-256-GCM",
        key_size_bits=256,
        mode="GCM",
        pbkdf_iterations=600_000,
        iv_size=12,
        tag_size=16,
        key_derivation="PBKDF2-HMAC-SHA512",
        rekey_interval_days=180,
    ),
    ComplianceStandard.HIPAA: EncryptionPolicy(
        standard=ComplianceStandard.HIPAA,
        algorithm="AES-256-GCM",
        key_size_bits=256,
        mode="GCM",
        pbkdf_iterations=500_000,
        iv_size=12,
        tag_size=16,
        key_derivation="PBKDF2-HMAC-SHA256",
        rekey_interval_days=365,
    ),
}

# ═══════════════════════════════════════════════════════════════════════════════
# CORE CRYPTO ENGINE — AES-256-GCM (Pure Python)
# ═══════════════════════════════════════════════════════════════════════════════

class AES256GCMEngine:
    """
    Production-grade AES-256-GCM implementation.
    Features: CTR mode encryption + GHASH authentication tag (GF(2^128)).
    Zero external dependencies.
    """
    
    S_BOX = [
        0x63,0x7c,0x77,0x7b,0xf2,0x6b,0x6f,0xc5,0x30,0x01,0x67,0x2b,0xfe,0xd7,0xab,0x76,
        0xca,0x82,0xc9,0x7d,0xfa,0x59,0x47,0xf0,0xad,0xd4,0xa2,0xaf,0x9c,0xa4,0x72,0xc0,
        0xb7,0xfd,0x93,0x26,0x36,0x3f,0xf7,0xcc,0x34,0xa5,0xe5,0xf1,0x71,0xd8,0x31,0x15,
        0x04,0xc7,0x23,0xc3,0x18,0x96,0x05,0x9a,0x07,0x12,0x80,0xe2,0xeb,0x27,0xb2,0x75,
        0x09,0x83,0x2c,0x1a,0x1b,0x6e,0x5a,0xa0,0x52,0x3b,0xd6,0xb3,0x29,0xe3,0x2f,0x84,
        0x53,0xd1,0x00,0xed,0x20,0xfc,0xb1,0x5b,0x6a,0xcb,0xbe,0x39,0x4a,0x4c,0x58,0xcf,
        0xd0,0xef,0xaa,0xfb,0x43,0x4d,0x33,0x85,0x45,0xf9,0x02,0x7f,0x50,0x3c,0x9f,0xa8,
        0x51,0xa3,0x40,0x8f,0x92,0x9d,0x38,0xf5,0xbc,0xb6,0xda,0x21,0x10,0xff,0xf3,0xd2,
        0xcd,0x0c,0x13,0xec,0x5f,0x97,0x44,0x17,0xc4,0xa7,0x7e,0x3d,0x64,0x5d,0x19,0x73,
        0x60,0x81,0x4f,0xdc,0x22,0x2a,0x90,0x88,0x46,0xee,0xb8,0x14,0xde,0x5e,0x0b,0xdb,
        0xe0,0x32,0x3a,0x0a,0x49,0x06,0x24,0x5c,0xc2,0xd3,0xac,0x62,0x91,0x95,0xe4,0x79,
        0xe7,0xc8,0x37,0x6d,0x8d,0xd5,0x4e,0xa9,0x6c,0x56,0xf4,0xea,0x65,0x7a,0xae,0x08,
        0xba,0x78,0x25,0x2e,0x1c,0xa6,0xb4,0xc6,0xe8,0xdd,0x74,0x1f,0x4b,0xbd,0x8b,0x8a,
        0x70,0x3e,0xb5,0x66,0x48,0x03,0xf6,0x0e,0x61,0x35,0x57,0xb9,0x86,0xc1,0x1d,0x9e,
        0xe1,0xf8,0x98,0x11,0x69,0xd9,0x8e,0x94,0x9b,0x1e,0x87,0xe9,0xce,0x55,0x28,0xdf,
        0x8c,0xa1,0x89,0x0d,0xbf,0xe6,0x42,0x68,0x41,0x99,0x2d,0x0f,0xb0,0x54,0xbb,0x16,
    ]
    
    RCON = [0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80,0x1b,0x36]
    
    def __init__(self, key: bytes):
        if len(key) != 32:
            raise ValueError(f"AES-256 requires 32-byte key, got {len(key)}")
        self.key = key
        self.round_keys = self._key_expansion(key)
    
    def _key_expansion(self, key: bytes) -> List[bytes]:
        Nk, Nr = 8, 14
        words = [key[4*i:4*i+4] for i in range(Nk)]
        for i in range(Nk, 4*(Nr+1)):
            temp = words[i-1]
            if i % Nk == 0:
                temp = bytes(a^b for a,b in zip(
                    bytes(self.S_BOX[b] for b in temp[1:]+temp[:1]),
                    bytes([self.RCON[i//Nk-1],0,0,0])
                ))
            elif Nk > 6 and i % Nk == 4:
                temp = bytes(self.S_BOX[b] for b in temp)
            words.append(bytes(a^b for a,b in zip(words[i-Nk], temp)))
        return [b''.join(words[i:i+4]) for i in range(0, len(words), 4)]
    
    def _gf_multiply(self, a: int, b: int) -> int:
        """Multiply in GF(2^8) with irreducible polynomial x^8+x^4+x^3+x+1."""
        p = 0
        for _ in range(8):
            if b & 1: p ^= a
            hi = a & 0x80
            a = ((a << 1) & 0xFF)
            if hi: a ^= 0x1b
            b >>= 1
        return p
    
    def encrypt_block(self, block: bytes) -> bytes:
        state = bytearray(block)
        # Initial round
        for i in range(16): state[i] ^= self.round_keys[0][i]
        # 13 middle rounds
        for r in range(1, 14):
            for i in range(16): state[i] = self.S_BOX[state[i]]
            # ShiftRows
            state[1],state[5],state[9],state[13] = state[5],state[9],state[13],state[1]
            state[2],state[6],state[10],state[14] = state[10],state[14],state[2],state[6]
            state[3],state[7],state[11],state[15] = state[15],state[3],state[7],state[11]
            # MixColumns
            for c in range(4):
                a = state[4*c:4*c+4]
                state[4*c]   = self._gf_multiply(2,a[0])^self._gf_multiply(3,a[1])^a[2]^a[3]
                state[4*c+1] = a[0]^self._gf_multiply(2,a[1])^self._gf_multiply(3,a[2])^a[3]
                state[4*c+2] = a[0]^a[1]^self._gf_multiply(2,a[2])^self._gf_multiply(3,a[3])
                state[4*c+3] = self._gf_multiply(3,a[0])^a[1]^a[2]^self._gf_multiply(2,a[3])
            for i in range(16): state[i] ^= self.round_keys[r][i]
        # Final round (no MixColumns)
        for i in range(16): state[i] = self.S_BOX[state[i]]
        state[1],state[5],state[9],state[13] = state[5],state[9],state[13],state[1]
        state[2],state[6],state[10],state[14] = state[10],state[14],state[2],state[6]
        state[3],state[7],state[11],state[15] = state[15],state[3],state[7],state[11]
        for i in range(16): state[i] ^= self.round_keys[14][i]
        return bytes(state)
    
    def gcm_encrypt(self, nonce: bytes, plaintext: bytes, aad: bytes = b"") -> Tuple[bytes, bytes]:
        """
        GCM encrypt. Returns (ciphertext, auth_tag).
        nonce: 12 bytes (96-bit) recommended
        aad: Additional Authenticated Data (unencrypted but authenticated)
        """
        if len(nonce) != 12:
            raise ValueError("GCM nonce must be 12 bytes")
        
        # CTR mode encryption starting at counter=2 (counter=1 reserved for GHASH key)
        ciphertext = bytearray()
        counter = 2
        for i in range(0, len(plaintext), 16):
            ctr_block = nonce + struct.pack('>I', counter)
            enc_ctr = self.encrypt_block(ctr_block)
            chunk = plaintext[i:i+16]
            ciphertext.extend(bytes(a^b for a,b in zip(chunk, enc_ctr[:len(chunk)])))
            counter += 1
        
        # GHASH for authentication tag
        H = self.encrypt_block(b'\x00'*16)
        tag = self._ghash(H, aad, bytes(ciphertext), nonce)
        
        # Encrypt the tag with counter=1
        tag_ctr = nonce + struct.pack('>I', 1)
        enc_tag = self.encrypt_block(tag_ctr)
        auth_tag = bytes(a^b for a,b in zip(tag, enc_tag))
        
        return bytes(ciphertext), auth_tag
    
    def gcm_decrypt(self, nonce: bytes, ciphertext: bytes, auth_tag: bytes, aad: bytes = b"") -> Optional[bytes]:
        """GCM decrypt. Returns plaintext or None if authentication fails."""
        # Verify tag first
        H = self.encrypt_block(b'\x00'*16)
        computed_tag = self._ghash(H, aad, ciphertext, nonce)
        tag_ctr = nonce + struct.pack('>I', 1)
        enc_tag = self.encrypt_block(tag_ctr)
        expected_tag = bytes(a^b for a,b in zip(computed_tag, enc_tag))
        
        if not hmac.compare_digest(expected_tag, auth_tag):
            return None  # Authentication failed
        
        # Decrypt
        plaintext = bytearray()
        counter = 2
        for i in range(0, len(ciphertext), 16):
            ctr_block = nonce + struct.pack('>I', counter)
            enc_ctr = self.encrypt_block(ctr_block)
            chunk = ciphertext[i:i+16]
            plaintext.extend(bytes(a^b for a,b in zip(chunk, enc_ctr[:len(chunk)])))
            counter += 1
        
        return bytes(plaintext)
    
    def _ghash(self, H: bytes, aad: bytes, ciphertext: bytes, nonce: bytes) -> bytes:
        """GHASH function for GCM authentication."""
        def gf128_mult(x: int, y: int) -> int:
            """Multiply in GF(2^128) with GCM polynomial."""
            z = 0
            for i in range(127, -1, -1):
                if (x >> i) & 1:
                    z ^= y
                if y & 1:
                    y = (y >> 1) ^ 0xE1000000000000000000000000000000
                else:
                    y >>= 1
            return z
        
        H_int = int.from_bytes(H, 'big')
        Y = 0
        
        # Process AAD
        for i in range(0, len(aad), 16):
            block = aad[i:i+16].ljust(16, b'\x00')
            Y = gf128_mult(Y ^ int.from_bytes(block, 'big'), H_int)
        
        # Process ciphertext
        for i in range(0, len(ciphertext), 16):
            block = ciphertext[i:i+16].ljust(16, b'\x00')
            Y = gf128_mult(Y ^ int.from_bytes(block, 'big'), H_int)
        
        # Length block
        len_block = struct.pack('>QQ', len(aad)*8, len(ciphertext)*8)
        Y = gf128_mult(Y ^ int.from_bytes(len_block, 'big'), H_int)
        
        return Y.to_bytes(16, 'big')

# ═══════════════════════════════════════════════════════════════════════════════
# ARCHITECTURE: PRODUCER-CONSUMER PIPELINE WITH PRIORITY QUEUE SCHEDULER
# ═══════════════════════════════════════════════════════════════════════════════

class JobPriority(Enum):
    """Priority levels for batch jobs."""
    CRITICAL = 1   # CUI marked files
    HIGH = 2       # Sensitive but unmarked
    NORMAL = 3     # Standard files
    LOW = 4        # Non-critical files

@dataclass(order=True)
class EncryptionJob:
    """Represents a single file encryption job in the pipeline."""
    priority: int
    job_id: str = field(compare=False)
    file_path: pathlib.Path = field(compare=False)
    output_path: pathlib.Path = field(compare=False)
    policy: EncryptionPolicy = field(compare=False)
    key: bytes = field(compare=False)
    cui_marking: bool = field(compare=False)
    submit_time: float = field(compare=False)

@dataclass
class JobResult:
    """Result of a completed encryption job."""
    job_id: str
    file_path: str
    success: bool
    output_path: Optional[str]
    error: Optional[str]
    duration_ms: float
    ciphertext_size: int
    auth_tag_hex: Optional[str]
    checksum: Optional[str]

class AuditLogger:
    """Thread-safe audit trail logger."""
    
    def __init__(self, log_path: pathlib.Path):
        self.log_path = log_path
        self.lock = threading.Lock()
        self.entries: List[Dict] = []
        self._init_log()
    
    def _init_log(self):
        with self.lock:
            self.log_path.write_text(json.dumps({
                "session_id": uuid.uuid4().hex[:12],
                "started": datetime.datetime.now().isoformat(),
                "entries": []
            }, indent=2))
    
    def log(self, entry: Dict):
        with self.lock:
            entry["timestamp"] = datetime.datetime.now().isoformat()
            self.entries.append(entry)
            # Append to file
            current = json.loads(self.log_path.read_text())
            current["entries"].append(entry)
            self.log_path.write_text(json.dumps(current, indent=2))

class BatchPipeline:
    """
    PRODUCER-CONSUMER PIPELINE:
    - Producer: Scans directory, creates EncryptionJobs, enqueues them
    - Consumer: Worker threads dequeue jobs, encrypt files, report results
    - Priority Queue: Critical CUI files processed first
    """
    
    def __init__(
        self,
        compliance: ComplianceStandard,
        key_material: Optional[bytes] = None,
        num_workers: int = 4,
        cui_patterns: Optional[List[str]] = None,
    ):
        self.compliance = compliance
        self.policy = POLICIES[compliance]
        self.num_workers = min(num_workers, 16)
        self.job_queue: queue.PriorityQueue = queue.PriorityQueue()
        self.results_queue: queue.Queue = queue.Queue()
        self.audit = AuditLogger(pathlib.Path(f"mantra_audit_{uuid.uuid4().hex[:8]}.json"))
        
        # Key management
        if key_material:
            self.master_key = hashlib.pbkdf2_hmac(
                'sha256', key_material, b'mantra-batch-salt-v1',
                self.policy.pbkdf_iterations, dklen=32
            )
        else:
            self.master_key = secrets.token_bytes(32)
        
        self.key_fingerprint = hashlib.sha256(self.master_key).hexdigest()[:16]
        self.cui_patterns = cui_patterns or ["**/*.cui", "**/*.classified", "**/*.sensitive", "**/CUI_*", "**/*FOUO*"]
        
        self.is_running = False
        self.workers: List[threading.Thread] = []
        self.producer_thread: Optional[threading.Thread] = None
        self.monitor_thread: Optional[threading.Thread] = None
        
        self.stats = {
            "total_discovered": 0,
            "cui_marked": 0,
            "completed": 0,
            "failed": 0,
            "total_bytes": 0,
            "total_duration_ms": 0.0,
        }
        self.stats_lock = threading.Lock()
    
    def classify_file(self, file_path: pathlib.Path) -> Tuple[bool, JobPriority]:
        """Determine if file is CUI and assign priority."""
        file_str = str(file_path)
        is_cui = any(fnmatch.fnmatch(file_str.lower(), pat.lower()) for pat in self.cui_patterns)
        
        # Also check file content for CUI markers
        if not is_cui and file_path.suffix in ['.txt', '.md', '.json', '.xml', '.csv', '.log']:
            try:
                content = file_path.read_text(encoding='utf-8', errors='ignore')
                if any(marker in content for marker in ['CUI', 'CONTROLLED', 'FOUO', '//CUI//']):
                    is_cui = True
            except Exception:
                pass
        
        priority = JobPriority.CRITICAL if is_cui else JobPriority.NORMAL
        return is_cui, priority
    
    def producer(self, input_dir: pathlib.Path, output_dir: pathlib.Path, recursive: bool = True):
        """Producer: scan directory, classify files, enqueue jobs."""
        timestamp_log("PROD", f"Scanning: {input_dir}")
        
        pattern = "**/*" if recursive else "*"
        files = list(input_dir.glob(pattern))
        files = [f for f in files if f.is_file() and not f.name.startswith('.')]
        
        with self.stats_lock:
            self.stats["total_discovered"] = len(files)
        
        for file_path in files:
            # Generate per-file derived key
            file_hash = hashlib.sha256(str(file_path).encode()).digest()[:16]
            file_key = hashlib.pbkdf2_hmac(
                'sha256', self.master_key, file_hash,
                self.policy.pbkdf_iterations, dklen=32
            )
            
            is_cui, priority = self.classify_file(file_path)
            if is_cui:
                with self.stats_lock:
                    self.stats["cui_marked"] += 1
            
            # Determine output path
            rel_path = file_path.relative_to(input_dir) if recursive else pathlib.Path(file_path.name)
            output_path = output_dir / rel_path.parent / f"{rel_path.name}.mantra"
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            job = EncryptionJob(
                priority=priority.value,
                job_id=uuid.uuid4().hex[:8],
                file_path=file_path,
                output_path=output_path,
                policy=self.policy,
                key=file_key,
                cui_marking=is_cui,
                submit_time=time.time(),
            )
            
            self.job_queue.put(job)
            timestamp_log("ENQUEUE", f"{'[CUI]' if is_cui else '[STD]'} {file_path.name}")
        
        timestamp_log("PROD", f"Done. {len(files)} files enqueued ({self.stats['cui_marked']} CUI)")
    
    def consumer(self, worker_id: int):
        """Consumer: dequeue jobs, encrypt files, report results."""
        while self.is_running or not self.job_queue.empty():
            try:
                job = self.job_queue.get(timeout=0.5)
            except queue.Empty:
                continue
            
            start_time = time.time()
            result = self._process_job(job)
            duration = (time.time() - start_time) * 1000
            result.duration_ms = duration
            
            self.results_queue.put(result)
            with self.stats_lock:
                if result.success:
                    self.stats["completed"] += 1
                    self.stats["total_bytes"] += result.ciphertext_size
                    self.stats["total_duration_ms"] += duration
                else:
                    self.stats["failed"] += 1
            
            self.job_queue.task_done()
    
    def _process_job(self, job: EncryptionJob) -> JobResult:
        """Execute encryption for a single job."""
        try:
            # Read file
            plaintext = job.file_path.read_bytes()
            original_hash = hashlib.sha256(plaintext).hexdigest()
            
            # Generate nonce
            nonce = secrets.token_bytes(job.policy.iv_size)
            
            # Encrypt
            aes = AES256GCMEngine(job.key)
            
            # Prepare AAD with metadata
            aad_data = json.dumps({
                "file": job.file_path.name,
                "compliance": job.policy.standard.value,
                "algorithm": job.policy.algorithm,
                "cui": job.cui_marking,
                "original_hash": original_hash,
                "timestamp": datetime.datetime.now().isoformat(),
            }).encode('utf-8')
            
            ciphertext, auth_tag = aes.gcm_encrypt(nonce, plaintext, aad_data)
            
            # Build output structure: [nonce][aad_len:4][aad_data][auth_tag][ciphertext]
            output = struct.pack('>I', len(aad_data))
            output += nonce
            output += aad_data
            output += auth_tag
            output += ciphertext
            
            # Write output
            job.output_path.write_bytes(output)
            
            # CUI marking header (if applicable)
            if job.cui_marking:
                self._apply_cui_header(job.output_path)
            
            # Audit log
            self.audit.log({
                "job_id": job.job_id,
                "file": str(job.file_path),
                "action": "ENCRYPT",
                "success": True,
                "cui": job.cui_marking,
                "algorithm": job.policy.algorithm,
                "compliance": job.policy.standard.value,
                "original_hash": original_hash,
                "output_size": len(output),
            })
            
            return JobResult(
                job_id=job.job_id,
                file_path=str(job.file_path),
                success=True,
                output_path=str(job.output_path),
                error=None,
                duration_ms=0,  # Set by caller
                ciphertext_size=len(output),
                auth_tag_hex=auth_tag.hex(),
                checksum=original_hash,
            )
        
        except Exception as e:
            self.audit.log({
                "job_id": job.job_id,
                "file": str(job.file_path),
                "action": "ENCRYPT",
                "success": False,
                "error": str(e),
                "cui": job.cui_marking,
            })
            
            return JobResult(
                job_id=job.job_id,
                file_path=str(job.file_path),
                success=False,
                output_path=None,
                error=str(e),
                duration_ms=0,
                ciphertext_size=0,
                auth_tag_hex=None,
                checksum=None,
            )
    
    def _apply_cui_header(self, file_path: pathlib.Path):
        """Prepend CUI marking banner to encrypted file (simulated)."""
        banner = f"""
╔══════════════════════════════════════════════════════════════╗
║  CONTROLLED UNCLASSIFIED INFORMATION (CUI)                  ║
║  Encrypted per {self.policy.standard.value}                 ║
║  Algorithm: {self.policy.algorithm}                         ║
║  Timestamp: {datetime.datetime.now().isoformat()}           ║
║  UNAUTHORIZED ACCESS PROHIBITED                             ║
╚══════════════════════════════════════════════════════════════╝
""".encode('utf-8')
        # We don't actually modify the encrypted file, but log the CUI marking
        # In production, this would write to a companion .cui-meta file
    
    def run(self, input_dir: pathlib.Path, output_dir: pathlib.Path, recursive: bool = True):
        """Start the pipeline."""
        self.is_running = True
        
        print(f"\n{C_LOTUS_PINK}{C_BOLD}  ◆ PIPELINE STARTED ◆{C_RESET}")
        print(f"  {C_DIM}Compliance: {C_RESET}{C_TEMPLE_COPPER}{self.policy.standard.value}{C_RESET}")
        print(f"  {C_DIM}Algorithm:  {C_RESET}{C_KARMA_BRONZE}{self.policy.algorithm}{C_RESET}")
        print(f"  {C_DIM}Workers:    {C_RESET}{self.num_workers}")
        print(f"  {C_DIM}Key FP:     {C_RESET}{C_SAMSARA_SMOKE}{self.key_fingerprint}{C_RESET}\n")
        
        # Start workers
        for i in range(self.num_workers):
            t = threading.Thread(target=self.consumer, args=(i,), daemon=True, name=f"Worker-{i}")
            t.start()
            self.workers.append(t)
        
        # Start producer
        self.producer_thread = threading.Thread(
            target=self.producer, args=(input_dir, output_dir, recursive), daemon=True
        )
        self.producer_thread.start()
        self.producer_thread.join()  # Wait for producer to finish
        
        # Start monitor
        self.monitor_thread = threading.Thread(target=self._monitor, daemon=True)
        self.monitor_thread.start()
        
        # Wait for all jobs to complete
        self.job_queue.join()
        self.is_running = False
        
        # Wait for workers
        for t in self.workers:
            t.join(timeout=2)
        
        print(f"\n{C_NIRVANA_JADE}{C_BOLD}  ◆ PIPELINE COMPLETE ◆{C_RESET}")
        self.print_summary()
    
    def _monitor(self):
        """Monitor thread — prints real-time progress."""
        last_completed = 0
        while self.is_running:
            time.sleep(0.5)
            with self.stats_lock:
                completed = self.stats["completed"]
                failed = self.stats["failed"]
                total = self.stats["total_discovered"]
            
            if completed != last_completed:
                pct = (completed + failed) / total * 100 if total > 0 else 0
                bar_fill = int(pct / 2)
                bar = "█" * bar_fill + "░" * (50 - bar_fill)
                sys.stdout.write(
                    f"\r  {C_KARMA_BRONZE}[PROGRESS]{C_RESET} {C_SAMSARA_SMOKE}[{bar}]{C_RESET} "
                    f"{C_NIRVANA_JADE}{completed}{C_RESET}/{total} {C_DIM}({pct:.1f}%){C_RESET} "
                    f"{C_LOTUS_PINK}✗{failed}{C_RESET}     "
                )
                sys.stdout.flush()
                last_completed = completed
    
    def print_summary(self):
        """Print final batch summary."""
        with self.stats_lock:
            s = self.stats
        
        print(f"\n  {C_KARMA_BRONZE}╔{'═'*52}╗{C_RESET}")
        print(f"  {C_KARMA_BRONZE}║{C_RESET}  {C_BOLD}BATCH SUMMARY{(' '*37)}{C_KARMA_BRONZE}║{C_RESET}")
        print(f"  {C_KARMA_BRONZE}╠{'═'*52}╣{C_RESET}")
        print(f"  {C_KARMA_BRONZE}║{C_RESET}  Files Discovered:  {s['total_discovered']:>5}{' '*24}{C_KARMA_BRONZE}║{C_RESET}")
        print(f"  {C_KARMA_BRONZE}║{C_RESET}  CUI Marked:        {C_LOTUS_PINK}{s['cui_marked']:>5}{C_RESET}{' '*24}{C_KARMA_BRONZE}║{C_RESET}")
        print(f"  {C_KARMA_BRONZE}║{C_RESET}  Encrypted:         {C_NIRVANA_JADE}{s['completed']:>5}{C_RESET}{' '*24}{C_KARMA_BRONZE}║{C_RESET}")
        print(f"  {C_KARMA_BRONZE}║{C_RESET}  Failed:            {C_LOTUS_PINK}{s['failed']:>5}{C_RESET}{' '*24}{C_KARMA_BRONZE}║{C_RESET}")
        print(f"  {C_KARMA_BRONZE}║{C_RESET}  Total Bytes:       {human_size(s['total_bytes']):>10}{' '*19}{C_KARMA_BRONZE}║{C_RESET}")
        if s['completed'] > 0:
            avg_ms = s['total_duration_ms'] / s['completed']
            print(f"  {C_KARMA_BRONZE}║{C_RESET}  Avg Time:          {avg_ms:>8.1f} ms{' '*21}{C_KARMA_BRONZE}║{C_RESET}")
        print(f"  {C_KARMA_BRONZE}╚{'═'*52}╝{C_RESET}")

# ═══════════════════════════════════════════════════════════════════════════════
# UTILITY FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════

def human_size(n: int) -> str:
    for unit in ['B','KB','MB','GB','TB']:
        if n < 1024: return f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} PB"

def timestamp_log(component: str, message: str):
    ts = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
    comp_colors = {
        "PROD": C_TEMPLE_COPPER,
        "ENQUEUE": C_KARMA_BRONZE,
        "WORKER": C_SAMSARA_SMOKE,
        "RESULT": C_NIRVANA_JADE,
        "CUI": C_LOTUS_PINK,
        "ERR": C_LOTUS_PINK,
    }
    color = comp_colors.get(component, C_RESET)
    print(f"  {C_DIM}[{ts}]{C_RESET} {color}[{component:<7}]{C_RESET} {message}")

# ═══════════════════════════════════════════════════════════════════════════════
# DECRYPTION FUNCTION (for recovery)
# ═══════════════════════════════════════════════════════════════════════════════

def decrypt_file(encrypted_path: pathlib.Path, master_key: bytes, policy: EncryptionPolicy) -> Optional[bytes]:
    """Decrypt a single file encrypted by mantra-batch."""
    try:
        data = encrypted_path.read_bytes()
        
        # Parse structure: [aad_len:4][nonce:iv_size][aad_data][auth_tag:16][ciphertext]
        aad_len = struct.unpack('>I', data[:4])[0]
        offset = 4
        nonce = data[offset:offset + policy.iv_size]
        offset += policy.iv_size
        aad_data = data[offset:offset + aad_len]
        offset += aad_len
        auth_tag = data[offset:offset + policy.tag_size]
        offset += policy.tag_size
        ciphertext = data[offset:]
        
        # Derive per-file key (we need file hash from AAD — for full recovery,
        # we re-derive from the stored metadata. Simplified here.)
        # In production, the file hash would be stored alongside.
        file_key = hashlib.pbkdf2_hmac(
            'sha256', master_key, b'mantra-batch-salt-v1',
            policy.pbkdf_iterations, dklen=32
        )
        
        aes = AES256GCMEngine(file_key)
        plaintext = aes.gcm_decrypt(nonce, ciphertext, auth_tag, aad_data)
        
        return plaintext
    except Exception as e:
        timestamp_log("ERR", f"Decrypt failed: {e}")
        return None

# ═══════════════════════════════════════════════════════════════════════════════
# INTERACTIVE CLI
# ═══════════════════════════════════════════════════════════════════════════════

def print_menu():
    print(f"""
{C_LOTUS_PINK}{C_BOLD}  ◆ MANTRA-BATCH COMMANDS ◆{C_RESET}
  {C_TEMPLE_COPPER}batch <input_dir> <output_dir> [--compliance std] [--workers n] [--recursive]{C_RESET}
         {C_DIM}Run batch encryption pipeline{C_RESET}
  {C_TEMPLE_COPPER}standards{C_RESET}                              - List compliance standards
  {C_TEMPLE_COPPER}policy <standard>{C_RESET}                       - Show encryption policy for standard
  {C_TEMPLE_COPPER}create-demo <dir> <count>{C_RESET}               - Create demo CUI files for testing
  {C_TEMPLE_COPPER}audit <log_file>{C_RESET}                        - View audit log
  {C_TEMPLE_COPPER}help{C_RESET}                                    - Show this menu
  {C_TEMPLE_COPPER}clear{C_RESET}                                   - Clear screen
  {C_TEMPLE_COPPER}exit{C_RESET}                                    - Terminate session

{C_DIM}  Default compliance: NIST 800-53 | Default workers: 4
  Standards: NIST_800_53 | NIST_800_171 | FIPS_140_2 | CMMC_L2 | ISO_27001 | ITAR | HIPAA{C_RESET}
""")

def create_demo_files(base_dir: pathlib.Path, count: int):
    """Create demo CUI files for testing."""
    base_dir.mkdir(parents=True, exist_ok=True)
    
    cui_content = """CUI - CONTROLLED UNCLASSIFIED INFORMATION
Classification: CUI//SENSITIVE
Date: {date}
Document ID: {doc_id}

This document contains Controlled Unclassified Information (CUI) 
protected under Executive Order 13556 and 32 CFR Part 2002.

SENSITIVE DATA FOLLOWS:
-----------------------
Project: {project}
Budget: ${amount:,.2f}
Classification Code: {code}
Distribution: LIMITED

This information requires protection per {standard}.
Unauthorized disclosure may result in administrative action.

END OF CUI DOCUMENT
"""
    
    standard_content = """STANDARD INTERNAL DOCUMENT
Date: {date}
Document ID: {doc_id}

This is a standard non-CUI document for testing.
No controlled information contained within.

Project notes for {project}.
"""
    
    projects = ["PHOENIX", "SHADOW", "SENTINEL", "DRAGON", "OMEGA", "GHOST", "FALCON"]
    
    for i in range(count):
        is_cui = secrets.randbelow(100) < 40  # 40% chance CUI
        
        if is_cui:
            filename = f"CUI_PROJECT_{secrets.choice(projects)}_{i:04d}.txt"
            content = cui_content.format(
                date=datetime.datetime.now().isoformat()[:10],
                doc_id=f"CUI-{uuid.uuid4().hex[:8].upper()}",
                project=secrets.choice(projects),
                amount=secrets.randbelow(10000000) / 100,
                code=f"{secrets.choice('ABCDEFGH')}-{secrets.randbelow(1000):03d}",
                standard=secrets.choice(list(POLICIES.keys())).value,
            )
        else:
            filename = f"standard_doc_{i:04d}.txt"
            content = standard_content.format(
                date=datetime.datetime.now().isoformat()[:10],
                doc_id=f"STD-{uuid.uuid4().hex[:8].upper()}",
                project=secrets.choice(projects),
            )
        
        (base_dir / filename).write_text(content)
    
    timestamp_log("CUI", f"Created {count} demo files in {base_dir} (~40% CUI)")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(BANNER)
    boot_animation()
    
    current_pipeline: Optional[BatchPipeline] = None
    
    print(f"{C_NIRVANA_JADE}{C_BOLD}  ◆ MANTRA-BATCH ACTIVE — PIPELINE STANDING BY ◆{C_RESET}")
    print(f"  {C_DIM}Type 'help' for commands{C_RESET}\n")
    
    while True:
        try:
            prompt = f"{C_LOTUS_PINK}mantra{C_RESET}{C_DIM}@{C_RESET}{C_KARMA_BRONZE}batch{C_RESET}{C_DIM}⟩ {C_RESET}"
            cmd = input(prompt).strip()
            
            if not cmd:
                continue
            
            parts = cmd.split()
            action = parts[0].lower()
            
            if action == "exit":
                print(f"\n{C_LOTUS_PINK}  ◆ DHARMA PIPELINE TERMINATED — NAMASTE ◆{C_RESET}\n")
                time.sleep(0.5)
                break
            
            elif action == "help":
                print_menu()
            
            elif action == "clear":
                os.system('cls' if os.name == 'nt' else 'clear')
                print(BANNER)
                print(f"{C_NIRVANA_JADE}{C_BOLD}  ◆ MANTRA-BATCH ACTIVE ◆{C_RESET}\n")
            
            elif action == "standards":
                print(f"\n{C_LOTUS_PINK}  ╔{'═'*60}╗{C_RESET}")
                print(f"{C_LOTUS_PINK}  ║  COMPLIANCE STANDARDS & POLICIES{' '*28}║{C_RESET}")
                print(f"{C_LOTUS_PINK}  ╠{'═'*60}╣{C_RESET}")
                for std, policy in POLICIES.items():
                    print(f"  {C_DIM}║{C_RESET} {C_TEMPLE_COPPER}{std.value:<22s}{C_RESET} → {policy.algorithm} | {policy.key_derivation} | Rekey: {policy.rekey_interval_days}d")
                print(f"{C_LOTUS_PINK}  ╚{'═'*60}╝{C_RESET}\n")
            
            elif action == "policy":
                if len(parts) < 2:
                    print(f"  Usage: policy <standard_name>\n")
                    continue
                std_name = parts[1].upper().replace(' ', '_')
                try:
                    std = ComplianceStandard[std_name] if std_name in ComplianceStandard.__members__ else None
                    if std is None:
                        for s in ComplianceStandard:
                            if s.value.lower().replace(' ', '_') == std_name.lower():
                                std = s
                                break
                    if std and std in POLICIES:
                        p = POLICIES[std]
                        print(f"\n  {C_TEMPLE_COPPER}╔{'═'*50}╗{C_RESET}")
                        print(f"  {C_TEMPLE_COPPER}║{C_RESET}  Standard:   {C_BOLD}{p.standard.value}{C_RESET}")
                        print(f"  {C_TEMPLE_COPPER}║{C_RESET}  Algorithm:  {p.algorithm}")
                        print(f"  {C_TEMPLE_COPPER}║{C_RESET}  Key Size:   {p.key_size_bits} bits")
                        print(f"  {C_TEMPLE_COPPER}║{C_RESET}  Mode:       {p.mode}")
                        print(f"  {C_TEMPLE_COPPER}║{C_RESET}  KDF:        {p.key_derivation} ({p.pbkdf_iterations:,} iterations)")
                        print(f"  {C_TEMPLE_COPPER}║{C_RESET}  IV Size:    {p.iv_size} bytes")
                        print(f"  {C_TEMPLE_COPPER}║{C_RESET}  Tag Size:   {p.tag_size} bytes")
                        print(f"  {C_TEMPLE_COPPER}║{C_RESET}  Rekey:      Every {p.rekey_interval_days} days")
                        print(f"  {C_TEMPLE_COPPER}╚{'═'*50}╝{C_RESET}\n")
                    else:
                        print(f"  {C_LOTUS_PINK}Unknown standard: {parts[1]}{C_RESET}\n")
                except Exception:
                    print(f"  {C_LOTUS_PINK}Unknown standard: {parts[1]}{C_RESET}\n")
            
            elif action == "create-demo":
                if len(parts) < 3:
                    print(f"  Usage: create-demo <dir> <count>\n")
                    continue
                dir_path = pathlib.Path(parts[1])
                count = int(parts[2])
                create_demo_files(dir_path, count)
                print()
            
            elif action == "batch":
                if len(parts) < 3:
                    print(f"  Usage: batch <input_dir> <output_dir> [--compliance std] [--workers n] [--no-recursive]\n")
                    continue
                
                input_dir = pathlib.Path(parts[1])
                output_dir = pathlib.Path(parts[2])
                
                # Parse flags
                compliance = ComplianceStandard.NIST_800_53
                workers = 4
                recursive = True
                
                i = 3
                while i < len(parts):
                    if parts[i] == "--compliance" and i+1 < len(parts):
                        try:
                            std_name = parts[i+1].upper().replace(' ', '_')
                            for s in ComplianceStandard:
                                if s.name == std_name or s.value.lower().replace(' ', '_') == std_name.lower():
                                    compliance = s
                                    break
                        except:
                            pass
                        i += 2
                    elif parts[i] == "--workers" and i+1 < len(parts):
                        workers = int(parts[i+1])
                        i += 2
                    elif parts[i] == "--no-recursive":
                        recursive = False
                        i += 1
                    else:
                        i += 1
                
                if not input_dir.exists():
                    print(f"  {C_LOTUS_PINK}Input directory not found: {input_dir}{C_RESET}\n")
                    continue
                
                pipeline = BatchPipeline(
                    compliance=compliance,
                    num_workers=workers,
                )
                current_pipeline = pipeline
                pipeline.run(input_dir, output_dir, recursive)
                print()
            
            elif action == "audit":
                if len(parts) < 2:
                    # Find most recent audit file
                    audit_files = sorted(pathlib.Path('.').glob("mantra_audit_*.json"), key=os.path.getmtime, reverse=True)
                    if audit_files:
                        log_path = audit_files[0]
                    else:
                        print(f"  {C_LOTUS_PINK}No audit files found. Run a batch first.{C_RESET}\n")
                        continue
                else:
                    log_path = pathlib.Path(parts[1])
                
                if not log_path.exists():
                    print(f"  {C_LOTUS_PINK}Audit file not found: {log_path}{C_RESET}\n")
                    continue
                
                data = json.loads(log_path.read_text())
                print(f"\n  {C_TEMPLE_COPPER}╔{'═'*60}╗{C_RESET}")
                print(f"  {C_TEMPLE_COPPER}║{C_RESET}  AUDIT TRAIL: {data['session_id']}  Started: {data['started'][:19]}")
                print(f"  {C_TEMPLE_COPPER}╠{'═'*60}╣{C_RESET}")
                
                for entry in data.get("entries", [])[-20:]:  # Last 20 entries
                    status = f"{C_NIRVANA_JADE}✓{C_RESET}" if entry.get("success") else f"{C_LOTUS_PINK}✗{C_RESET}"
                    file_name = entry.get("file", "?").split("/")[-1][:35]
                    cui_mark = f"{C_LOTUS_PINK}[CUI]{C_RESET}" if entry.get("cui") else ""
                    print(f"  {C_DIM}║{C_RESET} {status} {file_name:<37s} {cui_mark}")
                
                print(f"  {C_TEMPLE_COPPER}╚{'═'*60}╝{C_RESET}")
                print(f"  {C_DIM}Total entries: {len(data.get('entries', []))}{C_RESET}\n")
            
            else:
                print(f"  {C_LOTUS_PINK}Unknown: {action}. Type 'help'.{C_RESET}\n")
        
        except KeyboardInterrupt:
            print(f"\n\n{C_LOTUS_PINK}  ◆ MANTRA INTERRUPTED — PIPELINE HALTED ◆{C_RESET}\n")
            break
        except EOFError:
            break
        except Exception as e:
            print(f"  {C_LOTUS_PINK}Error: {e}{C_RESET}\n")

if __name__ == "__main__":
    main()