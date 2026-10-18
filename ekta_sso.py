import os
import sys
import time
import uuid
import hmac
import hashlib
from datetime import datetime, timedelta

# ==========================================
# EKTA-SSO: UNIFIED HARMONY 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;220m', '\033[38;5;231m', '\033[38;5;33m', '\033[38;5;208m', '\033[38;5;244m'
C6, C7, C8, C9, C10  = '\033[38;5;51m', '\033[38;5;93m', '\033[38;5;118m', '\033[38;5;252m', '\033[38;5;94m'
C11, C12, C13, C14, C15 = '\033[38;5;30m', '\033[38;5;160m', '\033[38;5;226m', '\033[38;5;202m', '\033[38;5;240m'
C16, C17, C18, C19, C20 = '\033[38;5;232m', '\033[38;5;124m', '\033[38;5;28m', '\033[38;5;214m', '\033[38;5;233m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE UNIFIED CIRCLE (EKTA)
# ==========================================
def ekta_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C3}             .---.
    {C3}            / {C1}SSO{C3} \\         {C1}E K T A
    {C1}           | {C3}(---){C1} |        {C6}S S O
    {C3}            \\ {C1}ONE{C3} /         {C15}v7.5 [OIDC_ENGINE]
    {C1}             '---'
    {C13}          [{C8}CENTRAL_IDP{C13}]
    """
    print(logo)
    print(f"{C3}{BLD}   EKTA-SSO: FEDERATED IDENTITY & UNIFIED AUTHENTICATION{RST}\n")
    
    # Trust federation animation
    apps = ["CUI_Inventory", "Staff_Portal", "Cloud_Storage", "Admin_Logs"]
    for app in apps:
        sys.stdout.write(f"\r{C5}[{C1}FEDERATE{C5}] {C2}Linking Service Provider: {C6}{app:<18}{RST}")
        sys.stdout.flush()
        time.sleep(0.3)
    print(f"\n{C8}[+] Identity Federation Complete. Single point of entry established.{RST}\n")

# ==========================================
# ARCHITECTURE: IDENTITY PROVIDER (IDP)
# ==========================================
class EktaIdP:
    """Simulates a Central Identity Provider generating signed Auth Tokens."""
    def __init__(self):
        self.signing_key = b"EKTA_SECRET_KEY_7788"
        self.session_store = {}

    def login(self, user, password):
        """Authenticates user at the central hub."""
        ts = datetime.now().strftime("%H:%M:%S")
        print(f"{C15}[{ts}] {C11}IDP_HUB: {C1}Verifying master credentials for {user}...{RST}")
        time.sleep(1)
        
        # Simple auth check for simulation
        if user == "raj_g" and password == "Kshatriya#2026":
            token = self._generate_jwt(user)
            self.session_store[user] = token
            print(f"{C8}    [✔] Success. Master Session Established.{RST}")
            return token
        return None

    def _generate_jwt(self, user):
        """Simulates a signed JSON Web Token (JWT)."""
        header = "HS256"
        payload = f"user:{user},exp:3600"
        signature = hmac.new(self.signing_key, f"{header}.{payload}".encode(), hashlib.sha256).hexdigest()
        return f"{header}.{payload}.{signature[:10]}"

class ServiceProvider:
    """Simulates a satellite application relying on SSO token."""
    def __init__(self, name):
        self.name = name

    def access_resource(self, token):
        print(f"{C13}[*] APP {self.name}: {C2}Validating SSO Token...{RST}")
        time.sleep(0.8)
        if token and "user:raj_g" in token:
            print(f"    {C8}[✔] Token Valid. Access to {self.name} Granted via EKTA Federation.{RST}\n")
            return True
        print(f"    {C12}[!] Invalid/Missing Token. Redirecting to Ekta-IdP...{RST}\n")
        return False

# ==========================================
# SIMULATION: UNIFIED LOGIN FLOW
# ==========================================
if __name__ == "__main__":
    try:
        ekta_banner_anim()
        idp = EktaIdP()
        
        # Step 1: Login once at the Hub
        sso_token = idp.login("raj_g", "Kshatriya#2026")
        print(f"{C5}    >> SSO_TOKEN: {sso_token}{RST}\n")
        time.sleep(1)

        # Step 2: Access multiple apps without re-logging in
        apps = [ServiceProvider("CUI_VAULT"), ServiceProvider("UNIVERSITY_LOGS")]
        for app in apps:
            app.access_resource(sso_token)

        # Step 3: Attempt access without token (Failure)
        malicious_app = ServiceProvider("SENSITIVE_DB")
        malicious_app.access_resource(None)

    except KeyboardInterrupt:
        print(f"\n{C12}[!] SSO Services Offline.{RST}")