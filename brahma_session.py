import os
import time
import sys
import threading
from math import ceil

# ==========================================
# BRAHMA-SESSION: THE COSMIC CYCLE THEME
# (5 Unique Non-Repeating Colors)
# ==========================================
LOTUS = '\033[38;5;211m'  # Light Pink (Creation)
VOID  = '\033[38;5;63m'   # Deep Blue/Purple (Space)
KALA  = '\033[38;5;220m'  # Golden Yellow (Time/Entropy)
AURA  = '\033[38;5;159m'  # Soft Cyan (System Text)
STAR  = '\033[38;5;231m'  # Bright White
RST   = '\033[0m'
BLD   = '\033[1m'

# ==========================================
# ADVANCED ANIMATIONS
# ==========================================

def cosmic_lotus_animation():
    """Advanced creation animation using orbital characters."""
    os.system('cls' if os.name == 'nt' else 'clear')
    sys.stdout.write(f"{LOTUS}[*] Initiating Cosmic Session Matrix...{RST}\n")
    
    # Orbital frames simulating an expanding lotus
    frames = [
        "    .    ",
        "   .o.   ",
        "  .oOo.  ",
        " .oO@Oo. ",
        "  .oOo.  ",
        "   .o.   ",
        "    .    "
    ]
    
    # Spin the lotus 3 times
    for _ in range(3):
        for frame in frames:
            sys.stdout.write(f"\r{VOID}[{RST} {LOTUS}{BLD}{frame}{RST} {VOID}]{RST}")
            sys.stdout.flush()
            time.sleep(0.08)
    print(f"\r{STAR}[+]{RST} {AURA}Brahma Session Initialized Successfully.     {RST}\n")
    time.sleep(0.5)

# ==========================================
# ARCHITECTURE: CONCURRENT DAEMON STATE MANAGER
# ==========================================

class SessionState:
    """Thread-safe Singleton object to hold current session data."""
    is_active = False
    username = None
    expiry_time = 0.0
    ttl_seconds = 15  # STRICT 15 SECOND SESSION FOR DEMO PURPOSES
    lock = threading.Lock() # Prevents race conditions between threads

def background_monitor():
    """
    The Daemon Worker. Runs invisibly in the background.
    It constantly monitors the time. If it passes the expiry, it kills the session.
    """
    while True:
        time.sleep(0.5) # Check twice a second
        
        with SessionState.lock:
            if SessionState.is_active:
                current_time = time.time()
                if current_time >= SessionState.expiry_time:
                    # KALA (Time) Destroys the session
                    SessionState.is_active = False
                    SessionState.username = None
                    
                    # Asynchronous Terminal Output (Overwrites current prompt cleanly)
                    sys.stdout.write(f"\r\033[K\n{KALA}{BLD}>> [!] KALA STRIKE: SESSION TTL EXPIRED. <<{RST}\n")
                    sys.stdout.write(f"{VOID}>> Your session was forcefully dissolved by the background daemon.{RST}\n")
                    sys.stdout.write(f"{AURA}brahma{RST}@{STAR}cosmos{RST}:{AURA}~/auth{RST}$ ")
                    sys.stdout.flush()

# Start the background daemon immediately
# daemon=True means this thread will auto-kill when you exit the main script
monitor_thread = threading.Thread(target=background_monitor, daemon=True)
monitor_thread.start()

# ==========================================
# FOREGROUND SHELL INTERFACE (OPTIONS MENU)
# ==========================================

def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = f"""{LOTUS}{BLD}
     ██████╗ ██████╗  █████╗ ██╗  ██╗███╗   ███╗ █████╗ 
     ██╔══██╗██╔══██╗██╔══██╗██║  ██║████╗ ████║██╔══██╗
     ██████╔╝██████╔╝███████║███████║██╔████╔██║███████║
     ██╔══██╗██╔══██╗██╔══██║██╔══██║██║╚██╔╝██║██╔══██║
     ██████╔╝██║  ██║██║  ██║██║  ██║██║ ╚═╝ ██║██║  ██║
     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝ {STAR}S E S S I O N{RST}
    """
    print(banner)
    print(f"{AURA}>> ARCHITECTURE: CONCURRENT DAEMON THREADS & TTL STATE{RST}")
    print(f"{AURA}>> WARNING: SESSIONS AUTOMATICALLY EXPIRE IN {SessionState.ttl_seconds} SECONDS{RST}\n")

