import os
import time
import math
import random

# ==========================================
# SARNATH-CLASSIFIER: NEURAL THEME
# ==========================================
GRN = '\033[92m'  # Success / Weights
CYN = '\033[96m'  # Info / Neural
WHT = '\033[97m'  # System
YLW = '\033[93m'  # Probability / Warning
RED = '\033[91m'  # Critical
RST = '\033[0m'   # Reset
BLD = '\033[1m'

# ==========================================
# PROBABILISTIC ML ARCHITECTURE
# ==========================================

class SarnathInferenceEngine:
    """
    Implements a Naive Bayes-style classification architecture.
    Calculates document probability across multiple CUI domains.
    """
    def __init__(self):
        # Neural weights: Probabilities assigned to keywords per category
        # Weights represent: { "keyword": { "Category": Probability_Weight } }
        self.model_weights = {
            "exploit":    {"CUI_TECHNICAL": 0.85, "CUI_LEGAL": 0.05, "PUBLIC": 0.10},
            "firewall":   {"CUI_TECHNICAL": 0.90, "CUI_LEGAL": 0.02, "PUBLIC": 0.08},
            "litigation": {"CUI_TECHNICAL": 0.05, "CUI_LEGAL": 0.95, "PUBLIC": 0.00},
            "statute":    {"CUI_TECHNICAL": 0.01, "CUI_LEGAL": 0.88, "PUBLIC": 0.11},
            "meeting":    {"CUI_TECHNICAL": 0.10, "CUI_LEGAL": 0.10, "PUBLIC": 0.80},
            "weather":    {"CUI_TECHNICAL": 0.05, "CUI_LEGAL": 0.05, "PUBLIC": 0.90},
            "aadhar":     {"CUI_TECHNICAL": 0.40, "CUI_LEGAL": 0.50, "PUBLIC": 0.10}
        }
        self.categories = ["CUI_TECHNICAL", "CUI_LEGAL", "PUBLIC"]

    def load_neural_weights(self):
        """Simulates the loading of a pre-trained ML model."""
        print(f"{CYN}[*] Loading Sarnath-v1 Inference Model...{RST}")
        for i in range(1, 6):
            print(f"{GRN}    ↳ Initializing Neural Layer {i}... [OK]{RST}")
            time.sleep(0.3)
        print(f"{GRN}[+] 512-bit Weight Matrix synchronized.{RST}\n")

    def predict(self, text):
        """
        Calculates the probability of each category using logarithmic scoring.
        """
        words = text.lower().split()
        scores = {cat: 0.0 for cat in self.categories}
        
        print(f"{CYN}[*] Commencing probabilistic analysis of input stream...{RST}")
        
        # We use Log-sum to prevent floating point underflow (Standard ML practice)
        for word in words:
            if word in self.model_weights:
                print(f"{WHT}    - Feature detected: {BLD}{word}{RST}")
                for cat in self.categories:
                    weight = self.model_weights[word].get(cat, 0.01)
                    scores[cat] += math.log(weight)
                time.sleep(0.1)

        # Convert log scores back to a readable percentage distribution
        # This is a simplified Softmax-style normalization
        exp_scores = {cat: math.exp(score) for cat, score in scores.items()}
        total = sum(exp_scores.values())
        probabilities = {cat: (val / total) * 100 for cat, val in exp_scores.items()}
        
        return probabilities

# ==========================================
# SYSTEM EXECUTION & AESTHETICS
# ==========================================

def display_sarnath_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = f"""{GRN}{BLD}
     ███████╗ █████╗ ██████╗ ███╗   ██╗ █████╗ ████████╗██╗  ██╗
     ██╔════╝██╔══██╗██╔══██╗████╗  ██║██╔══██╗╚══██╔══╝██║  ██║
     ███████╗███████║██████╔╝██╔██╗ ██║███████║   ██║   ███████║
     ╚════██║██╔══██║██╔══██╗██║╚██╗██║██╔══██║   ██║   ██╔══██║
     ███████║██║  ██║██║  ██║██║ ╚████║██║  ██║   ██║   ██║  ██║
     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝
     {WHT}C L A S S I F I C A T I O N   M L   E N G I N E{RST}
    """
    print(banner)
    print(f"{CYN}>> ARCHITECTURE: BAYESIAN INFERENCE PROBABILITY MATRIX{RST}")
    print(f"{CYN}>> MODULE: SARNATH-V1 (PRE-TRAINED){RST}\n")

def run_engine():
    display_sarnath_banner()
    
    # 1. Initialize Engine
    engine = SarnathInferenceEngine()
    engine.load_neural_weights()
    
    # 2. Input Payload
    payload = "The firewall audit revealed a critical exploit related to the Aadhar database."
    print(f"{WHT}TARGET PAYLOAD: {RST}'{payload}'\n")
    
    # 3. Perform Inference
    time.sleep(1)
    results = engine.predict(payload)
    
    # 4. Display Probability Distribution
    print(f"\n{CYN}{BLD}============== INFERENCE REPORT =============={RST}")
    # Sort categories by highest percentage first
    sorted_results = sorted(results.items(), key=lambda item: item[1], reverse=True)
    
    for category, prob in sorted_results:
        color = GRN if prob > 50 else (YLW if prob > 20 else WHT)
        bar = "█" * int(prob / 5)
        print(f" {category:<15} : {color}{prob:>6.2f}% {bar}{RST}")
    
    # 5. Final Suggestion
    suggestion = sorted_results[0][0]
    confidence = sorted_results[0][1]
    
    print(f"{CYN}{'-'*46}{RST}")
    print(f"{WHT}SUGGESTED LABEL: {BLD}{suggestion}{RST}")
    print(f"{WHT}CONFIDENCE LEVEL: {GRN if confidence > 70 else YLW}{confidence:.2f}%{RST}")
    print(f"{CYN}{'-'*46}{RST}")

if __name__ == "__main__":
    try:
        run_engine()
    except KeyboardInterrupt:
        print(f"\n{RED}[!] Neural link severed by operator.{RST}")