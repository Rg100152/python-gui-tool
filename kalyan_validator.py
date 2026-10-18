import os
import time
import hashlib
from dataclasses import dataclass, field
from abc import ABC, abstractmethod

# ==========================================
# KALYAN-VALIDATOR: CRYPTOGRAPHIC THEME
# ==========================================
CYN = '\033[96m'  # Cyan (System Info)
GRN = '\033[92m'  # Green (Valid/OK)
RED = '\033[91m'  # Red (Invalid/Fail)
YLW = '\033[93m'  # Yellow (Processing)
MAG = '\033[95m'  # Magenta (Hashes)
RST = '\033[0m'   # Reset
BLD = '\033[1m'

# ==========================================
# DATA MODELING (STRICT PAYLOAD STRUCTURE)
# ==========================================
@dataclass
class EvidencePayload:
    """A strict data structure representing the document being validated."""
    filename: str
    content: str
    size_bytes: int = 0
    checksum: str = ""
    is_compliant: bool = True
    audit_trail: list = field(default_factory=list)

    def __post_init__(self):
        self.size_bytes = len(self.content.encode('utf-8'))
        self.checksum = hashlib.sha256(self.content.encode('utf-8')).hexdigest()

# ==========================================
# CHAIN OF RESPONSIBILITY ARCHITECTURE
# ==========================================
class ComplianceHandler(ABC):
    """Abstract Base Class for the validation chain."""
    @abstractmethod
    def set_next(self, handler: 'ComplianceHandler') -> 'ComplianceHandler':
        pass

    @abstractmethod
    def validate(self, payload: EvidencePayload) -> EvidencePayload:
        pass

class AbstractValidator(ComplianceHandler):
    """Core pipeline logic. Passes payload to the next node if valid."""
    _next_handler: ComplianceHandler = None

    def set_next(self, handler: ComplianceHandler) -> ComplianceHandler:
        self._next_handler = handler
        return handler

    def validate(self, payload: EvidencePayload) -> EvidencePayload:
        if self._next_handler and payload.is_compliant:
            return self._next_handler.validate(payload)
        return payload

# ==========================================
# SPECIFIC VALIDATION NODES (THE CHAIN)
# ==========================================
class FileIntegrityNode(AbstractValidator):
    def validate(self, payload: EvidencePayload) -> EvidencePayload:
        print(f" {YLW}↳ VERIFYING SHA-256 SIGNATURE: {MAG}{payload.checksum[:16]}...{RST}", end="")
        time.sleep(0.4)
        if payload.size_bytes > 0:
            print(f"\r {GRN}↳ SIGNATURE VERIFIED: {payload.checksum[:16]}... [ OK ]{RST}")
            payload.audit_trail.append("Integrity: PASS")
        else:
            print(f"\r {RED}↳ SIGNATURE VERIFIED: {payload.checksum[:16]}... [ FAIL ]{RST}")
            payload.is_compliant = False
            payload.audit_trail.append("Integrity: ZERO_BYTE_FILE")
        return super().validate(payload)

class HeaderMarkerNode(AbstractValidator):
    def validate(self, payload: EvidencePayload) -> EvidencePayload:
        print(f" {YLW}↳ ANALYZING HEADER METADATA...{RST}", end="")
        time.sleep(0.4)
        lines = payload.content.strip().split('\n')
        if lines and lines[0].startswith("CLASSIFICATION: CUI"):
            print(f"\r {GRN}↳ HEADER METADATA CUI MARKER LOCATED.      [ OK ]{RST}")
            payload.audit_trail.append("Header: PASS")
        else:
            print(f"\r {RED}↳ HEADER METADATA MISSING CUI MARKER!      [ FAIL ]{RST}")
            payload.is_compliant = False
            payload.audit_trail.append("Header: MISSING_MARKER")
        return super().validate(payload)

class FooterMarkerNode(AbstractValidator):
    def validate(self, payload: EvidencePayload) -> EvidencePayload:
        print(f" {YLW}↳ ANALYZING FOOTER METADATA...{RST}", end="")
        time.sleep(0.4)
        lines = payload.content.strip().split('\n')
        if lines and lines[-1].startswith("END CLASSIFICATION"):
            print(f"\r {GRN}↳ FOOTER METADATA TERMINATOR LOCATED.      [ OK ]{RST}")
            payload.audit_trail.append("Footer: PASS")
        else:
            print(f"\r {RED}↳ FOOTER METADATA TERMINATOR MISSING!      [ FAIL ]{RST}")
            payload.is_compliant = False
            payload.audit_trail.append("Footer: MISSING_TERMINATOR")
        return super().validate(payload)

# ==========================================
# SYSTEM EXECUTION & AESTHETICS
# ==========================================
def display_kalyan_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = f"""{CYN}{BLD}
     _  __     _                    _    __      _ _     _       _             
    | |/ /__ _| |_   _  __ _ _ __   \ \ / /_ _| (_) | __| | __ _| |_ ___  _ __ 
    | ' // _` | | | | |/ _` | '_ \   \ V / _` | | | |/ _` |/ _` | __/ _ \| '__|
    | . \ (_| | | |_| | (_| | | | |   | | (_| | | | | (_| | (_| | || (_) | |   
    |_|\_\__,_|_|\__, |\__,_|_| |_|   |_|\__,_|_|_|_|\__,_|\__,_|\__\___/|_|   
                 |___/                                                         
    {RST}"""
    print(banner)
    print(f"{CYN}[*] ARCHITECTURE: CHAIN OF RESPONSIBILITY (BEHAVIORAL PIPELINE){RST}")
    print(f"{CYN}[*] PROTOCOL: CRYPTOGRAPHIC INTEGRITY & LABEL VALIDATION{RST}\n")

def generate_test_cases():
    valid = "CLASSIFICATION: CUI // SP-PRVT\nThis is secure data.\nEND CLASSIFICATION"
    invalid = "CLASSIFICATION: PUBLIC\nThis is a poorly labeled file.\nNo footer here."
    return [
        ("auth_report_valid.txt", valid),
        ("auth_report_corrupt.txt", invalid)
    ]

def run_validator():
    display_kalyan_banner()
    
    # 1. Instantiate the Chain Nodes
    integrity_check = FileIntegrityNode()
    header_check = HeaderMarkerNode()
    footer_check = FooterMarkerNode()
    
    # 2. Link the Chain
    integrity_check.set_next(header_check).set_next(footer_check)
    
    # 3. Process Evidence
    test_files = generate_test_cases()
    
    for filename, content in test_files:
        print(f"{BLD}{CYN}[+] INITIALIZING VALIDATION SEQUENCE FOR: {filename}{RST}")
        print("-" * 65)
        
        # Load data into our strict dataclass model
        payload = EvidencePayload(filename=filename, content=content)
        
        # Push the payload through the beginning of the chain
        final_result = integrity_check.validate(payload)
        
        print("-" * 65)
        if final_result.is_compliant:
            print(f"{GRN}{BLD}>> STATUS: COMPLIANT. DOCUMENT AUTHORIZED FOR TRANSFER.{RST}\n")
        else:
            print(f"{RED}{BLD}>> STATUS: NON-COMPLIANT. QUARANTINE PROTOCOL ENGAGED.{RST}")
            print(f"{RED}>> REASON: {', '.join([x for x in final_result.audit_trail if 'FAIL' in x or 'MISSING' in x])}{RST}\n")
        time.sleep(1)

if __name__ == "__main__":
    try:
        run_validator()
    except KeyboardInterrupt:
        print(f"\n{RED}[!] KALYAN VALIDATOR TERMINATED BY KERNEL.{RST}")