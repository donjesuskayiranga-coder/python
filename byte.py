# stegorsa_solver.py
import sys
import re
from Crypto.Util.number import long_to_bytes, inverse

# --- Fix Python 3.13 large integer limit ---
sys.set_int_max_str_digits(100000)

# --- Challenge info ---
image_file = "image.jpg"   # your downloaded image
e = 79                     # given in debug info
ct = 719                   # given ciphertext

# Step 1: Read the image in binary
with open(image_file, "rb") as f:
    data = f.read()

# Step 2: Extract all non-ASCII bytes (likely the hidden private key)
raw_bytes = bytes([b for b in data if b > 127])
if not raw_bytes:
    print("[-] No private key bytes found in image!")
    sys.exit()

print(f"[+] Extracted {len(raw_bytes)} raw bytes for private exponent")

# Step 3: Convert bytes to integer -> candidate private exponent
d = int.from_bytes(raw_bytes, byteorder="big")
print("[+] Candidate private exponent calculated")

# Step 4: Compute a small modulus for tiny CTF numbers
# For this challenge, modulus n can be approximated as p = small number from debug info
# Using n = p for small CTF flag works
n = 114637  # from debug info, tiny modulus

# Step 5: Decrypt ciphertext
m = pow(ct, d, n)

# Step 6: Convert decrypted integer to bytes
flag_bytes = long_to_bytes(m)

# Step 7: Print flag safely
try:
    print("[+] FLAG:", flag_bytes.decode())
except UnicodeDecodeError:
    # fallback: ignore errors and show ASCII characters
    print("[+] FLAG (ASCII fallback):", flag_bytes.decode(errors='ignore'))
    print("[+] FLAG (raw bytes):", flag_bytes)