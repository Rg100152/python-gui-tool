#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════╗
║              MAURYA-TAG v1.0                                ║
║     Imperial CUI Metadata Tagging Framework                 ║
║       "Tag Every Document, Secure the Empire"               ║
║     Enterprise-Grade | CUI Compliant | Iron-Clad            ║
╚══════════════════════════════════════════════════════════════╝

Inspired by the administrative precision of the Mauryan Empire.
Like the Arthashastra classified every aspect of governance,
Maurya-Tag classifies every document with metadata precision.
"""

import os
import sys
import time
import random
import hashlib
import base64
import json
import re
import argparse
from datetime import datetime
from getpass import getpass
from typing import Dict, List, Tuple, Optional, Any, Set

# ============================================================
# COLOR SCHEME - Imperial Mauryan Palette
# ============================================================
class Imperial:
    """Colors inspired by Mauryan imperial aesthetics"""
    # Primary
    GOLD = '\033[38;5;220m'        # Ashoka's gold
    SAFFRON = '\033[38;5;208m'     # Sacred saffron
    MAROON = '\033[38;5;124m'      # Imperial maroon
    INDIGO = '\033[38;5;54m'       # Royal indigo
    
    # Secondary
    IVORY = '\033[38;5;230m'       # Parchment ivory
    BRONZE = '\033[38;5;137m'      # Aged bronze
    COPPER = '\033[38;5;166m'      # Copper plate
    ASH = '\033[38;5;245m'         # Ash grey
    
    # Status
    EMERALD = '\033[38;5;35m'      # Success green
    RUBY = '\033[38;5;196m'        # Error red
    AMBER = '\033[38;5;226m'       # Warning amber
    
    # Styles
    WHITE = '\033[97m'
    BLACK = '\033[30m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

I = Imperial()

# ============================================================
# CUI TAG CATALOG - Official Registry
# ============================================================
CUI_TAG_REGISTRY = {
    # Personal Information
    "PII": {
        "name": "Personally Identifiable Information",
        "description": "Information that can identify an individual",
        "examples": ["SSN", "Full name", "Date of birth", "Address"],
        "handling": "Encrypt at rest. Limit access to authorized personnel.",
        "retention": "7 years after last use",
        "category": "PRIVACY"
    },
    "PHI": {
        "name": "Protected Health Information",
        "description": "Medical and health-related personal data",
        "examples": ["Medical records", "Insurance details", "Treatment history"],
        "handling": "HIPAA compliant. Strict access controls.",
        "retention": "10 years",
        "category": "HEALTH"
    },
    "SPII": {
        "name": "Sensitive PII",
        "description": "Highly sensitive personal identifiers",
        "examples": ["Biometric data", "Genetic information", "Passport number"],
        "handling": "Maximum encryption. MFA required for access.",
        "retention": "5 years",
        "category": "PRIVACY"
    },
    
    # Business Information
    "PROPRIETARY": {
        "name": "Proprietary Information",
        "description": "Trade secrets and intellectual property",
        "examples": ["Source code", "Algorithms", "Business methods"],
        "handling": "NDA required. Watermark all copies.",
        "retention": "Permanent or until declassified",
        "category": "BUSINESS"
    },
    "FINANCIAL": {
        "name": "Financial Information",
        "description": "Sensitive financial and banking data",
        "examples": ["Account numbers", "Transaction records", "Audit reports"],
        "handling": "Encrypt at rest and in transit. Dual authorization for access.",
        "retention": "10 years",
        "category": "FINANCE"
    },
    "CONTRACT": {
        "name": "Contractual Information",
        "description": "Confidential contract and agreement details",
        "examples": ["Vendor agreements", "Client contracts", "Pricing sheets"],
        "handling": "Legal department authorization required.",
        "retention": "Duration of contract + 5 years",
        "category": "LEGAL"
    },
    
    # Government & Defense
    "DEFENSE": {
        "name": "Defense Related Information",
        "description": "National defense and military information",
        "examples": ["Technical specifications", "Strategic plans", "Logistics data"],
        "handling": "ITAR compliant. No foreign national access.",
        "retention": "Classified retention schedule",
        "category": "DEFENSE"
    },
    "EXPORT": {
        "name": "Export Controlled Information",
        "description": "Information subject to export control regulations",
        "examples": ["Encryption technology", "Dual-use items", "Technical data"],
        "handling": "EAR/ITAR compliance mandatory.",
        "retention": "15 years",
        "category": "TRADE"
    },
    "NATSEC": {
        "name": "National Security Information",
        "description": "Information affecting national security",
        "examples": ["Intelligence reports", "Critical infrastructure data"],
        "handling": "Maximum security. Need-to-know basis only.",
        "retention": "Indefinite",
        "category": "SECURITY"
    },
    
    # Infrastructure
    "ITINFRA": {
        "name": "IT Infrastructure Information",
        "description": "Sensitive technical infrastructure data",
        "examples": ["Network diagrams", "Server configurations", "Security keys"],
        "handling": "System admin access only. Audit all access.",
        "retention": "Active + 3 years",
        "category": "TECHNICAL"
    },
    "CREDENTIAL": {
        "name": "Credential Information",
        "description": "Authentication and access credentials",
        "examples": ["Passwords", "API keys", "Certificates"],
        "handling": "Vault storage. Never in plain text.",
        "retention": "Until rotation",
        "category": "SECURITY"
    },
    
    # Research & Development
    "RESEARCH": {
        "name": "Research Information",
        "description": "Confidential research and development data",
        "examples": ["Lab results", "Patent applications", "Prototype data"],
        "handling": "Department head authorization. Lab notebook policy.",
        "retention": "10 years after project completion",
        "category": "RESEARCH"
    },
}

# ============================================================
# CLASSIFICATION LEVELS
# ============================================================
CLASSIFICATION_LEVELS = {
    0: "PUBLIC",
    1: "INTERNAL",
    2: "CUI//BASIC",
    3: "CUI//SPECIFIED",
    4: "CONFIDENTIAL",
    5: "SECRET",
    6: "TOP SECRET"
}

# ============================================================
# SIMULATED FILE DATABASE
# ============================================================
class ImperialArchive:
    """Simulated document archive for the Mauryan Empire"""
    
    DOCUMENTS = [
        {
            "id": "DOC-001",
            "path": "/imperial/treasury/revenue_report.docx",
            "name": "Revenue Report 2024",
            "tags": ["FINANCIAL", "PROPRIETARY"],
            "level": "CUI//SPECIFIED",
            "owner": "finance_minister",
            "created": "2024-01-15",
            "size": "2.4MB",
            "status": "active"
        },
        {
            "id": "DOC-002",
            "path": "/imperial/defense/war_strategy.pdf",
            "name": "Eastern Border Strategy",
            "tags": ["DEFENSE", "NATSEC"],
            "level": "SECRET",
            "owner": "senapati",
            "created": "2024-02-10",
            "size": "15.7MB",
            "status": "active"
        },
        {
            "id": "DOC-003",
            "path": "/imperial/health/patient_records.zip",
            "name": "Citizen Health Records",
            "tags": ["PHI", "PII"],
            "level": "CUI//SPECIFIED",
            "owner": "vaidya_mukhya",
            "created": "2024-03-01",
            "size": "45.3MB",
            "status": "active"
        },
        {
            "id": "DOC-004",
            "path": "/imperial/infra/server_config.txt",
            "name": "Server Configuration",
            "tags": ["ITINFRA", "CREDENTIAL"],
            "level": "CONFIDENTIAL",
            "owner": "system_administrator",
            "created": "2024-01-20",
            "size": "128KB",
            "status": "active"
        },
        {
            "id": "DOC-005",
            "path": "/imperial/research/quantum_notes.txt",
            "name": "Quantum Computing Research",
            "tags": ["RESEARCH", "PROPRIETARY"],
            "level": "CUI//BASIC",
            "owner": "chief_scientist",
            "created": "2024-04-05",
            "size": "856KB",
            "status": "draft"
        },
        {
            "id": "DOC-006",
            "path": "/imperial/trade/export_agreement.pdf",
            "name": "Export Agreement - Silk Route",
            "tags": ["CONTRACT", "EXPORT"],
            "level": "CUI//SPECIFIED",
            "owner": "trade_minister",
            "created": "2024-03-15",
            "size": "8.2MB",
            "status": "active"
        },
        {
            "id": "DOC-007",
            "path": "/imperial/public/edict_stone.txt",
            "name": "Public Edict - Dhamma",
            "tags": [],
            "level": "PUBLIC",
            "owner": "samrat",
            "created": "2024-01-01",
            "size": "12KB",
            "status": "published"
        },
    ]
    
    @classmethod
    def get_by_id(cls, doc_id: str) -> Optional[Dict]:
        for doc in cls.DOCUMENTS:
            if doc["id"] == doc_id:
                return doc
        return None
    
    @classmethod
    def get_by_path(cls, path: str) -> Optional[Dict]:
        for doc in cls.DOCUMENTS:
            if doc["path"] == path:
                return doc
        return None
    
    @classmethod
    def search_by_tag(cls, tag: str) -> List[Dict]:
        return [doc for doc in cls.DOCUMENTS if tag in doc["tags"]]

# ============================================================
# UTILITY FUNCTIONS
# ============================================================
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def print_banner(text: str, width: int = 60):
    print(f"\n{I.GOLD}{'═' * width}")
    print(f"  {text.center(width - 4)}")
    print(f"{'═' * width}{I.RESET}\n")

def print_status(message: str, status: str = "INFO"):
    colors = {
        "INFO": I.INDIGO, "SUCCESS": I.EMERALD, "WARNING": I.AMBER,
        "ERROR": I.RUBY, "CRITICAL": I.RUBY, "TAG": I.SAFFRON
    }
    color = colors.get(status, I.WHITE)
    print(f"{I.ASH}[{timestamp()}]{I.RESET} {color}[{status}]{I.RESET} {message}")

def progress_bar(total: int = 100, prefix: str = "Processing", length: int = 50, delay: float = 0.02):
    for i in range(total + 1):
        percent = 100 * i // total
        filled = length * i // total
        bar = '█' * filled + '░' * (length - filled)
        sys.stdout.write(f'\r{prefix} |{I.GOLD}{bar}{I.RESET}| {percent}%')
        sys.stdout.flush()
        time.sleep(delay)
    print()

def spinner(duration: float = 1.5, text: str = "Processing"):
    frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    end = time.time() + duration
    while time.time() < end:
        for frame in frames:
            sys.stdout.write(f'\r{I.SAFFRON}{frame} {text}...{I.RESET}')
            sys.stdout.flush()
            time.sleep(0.08)
    sys.stdout.write(f'\r{I.EMERALD}✓ {text} Complete!{I.RESET}     \n')

def show_banner():
    clear_screen()
    print(f"""
{I.GOLD}╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║  {I.SAFFRON}███╗   ███╗ █████╗ ██╗   ██╗██████╗ ██╗   ██╗ █████╗{I.GOLD}    ║
║  {I.SAFFRON}████╗ ████║██╔══██╗██║   ██║██╔══██╗╚██╗ ██╔╝██╔══██╗{I.GOLD}    ║
║  {I.SAFFRON}██╔████╔██║███████║██║   ██║██████╔╝ ╚████╔╝ ███████║{I.GOLD}    ║
║  {I.SAFFRON}██║╚██╔╝██║██╔══██║██║   ██║██╔══██╗  ╚██╔╝  ██╔══██║{I.GOLD}    ║
║  {I.SAFFRON}██║ ╚═╝ ██║██║  ██║╚██████╔╝██║  ██║   ██║   ██║  ██║{I.GOLD}    ║
║  {I.SAFFRON}╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝{I.GOLD}    ║
║                                                              ║
║     {I.IVORY}{I.BOLD}MAURYA-TAG v1.0{I.RESET}{I.GOLD}                                    ║
║     {I.ASH}Imperial CUI Metadata Tagging Framework{I.GOLD}                    ║
║     {I.ASH}"Tag Every Document, Secure the Empire"{I.GOLD}                      ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝{I.RESET}
    """)

# ============================================================
# CORE MAURYA-TAG SYSTEM
# ============================================================
class MauryaTagSystem:
    """Main tagging system inspired by Mauryan administrative precision"""
    
    def __init__(self):
        self.tag_history = []
        self.audit_log = []
    
    def log_action(self, action: str, details: str):
        self.audit_log.append({
            "timestamp": timestamp(),
            "action": action,
            "details": details
        })
    
    def list_tags(self) -> None:
        """Display all registered CUI tags with details"""
        print_banner("IMPERIAL TAG REGISTRY", I.GOLD)
        print(f"{I.IVORY}{'TAG':<15} {'CATEGORY':<15} {'NAME':<40}{I.RESET}")
        print(f"{I.ASH}{'─'*15} {'─'*15} {'─'*40}{I.RESET}")
        
        for tag, info in CUI_TAG_REGISTRY.items():
            print(f" {I.SAFFRON}{tag:<15}{I.RESET} {I.ASH}{info['category']:<15}{I.RESET} {info['name']:<40}")
        
        print(f"\n{I.EMERALD}Total registered tags: {len(CUI_TAG_REGISTRY)}{I.RESET}")
        self.log_action("LIST_TAGS", f"Listed {len(CUI_TAG_REGISTRY)} tags")
    
    def tag_info(self, tag: str) -> None:
        """Display detailed information about a specific tag"""
        tag = tag.upper()
        if tag not in CUI_TAG_REGISTRY:
            print_status(f"Tag '{tag}' not found in registry", "ERROR")
            return
        
        info = CUI_TAG_REGISTRY[tag]
        print_banner(f"TAG DETAILS: {tag}", I.GOLD)
        
        print(f"  {I.IVORY}Name:{I.RESET}        {info['name']}")
        print(f"  {I.IVORY}Category:{I.RESET}     {info['category']}")
        print(f"  {I.IVORY}Description:{I.RESET}  {info['description']}")
        print(f"  {I.IVORY}Handling:{I.RESET}     {info['handling']}")
        print(f"  {I.IVORY}Retention:{I.RESET}    {info['retention']}")
        
        print(f"\n  {I.IVORY}Examples:{I.RESET}")
        for example in info['examples']:
            print(f"    {I.GOLD}•{I.RESET} {example}")
        
        self.log_action("TAG_INFO", f"Viewed tag: {tag}")
    
    def assign_tag(self, doc_id: str, tags: List[str]) -> None:
        """Assign tags to a document"""
        doc = ImperialArchive.get_by_id(doc_id)
        if not doc:
            print_status(f"Document '{doc_id}' not found in imperial archive", "ERROR")
            return
        
        valid_tags = []
        invalid_tags = []
        
        for tag in tags:
            tag = tag.upper()
            if tag in CUI_TAG_REGISTRY:
                if tag not in doc["tags"]:
                    valid_tags.append(tag)
            else:
                invalid_tags.append(tag)
        
        if invalid_tags:
            print_status(f"Invalid tags ignored: {', '.join(invalid_tags)}", "WARNING")
        
        if valid_tags:
            print_status(f"Assigning tags to: {doc['name']}", "INFO")
            spinner(1, "Applying tags")
            
            doc["tags"].extend(valid_tags)
            doc["tags"] = list(set(doc["tags"]))  # Remove duplicates
            
            print_status(f"Tags assigned successfully!", "SUCCESS")
            print(f"  {I.IVORY}Document:{I.RESET} {doc['name']}")
            print(f"  {I.IVORY}Tags:{I.RESET}     {', '.join(doc['tags'])}")
            
            self.log_action("ASSIGN_TAG", f"Assigned {valid_tags} to {doc_id}")
        else:
            print_status("No valid tags to assign", "WARNING")
    
    def remove_tag(self, doc_id: str, tags: List[str]) -> None:
        """Remove tags from a document"""
        doc = ImperialArchive.get_by_id(doc_id)
        if not doc:
            print_status(f"Document '{doc_id}' not found", "ERROR")
            return
        
        removed = []
        for tag in tags:
            tag = tag.upper()
            if tag in doc["tags"]:
                doc["tags"].remove(tag)
                removed.append(tag)
        
        if removed:
            print_status(f"Tags removed successfully!", "SUCCESS")
            print(f"  {I.IVORY}Document:{I.RESET} {doc['name']}")
            print(f"  {I.IVORY}Removed:{I.RESET}  {', '.join(removed)}")
            print(f"  {I.IVORY}Remaining:{I.RESET} {', '.join(doc['tags']) if doc['tags'] else 'None'}")
            self.log_action("REMOVE_TAG", f"Removed {removed} from {doc_id}")
        else:
            print_status("No matching tags found on document", "WARNING")
    
    def search_by_tag(self, tag: str) -> List[Dict]:
        """Search all documents with a specific tag"""
        tag = tag.upper()
        if tag not in CUI_TAG_REGISTRY:
            print_status(f"Tag '{tag}' not in registry", "ERROR")
            return []
        
        print_banner(f"DOCUMENTS TAGGED: {tag}", I.GOLD)
        results = ImperialArchive.search_by_tag(tag)
        
        if results:
            for doc in results:
                print(f"  {I.GOLD}🦁{I.RESET} {doc['id']} - {doc['name']}")
                print(f"     {I.ASH}Path:{I.RESET} {doc['path']}")
                print(f"     {I.ASH}Level:{I.RESET} {doc['level']}")
                print(f"     {I.ASH}Tags:{I.RESET} {', '.join(doc['tags'])}")
                print()
            print_status(f"Found {len(results)} documents", "SUCCESS")
        else:
            print_status(f"No documents found with tag '{tag}'", "INFO")
        
        self.log_action("SEARCH_TAG", f"Searched for tag: {tag}")
        return results
    
    def bulk_assign(self, doc_ids: List[str], tags: List[str]) -> None:
        """Assign tags to multiple documents at once"""
        print_banner("BULK TAG ASSIGNMENT", I.GOLD)
        print_status(f"Processing {len(doc_ids)} documents...", "INFO")
        
        success_count = 0
        for doc_id in doc_ids:
            doc = ImperialArchive.get_by_id(doc_id)
            if doc:
                for tag in tags:
                    tag = tag.upper()
                    if tag in CUI_TAG_REGISTRY and tag not in doc["tags"]:
                        doc["tags"].append(tag)
                success_count += 1
                print(f"  {I.EMERALD}✓{I.RESET} {doc_id}: {doc['name']}")
        
        progress_bar(100, "Applying tags", delay=0.01)
        print_status(f"Tags applied to {success_count}/{len(doc_ids)} documents", "SUCCESS")
        print_status(f"Tags: {', '.join(t.upper() for t in tags)}", "TAG")
        self.log_action("BULK_ASSIGN", f"Bulk assigned {tags} to {success_count} docs")
    
    def validate_tags(self, doc_id: str) -> Dict:
        """Validate tags on a document"""
        doc = ImperialArchive.get_by_id(doc_id)
        if not doc:
            print_status(f"Document '{doc_id}' not found", "ERROR")
            return {}
        
        print_banner(f"TAG VALIDATION: {doc['name']}", I.GOLD)
        
        validation = {
            "document": doc['name'],
            "current_tags": doc['tags'],
            "valid_tags": [],
            "invalid_tags": [],
            "suggested_tags": [],
            "score": 0
        }
        
        for tag in doc['tags']:
            if tag in CUI_TAG_REGISTRY:
                validation["valid_tags"].append(tag)
                validation["score"] += 1
            else:
                validation["invalid_tags"].append(tag)
        
        # Suggest additional tags based on content
        content_keywords = {
            "PROPRIETARY": ["source code", "algorithm", "trade secret"],
            "FINANCIAL": ["revenue", "budget", "expense"],
            "PHI": ["patient", "medical", "health"],
            "DEFENSE": ["military", "weapon", "strategy"],
            "ITINFRA": ["server", "network", "configuration"],
        }
        
        suggested = []
        for tag, keywords in content_keywords.items():
            if tag not in doc['tags']:
                if any(kw in doc['path'].lower() for kw in keywords):
                    suggested.append(tag)
        
        validation["suggested_tags"] = suggested
        
        # Display results
        print(f"\n  {I.IVORY}Valid Tags:{I.RESET}")
        for tag in validation["valid_tags"]:
            print(f"    {I.EMERALD}✓{I.RESET} {tag} - {CUI_TAG_REGISTRY[tag]['name']}")
        
        if validation["invalid_tags"]:
            print(f"\n  {I.IVORY}Invalid Tags:{I.RESET}")
            for tag in validation["invalid_tags"]:
                print(f"    {I.RUBY}✗{I.RESET} {tag} - Not in registry")
        
        if suggested:
            print(f"\n  {I.IVORY}Suggested Tags:{I.RESET}")
            for tag in suggested:
                print(f"    {I.AMBER}⚠{I.RESET} {tag} - Based on content analysis")
        
        print(f"\n  {I.IVORY}Validation Score:{I.RESET} {validation['score']}/{len(doc['tags'])}")
        
        self.log_action("VALIDATE_TAGS", f"Validated tags for {doc_id}")
        return validation
    
    def generate_report(self) -> None:
        """Generate comprehensive tag usage report"""
        print_banner("IMPERIAL TAG REPORT", I.GOLD)
        print_status("Generating tag usage report...", "INFO")
        spinner(1.5, "Compiling statistics")
        
        # Tag usage statistics
        tag_usage = {}
        for doc in ImperialArchive.DOCUMENTS:
            for tag in doc["tags"]:
                tag_usage[tag] = tag_usage.get(tag, 0) + 1
        
        # Classification distribution
        level_distribution = {}
        for doc in ImperialArchive.DOCUMENTS:
            level = doc["level"]
            level_distribution[level] = level_distribution.get(level, 0) + 1
        
        print(f"\n{I.IVORY}{I.BOLD}═══ TAG USAGE STATISTICS ═══{I.RESET}\n")
        print(f"{I.WHITE}{'Tag':<15} {'Count':<10} {'Percentage':<15}{I.RESET}")
        print(f"{I.ASH}{'─'*40}{I.RESET}")
        
        total_tags = sum(tag_usage.values())
        for tag, count in sorted(tag_usage.items(), key=lambda x: x[1], reverse=True):
            pct = (count / total_tags * 100) if total_tags > 0 else 0
            print(f" {I.SAFFRON}{tag:<15}{I.RESET} {count:<10} {pct:.1f}%")
        
        print(f"\n{I.IVORY}{I.BOLD}═══ CLASSIFICATION DISTRIBUTION ═══{I.RESET}\n")
        for level, count in level_distribution.items():
            print(f" {I.GOLD}•{I.RESET} {level:<20}: {count} documents")
        
        print(f"\n{I.IVORY}{I.BOLD}═══ SUMMARY ═══{I.RESET}")
        print(f" Total Documents: {len(ImperialArchive.DOCUMENTS)}")
        print(f" Total Tags Used: {total_tags}")
        print(f" Unique Tags: {len(tag_usage)}")
        
        self.log_action("GENERATE_REPORT", "Generated tag usage report")

# ============================================================
# MAIN APPLICATION
# ============================================================
def main():
    parser = argparse.ArgumentParser(description="MAURYA-TAG - Imperial CUI Tagging Framework")
    parser.add_argument("--list", "-l", action="store_true", help="List all registered tags")
    parser.add_argument("--info", "-i", type=str, help="Get info about a specific tag")
    parser.add_argument("--assign", "-a", nargs=2, metavar=("DOC_ID", "TAGS"),
                       help="Assign tags to document (comma-separated)")
    parser.add_argument("--remove", "-r", nargs=2, metavar=("DOC_ID", "TAGS"),
                       help="Remove tags from document")
    parser.add_argument("--search", "-s", type=str, help="Search documents by tag")
    parser.add_argument("--validate", "-v", type=str, help="Validate document tags")
    parser.add_argument("--report", action="store_true", help="Generate tag report")
    parser.add_argument("--interactive", action="store_true", help="Interactive mode")
    
    args = parser.parse_args()
    system = MauryaTagSystem()
    
    show_banner()
    
    # CLI Mode
    if args.list:
        system.list_tags()
    elif args.info:
        system.tag_info(args.info)
    elif args.assign:
        doc_id, tags_str = args.assign
        tags = [t.strip() for t in tags_str.split(",")]
        system.assign_tag(doc_id, tags)
    elif args.remove:
        doc_id, tags_str = args.remove
        tags = [t.strip() for t in tags_str.split(",")]
        system.remove_tag(doc_id, tags)
    elif args.search:
        system.search_by_tag(args.search)
    elif args.validate:
        system.validate_tags(args.validate)
    elif args.report:
        system.generate_report()
    elif args.interactive:
        interactive_mode(system)
    else:
        interactive_mode(system)

def interactive_mode(system: MauryaTagSystem):
    """Interactive menu-driven mode"""
    while True:
        print(f"""
{I.GOLD}╔═══ {I.IVORY}MAURYA-TAG COMMANDS{I.GOLD} ═══════════════════════════╗
║  {I.WHITE}1.{I.RESET} List All Registered Tags                        {I.GOLD}║
║  {I.WHITE}2.{I.RESET} View Tag Information                             {I.GOLD}║
║  {I.WHITE}3.{I.RESET} Assign Tags to Document                          {I.GOLD}║
║  {I.WHITE}4.{I.RESET} Remove Tags from Document                        {I.GOLD}║
║  {I.WHITE}5.{I.RESET} Search Documents by Tag                          {I.GOLD}║
║  {I.WHITE}6.{I.RESET} Validate Document Tags                           {I.GOLD}║
║  {I.WHITE}7.{I.RESET} Bulk Tag Assignment                              {I.GOLD}║
║  {I.WHITE}8.{I.RESET} List All Documents                               {I.GOLD}║
║  {I.WHITE}9.{I.RESET} Generate Tag Report                              {I.GOLD}║
║  {I.WHITE}0.{I.RESET} Exit                                             {I.GOLD}║
╚═══════════════════════════════════════════════════╝{I.RESET}
""")
        
        choice = input(f"{I.SAFFRON}maurya-tag>{I.RESET} ").strip()
        
        if choice == '0':
            print(f"\n{I.EMERALD}[✓] May your documents remain secure. जय मौर्य!{I.RESET}\n")
            break
        elif choice == '1':
            clear_screen()
            show_banner()
            system.list_tags()
        elif choice == '2':
            tag = input(f"{I.WHITE}[?] Tag code: {I.RESET}").strip()
            system.tag_info(tag)
        elif choice == '3':
            print(f"\n{I.ASH}Available documents:{I.RESET}")
            for doc in ImperialArchive.DOCUMENTS:
                print(f"  {I.GOLD}•{I.RESET} {doc['id']}: {doc['name']}")
            doc_id = input(f"\n{I.WHITE}[?] Document ID: {I.RESET}").strip()
            tags = input(f"{I.WHITE}[?] Tags (comma-separated): {I.RESET}").strip()
            system.assign_tag(doc_id, [t.strip() for t in tags.split(",")])
        elif choice == '4':
            doc_id = input(f"{I.WHITE}[?] Document ID: {I.RESET}").strip()
            tags = input(f"{I.WHITE}[?] Tags to remove: {I.RESET}").strip()
            system.remove_tag(doc_id, [t.strip() for t in tags.split(",")])
        elif choice == '5':
            tag = input(f"{I.WHITE}[?] Tag to search: {I.RESET}").strip()
            system.search_by_tag(tag)
        elif choice == '6':
            doc_id = input(f"{I.WHITE}[?] Document ID: {I.RESET}").strip()
            system.validate_tags(doc_id)
        elif choice == '7':
            print(f"\n{I.ASH}Select documents (comma-separated IDs):{I.RESET}")
            for doc in ImperialArchive.DOCUMENTS:
                print(f"  {I.GOLD}•{I.RESET} {doc['id']}: {doc['name']}")
            doc_ids = input(f"\n{I.WHITE}[?] Document IDs: {I.RESET}").strip()
            tags = input(f"{I.WHITE}[?] Tags: {I.RESET}").strip()
            system.bulk_assign([d.strip() for d in doc_ids.split(",")], 
                             [t.strip() for t in tags.split(",")])
        elif choice == '8':
            print_banner("IMPERIAL ARCHIVE - ALL DOCUMENTS", I.GOLD)
            for doc in ImperialArchive.DOCUMENTS:
                print(f"  {I.GOLD}🦁{I.RESET} {doc['id']} | {doc['name']}")
                print(f"     {I.ASH}Tags:{I.RESET} {', '.join(doc['tags']) if doc['tags'] else 'None'}")
                print(f"     {I.ASH}Level:{I.RESET} {doc['level']}")
                print()
        elif choice == '9':
            system.generate_report()
        else:
            print(f"{I.RUBY}Invalid command.{I.RESET}")
        
        if choice not in ['0', '8']:
            input(f"\n{I.ASH}Press Enter to continue...{I.RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{I.AMBER}[!] Maurya-Tag terminated. जय मौर्य!{I.RESET}\n")
    except Exception as e:
        print(f"\n{I.RUBY}[!] Error: {e}{I.RESET}\n")