def cmd_help():
    print(f"\n{LOTUS}{BLD}--- BRAHMA-SESSION MENU ---{RST}")
    print(f" {STAR}login <user>{RST}  : Create a new session (Triggers animation)")
    print(f" {STAR}status{RST}        : View current active session and remaining TTL")
    print(f" {STAR}renew{RST}         : Reset the Time-To-Live (TTL) clock")
    print(f" {STAR}logout{RST}        : Manually dissolve the session")
    print(f" {STAR}exit{RST}          : Close the program")
    print(f"{LOTUS}{'-'*27}{RST}")

def get_progress_bar(remaining, total, length=20):
    """Draws a visual progress bar for the remaining time."""
    filled = int((remaining / total) * length)
    bar = "█" * filled + "-" * (length - filled)
    color = LOTUS if remaining > (total/2) else KALA
    return f"{color}[{bar}]{RST}"

def run_shell():
    print_banner()
    
    while True:
        try:
            # Interactive Shell Prompt
            prompt = f"{AURA}brahma{RST}@{STAR}cosmos{RST}:{AURA}~/auth{RST}$ "
            raw = input(prompt).strip().split()
            if not raw: continue
            
            cmd = raw[0].lower()
            args = raw[1:]

            if cmd == "help":
                cmd_help()
                
            elif cmd == "login":
                if SessionState.is_active:
                    print(f"{KALA}[!] Session already active. Please logout first.{RST}")
                    continue
                if len(args) < 1:
                    print(f"{KALA}[!] Usage: login <username>{RST}")
                    continue
                    
                cosmic_lotus_animation() # Run the advanced animation
                
                with SessionState.lock:
                    SessionState.is_active = True
                    SessionState.username = args[0].upper()
                    SessionState.expiry_time = time.time() + SessionState.ttl_seconds
                
            elif cmd == "status":
                with SessionState.lock:
                    if SessionState.is_active:
                        remaining = SessionState.expiry_time - time.time()
                        if remaining > 0:
                            bar = get_progress_bar(remaining, SessionState.ttl_seconds)
                            print(f"\n{AURA}IDENTITY: {STAR}{BLD}{SessionState.username}{RST}")
                            print(f"{AURA}STATE:    {LOTUS}ACTIVE{RST}")
                            print(f"{AURA}LIFELINE: {bar} {ceil(remaining)}s remaining{RST}\n")
                        else:
                            print(f"{KALA}[!] Status desync. Session is collapsing...{RST}")
                    else:
                        print(f"{VOID}[*] No active session in the matrix.{RST}")
                        
            elif cmd == "renew":
                with SessionState.lock:
                    if SessionState.is_active:
                        SessionState.expiry_time = time.time() + SessionState.ttl_seconds
                        print(f"{LOTUS}[+] Session TTL refreshed. You have {SessionState.ttl_seconds} seconds.{RST}")
                    else:
                        print(f"{VOID}[-] No active session to renew.{RST}")
                        
            elif cmd == "logout":
                with SessionState.lock:
                    SessionState.is_active = False
                    SessionState.username = None
                print(f"{VOID}[*] Session manually dissolved.{RST}")
                
            elif cmd == "exit":
                print(f"{STAR}[*] Cosmos shutting down. Threads terminating...{RST}")
                break
                
            else:
                print(f"{KALA}[!] Unknown command. Type 'help'.{RST}")
                
        except Exception as e:
            print(f"{KALA}[!] System Error: {e}{RST}")
        except KeyboardInterrupt:
            print(f"\n{STAR}[*] Manual Interrupt detected. Exiting.{RST}")
            break

if __name__ == "__main__":
    run_shell()