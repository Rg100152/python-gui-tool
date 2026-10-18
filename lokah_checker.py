import os
import time
import sys

# ==========================================
# LOKAH-CHECKER: AMBER/GOLD THEME
# ==========================================
AMBER = '\033[38;5;214m'
RED = '\033[91m'
GRN = '\033[92m'
WHT = '\033[97m'
GRY = '\033[90m'
RST = '\033[0m'
BLD = '\033[1m'

# ==========================================
# LOGO ANIMATION MODULE
# ==========================================
def animate_logo():
    """Generates a dynamic boot-up animation for the Lokah terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')
    
    logo_lines = [
        r"  _        ____   _  __  ___   _   _ ",
        r" | |      / __ \ | |/ / / _ \ | | | |",
        r" | |     | |  | || ' / / /_\ \| |_| |",
        r" | |___  | |__| || . \ |  _  ||  _  |",
        r" |_____|  \____/ |_|\_\|_| |_||_| |_|"
    ]
    
    # 1. Drop down effect for the letters
    print(f"{AMBER}{BLD}")
    for line in logo_lines:
        print(line)
        time.sleep(0.15)
    print(f"{RST}")

    # 2. Spinner / Radar Animation
    radar_chars = ["|", "/", "-", "\\", "|", "/", "-", "\\"]
    sys.stdout.write(f"{WHT}[*] INITIALIZING LOKAH VERIFICATION ENGINE... {RST}")
    for _ in range(15):
        for char in radar_chars:
            sys.stdout.write(f"\b{AMBER}{char}{RST}")
            sys.stdout.flush()
            time.sleep(0.05)
    print(f"\b{GRN}[ OK ]{RST}\n")

# ==========================================
# ARCHITECTURE: FORWARD CHAINING EXPERT SYSTEM
# ==========================================

class LogicalRule:
    """A declarative rule for the Expert System."""
    def __init__(self, conditions, conclusion, description):
        # ALL conditions must be in the working memory for this rule to fire
        self.conditions = set(conditions)
        self.conclusion = conclusion
        self.description = description

class LokahInferenceEngine:
    """Evaluates facts against rules to deduce 'Need-to-Know' status."""
    def __init__(self):
        self.rules = []
        self.working_memory = set() # Stores current known facts
        self.audit_log = []

    def add_rule(self, conditions, conclusion, desc):
        self.rules.append(LogicalRule(conditions, conclusion, desc))

    def load_facts(self, facts):
        self.working_memory.update(facts)
        self.audit_log.append(f"Initial Facts Loaded: {facts}")

    def evaluate(self):
        """Forward Chaining: Keep evaluating rules until no new facts are found."""
        print(f"{AMBER}>> COMMENCING FORWARD-CHAINING DEDUCTION...{RST}")
        time.sleep(0.5)
        
        new_facts_found = True
        iteration = 1
        
        while new_facts_found:
            new_facts_found = False
            for rule in self.rules:
                # If rule is not already applied AND all conditions are met
                if rule.conclusion not in self.working_memory and rule.conditions.issubset(self.working_memory):
                    self.working_memory.add(rule.conclusion)
                    new_facts_found = True
                    
                    log_msg = f"Iteration {iteration} | Rule Fired: {rule.description} -> Deduced Fact: [{rule.conclusion}]"
                    print(f"{GRY}{log_msg}{RST}")
                    self.audit_log.append(log_msg)
                    time.sleep(0.3)
            iteration += 1

        print(f"{AMBER}>> DEDUCTION COMPLETE. ANALYZING FINAL STATE.{RST}\n")
        return self._final_verdict()

    def _final_verdict(self):
        """Checks the final state of the Working Memory."""
        if "ACCESS_DENIED" in self.working_memory:
            return False, "HARD REJECT: Security violation detected during inference."
        elif "NEED_TO_KNOW_VERIFIED" in self.working_memory:
            return True, "AUTHORIZED: Strict Need-to-Know criteria mathematically satisfied."
        else:
            return False, "DENIED: Engine could not verify a legitimate need-to-know."

# ==========================================
# REAL-WORLD PROBLEM SETUP & EXECUTION
# ==========================================

def setup_abac_rules(engine):
    """
    Real-world Need-to-Know policies (Attribute-Based Access Control).
    """
    # CLEARANCE RULES
    engine.add_rule(["user_clearance_high", "resource_level_high"], "clearance_match", "User has sufficient clearance for high-level resource.")
    engine.add_rule(["user_clearance_low", "resource_level_high"], "ACCESS_DENIED", "Clearance mismatch. User level too low.")
    
    # PROJECT ASSIGNMENT (THE "NEED TO KNOW" CORE)
    engine.add_rule(["user_in_project_alpha", "resource_is_project_alpha"], "project_match", "User is assigned to the target project.")
    
    # CONTEXTUAL RULES (Time, Status)
    engine.add_rule(["user_status_active", "time_is_working_hours"], "context_valid", "User is active and within operational hours.")
    engine.add_rule(["user_status_on_leave"], "ACCESS_DENIED", "User is currently on leave. Temporary suspension of rights.")
    
    # FINAL CONCLUSION RULE
    engine.add_rule(["clearance_match", "project_match", "context_valid"], "NEED_TO_KNOW_VERIFIED", "All attributes align. Need-to-Know is verified.")

def run_lokah():
    animate_logo()
    
    engine = LokahInferenceEngine()
    setup_abac_rules(engine)
    
    # --- TEST SCENARIO 1: The Valid Request ---
    print(f"{WHT}{BLD}--- SCENARIO 1: Valid Employee Request ---{RST}")
    print(f"{AMBER}Facts: High Clearance, Project Alpha, Active, Working Hours{RST}")
    engine.load_facts(["user_clearance_high", "resource_level_high", "user_in_project_alpha", "resource_is_project_alpha", "user_status_active", "time_is_working_hours"])
    
    success, reason = engine.evaluate()
    if success:
        print(f"{GRN}[+] {reason}{RST}\n")
    else:
        print(f"{RED}[-] {reason}{RST}\n")

    # --- TEST SCENARIO 2: The Need-to-Know Violation ---
    print(f"{WHT}{BLD}--- SCENARIO 2: Executive on Vacation ---{RST}")
    print(f"{AMBER}Facts: High Clearance, Project Alpha, ON LEAVE{RST}")
    # Reset engine memory
    engine.working_memory.clear()
    engine.load_facts(["user_clearance_high", "resource_level_high", "user_in_project_alpha", "resource_is_project_alpha", "user_status_on_leave"])
    
    success, reason = engine.evaluate()
    if success:
        print(f"{GRN}[+] {reason}{RST}\n")
    else:
        print(f"{RED}[-] {reason}{RST}\n")

if __name__ == "__main__":
    try:
        run_lokah()
    except KeyboardInterrupt:
        print(f"\n{RED}[!] LOKAH Engine Halted.{RST}")