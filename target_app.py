
def secure_login(user_input):
    secret_key = "admin_super_password_123"  # VULN: Hardcoded Secret
    if user_input == secret_key:
        print("Logged in!")
        
def run_system_command(cmd):
    eval(cmd)  # VULN: Remote Code Execution (RCE)
    exec("import os; os.system(cmd)") # VULN: RCE
    
db_password = 'root' # VULN: Hardcoded Secret
