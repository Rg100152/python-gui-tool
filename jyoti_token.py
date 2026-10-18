import os
import sys
import time
import hmac
import hashlib
import base64
import json
from datetime import datetime, timedelta

# ==========================================
# JYOTI-TOKEN: RADIANT LIGHT 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;226m', '\033[38;5;231m', '\033[38;5;220m', '\033[38;5;51m', '\033[38;5;208m'
C6, C7, C8, C9, C10  = '\033[38;5;121m', '\033[38;5;196m', '\033[38;5;33m', '\033[38;5;214m', '\033[38;5;250m'
C11, C12, C13, C14, C15 = '\033[38;5;201m', '\033[38;5;93m', '\033[38;5;244m', '\033[38;5;202m', '\033[38;5;240m'
C16, C17, C18, C19, C20 = '\033[38;5;232m', '\033[38;5;124m', '\033[38;5;28m', '\033[38;5;215m', '\033[38;5;233m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE BURNING TORCH (JYOTI)
# ==========================================
def jyoti_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C1}             (  )
    {C1}            (    )         {C1}J Y O T I
    {C3}           |      |        {C5}T O K E N
    {C5}           |      |        {C15}v7.8 [STATELESS_JWT]
    {C13}          /________\\
    {C13}          ----------
    """
    print(logo)
    print(f"{C1}{BLD}   JYOTI-TOKEN: SECURE JSON WEB TOKEN (JWT) GENERATOR{RST}\n")
    
    # Token construction animation
    layers = ["Header_Gen", "Payload_Encode", "Secret_Signing", "Integrity_Seal"]
    for l in layers:
        sys.stdout.write(f"\r{C15}[{C1}LIGHT{C15}] {C2}Igniting Token Layer: {C4}{l:<20}{RST}")
        sys.stdout.flush()
        time.sleep(0.3)
    print(f"\n{C6}[+] Jyoti is burning. Cryptographic signatures are active.{RST}\n")

# ==========================================
# ARCHITECTURE: TOKEN GENERATION ENGINE
# ==========================================
class JyotiTokenEngine:
    """Simulates a secure JWT-like token generation and validation engine."""
    def __init__(self, secret_key):
        self.secret_key = secret_key.encode()

    def _b64_encode(self, data):
        return base64.urlsafe_b64encode(json.dumps(data).encode()).decode().strip("=")

    def generate_token(self, user_id, scope):
        """Creates a signed token for a user."""
        header = {"alg": "HS256", "typ": "JWT"}
        payload = {
            "sub": user_id,
            "scope": scope,
            "iat": int(time.time()),
            "exp": int(time.time()) + 3600,
            "jti": hashlib.md5(str(time.time()).encode()).hexdigest()[:8]
        }
        
        # Structure: Header.Payload.Signature
        unsigned_token = f"{self._b64_encode(header)}.{self._b64_encode(payload)}"
        signature = hmac.new(self.secret_key, unsigned_token.encode(), hashlib.sha256).hexdigest()
        
        full_token = f"{unsigned_token}.{signature[:20]}"
        
        ts = datetime.now().strftime("%H:%M:%S")
        print(f"{C15}[{ts}] {C4}GENERATING: {C1}{user_id}{RST} | Scope: {C9}{scope}{RST}")
        time.sleep(1)
        return full_token

    def validate_token(self, token):
        """Verifies token integrity and expiration."""
        ts = datetime.now().strftime("%H:%M:%S")
        try:
            parts = token.split('.')
            if len(parts) != 3: raise ValueError("MALFORMED")
            
            header, payload, signature = parts
            unsigned_token = f"{header}.{payload}"
            
            # Recalculate signature to verify integrity
            expected_sig = hmac.new(self.secret_key, unsigned_token.encode(), hashlib.sha256).hexdigest()[:20]
            
            if not hmac.compare_digest(signature, expected_sig):
                self._trigger_token_alert(ts, "SIGNATURE_INVALID / TAMPERED")
                return False
            
            # Check Expiration (Simulation)
            print(f"{C15}[{ts}] {C6}VERIFYING: {C2}Token Signature OK...{RST}")
            time.sleep(0.5)
            print(f"    {C11}[✔] TOKEN VALIDATED. User Identity: {C1}Authenticated.{RST}\n")
            return True

        except Exception as e:
            self._trigger_token_alert(ts, str(e))
            return False

    def _trigger_token_alert(self, ts, reason):
        print(f"\n{C7}{BLD}!!! JYOTI-TOKEN: CRYPTOGRAPHIC FORGERY DETECTED !!!{RST}")
        print(f"{C7}│ {C2}TIMESTAMP : {C10}{ts}{RST}")
        print(f"{C7}│ {C2}VIOLATION : {C7}{BLD}{reason}{RST}")
        print(f"{C7}│ {C2}ACTION    : {C7}{BLD}REVOKING_ACCESS | LOGGING_ATTEMPT_TO_PROCTOR{RST}")
        print(f"{C7}└{'─'*55}{RST}\n")
        time.sleep(0.5)

# ==========================================
# SIMULATION: TOKEN LIFECYCLE
# ==========================================
if __name__ == "__main__":
    try:
        SECRET = "VBSPU_BCA_DEPT_SECRET_2026"
        jyoti_banner_anim()
        engine = JyotiTokenEngine(SECRET)
        
        # Scenario 1: Valid Login & Token Generation
        user_token = engine.generate_token("Raj_Gautam", "CUI_READ_WRITE")
        print(f"{C13}    >> ISSUED TOKEN: {C4}{user_token}{RST}\n")
        time.sleep(1)

        # Scenario 2: Legitimate Access with the Token
        engine.validate_token(user_token)
        
        # Scenario 3: Malicious Tampering Simulation
        time.sleep(1)
        tampered_token = user_token[:-5] + "hackr" # Changing the signature
        engine.validate_token(tampered_token)

    except KeyboardInterrupt:
        print(f"\n{C7}[!] Light Extinguished.{RST}")

        