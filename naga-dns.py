import time
import sys
import os
import random

# --- 20 Hacking Colors (ANSI 256-color palette) ---
# Format: \033[38;5;Nm (N is the color code)
COLORS = [
    "46", "47", "48", "49", "51",   # Greens & Cyans
    "81", "75", "63", "93", "165",  # Blues & Purples
    "198", "201", "160", "196", "202", # Pinks & Reds
    "208", "214", "220", "226", "15"  # Oranges, Yellows & White
]

def get_color(code):
    return f"\033[38;5;{code}m"

RESET = "\033[0m"
BOLD = "\033[1m"

def typewriter(text, color_code, delay=0.03):
    """Typewriter effect animation"""
    sys.stdout.write(get_color(color_code) + BOLD)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET + "\n")

def naga_logo():
    """Manual ASCII Logo for Naga-DNS"""
    logo = r"""
    _   __                 ____  _   _______
   / | / /___ _____ _____ _/ __ \/ | / / ___/
  /  |/ / __ `/ __ `/ __ `/ / / /  |/ /\__ \ 
 / /|  / /_/ / /_/ / /_/ / /_/ / /|  /___/ / 
/_/ |_/\__,_/\__, /\__,_/_____/_/ |_//____/  
            /____/                           
    """
    os.system('clear')
    lines = logo.splitlines()
    for i, line in enumerate(lines):
        # Shifting through the 20 colors for the logo
        color = COLORS[i % len(COLORS)]
        print(get_color(color) + BOLD + line + RESET)
        time.sleep(0.1)
    
    print(f"\n{get_color(51)}[SYSTEM]{RESET} {BOLD}Naga-DNS Interceptor Active...{RESET}\n")

def boot_anim():
    """Hacker-style boot sequence"""
    tasks = [
        "Loading Naga-Core...",
        "Bypassing DNS Cache...",
        "Injecting Filter Hooks...",
        "Establishing Stealth Tunnel...",
        "Naga is watching..."
    ]
    for task in tasks:
        color = random.choice(COLORS)
        sys.stdout.write(f"{get_color(color)}[+] {task}{RESET}")
        for _ in range(3):
            time.sleep(0.3)
            sys.stdout.write(".")
            sys.stdout.flush()
        print(" [OK]")

def simulate_logs():
    """Real-time scrolling logs animation"""
    sites = [
        ("malware-traffic.ru", "BLOCKED", "160"),
        ("google.com", "ALLOWED", "46"),
        ("tracker.pixel.io", "DROPPED", "208"),
        ("github.com", "ALLOWED", "46"),
        ("pwned-check.net", "BLOCKED", "160")
    ]
    
    print(f"\n{BOLD}{'TIME':<12} {'DOMAIN':<25} {'STATUS':<15}{RESET}")
    print("-" * 55)
    
    for _ in range(8):
        site, status, s_color = random.choice(sites)
        curr_time = time.strftime("%H:%M:%S")
        
        # Picking a random color for the line from our 20 colors
        line_color = random.choice(COLORS)
        
        output = f"{get_color(line_color)}{curr_time:<12} {site:<25} {get_color(s_color)}{BOLD}{status}{RESET}"
        print(output)
        time.sleep(0.7)

def main_table():
    """Final summary table using simple characters"""
    print(f"\n{get_color(51)}+--------------------------------------------+")
    print(f"| {BOLD}NAGA-DNS SESSION SUMMARY{RESET}{get_color(51):>19} |")
    print(f"+--------------------------------------------+")
    
    stats = [
        ("TOTAL PACKETS", "1,240", "51"),
        ("BLOCKED SITES", "86", "160"),
        ("SINKHOLED IPS", "12", "201"),
        ("SYSTEM UPTIME", "00:45:12", "46")
    ]
    
    for label, val, c in stats:
        print(f"| {label:<20} | {get_color(c)}{val:>17}{RESET}{get_color(51)} |")
    
    print(f"+--------------------------------------------+{RESET}")

if __name__ == "__main__":
    try:
        naga_logo()
        boot_anim()
        simulate_logs()
        main_table()
        print(f"\n{get_color(196)}[ALERT]{RESET} Naga-DNS is running in stealth mode. Press Ctrl+C to stop.")
        while True: time.sleep(1) # Keep running
    except KeyboardInterrupt:
        print(f"\n\n{get_color(208)}[!] Naga-DNS shutting down safely... Good Bye Raj.{RESET}")