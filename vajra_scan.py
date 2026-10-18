import os
import time
import random

class VajraScan:
    """
    Project Vajra-Scan: Automated CUI (Controlled Unclassified Information) Classifier.
    Analyzes document text to determine sensitivity levels and required markings.
    """
    
    def __init__(self):
        # Threat intelligence and keyword dictionaries
        self.cui_indicators = [
            "proprietary", "export controlled", "financial data", 
            "pii", "phi", "aadhar", "passport", "internal use only"
        ]
        self.secret_indicators = [
            "top secret", "classified", "weapon schematic", 
            "national security", "zero-day"
        ]
        
    def _simulate_delay(self, min_time=0.1, max_time=0.5):
        """Simulates network/processing delay for the hacker aesthetic."""
        time.sleep(random.uniform(min_time, max_time))

    def log_status(self, message, msg_type="info"):
        """Displays formatted console output."""
        if msg_type == "info":
            print(f"[*] {message}")
        elif msg_type == "success":
            print(f"[+] {message}")
        elif msg_type == "warning":
            print(f"[!] {message}")
        elif msg_type == "error":
            print(f"[-] {message}")
        self._simulate_delay()

    def display_banner(self):
        """Prints the hacker-style ASCII banner."""
        banner = """
        _    _      _               _____                 
       | |  | |    (_)             / ____|                
       | |  | | __ _ _ _ __ __ _  | (___   ___ __ _ _ __  
       | |/\| |/ _` | | '__/ _` |  \___ \ / __/ _` | '_ \ 
       \  /\  / (_| | | | | (_| |  ____) | (_| (_| | | | |
        \/  \/ \__,_| |_|  \__,_| |_____/ \___\__,_|_| |_|
                   _/ |                                   
                  |__/                                    
        """
        print(banner)
        print("=" * 60)
        print(" PROJECT: VAJRA-SCAN (Automated Content Classifier)")
        print(" REGION/ORIGIN: INDIA DOMAIN")
        print(" STATUS: SYSTEM ONLINE AND READY")
        print("=" * 60 + "\n")

    def generate_dummy_file(self, filename="target_document.txt"):
        """Creates a dummy file for testing purposes if one doesn't exist."""
        self.log_status(f"Locating target: {filename}...", "info")
        if not os.path.exists(filename):
            self.log_status("Target not found. Generating dummy test file...", "warning")
            with open(filename, "w") as file:
                file.write("This is an employee record containing Aadhar details and proprietary code.")
            self.log_status(f"Dummy file '{filename}' injected successfully.", "success")
        else:
            self.log_status("Target acquired.", "success")

    def analyze_document(self, filename):
        """Scans the document and calculates the sensitivity threat level."""
        self.log_status(f"Initializing deep scan on {filename}...", "info")
        
        try:
            with open(filename, "r") as file:
                content = file.read().lower()
        except Exception as e:
            self.log_status(f"Access Denied or Error reading file: {e}", "error")
            return

        self._simulate_delay(1.0, 2.0) # Simulating deep text analysis
        
        # Scoring logic
        cui_hits = sum(1 for word in self.cui_indicators if word in content)
        secret_hits = sum(1 for word in self.secret_indicators if word in content)

        self.log_status("Hex-dump parsing complete. Compiling metrics...", "info")
        print("-" * 40)
        print(f" CUI Keywords Detected:    {cui_hits}")
        print(f" SECRET Keywords Detected: {secret_hits}")
        print("-" * 40)

        # Classification decision matrix
        if secret_hits > 0:
            self._apply_classification("RESTRICTED / SECRET")
        elif cui_hits > 0:
            self._apply_classification("CUI (Controlled Unclassified Information)")
        else:
            self._apply_classification("PUBLIC / UNCLASSIFIED")

    def _apply_classification(self, level):
        """Final output formatter for the scan results."""
        self._simulate_delay(0.5, 1.0)
        print("\n" + "=" * 60)
        print(f" FINAL CLASSIFICATION: [ {level} ]")
        print("=" * 60 + "\n")
        self.log_status("Scan sequence terminated safely. Exiting routine.", "success")


# Execution Block
if __name__ == "__main__":
    # Initialize the scanner object
    scanner = VajraScan()
    
    # Run the sequence
    scanner.display_banner()
    
    # For Thonny, we will create a dummy text file to scan automatically
    target_file = "payload_data.txt"
    scanner.generate_dummy_file(target_file)
    
    # Begin classification
    scanner.analyze_document(target_file)