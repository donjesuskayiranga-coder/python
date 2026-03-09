from string import ascii_uppercase

ciphertext = "NOUNWGBMFKT"

def modinv(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def decrypt_affine(ciphertext, a, b):
    m = 26
    a_inv = modinv(a, m)
    if a_inv is None:
        return None
    plaintext = ""
    for c in ciphertext:
        if c.isalpha():
            y = ascii_uppercase.index(c)
            x = (a_inv * (y - b)) % m
            plaintext += ascii_uppercase[x]
        else:
            plaintext += c
    return plaintext

valid_a = [1,3,5,7,9,11,15,17,19,21,23,25]

for a in valid_a:
    for b in range(26):
        decrypted = decrypt_affine(ciphertext, a, b)
        if decrypted is not None:
            print(f"a={a}, b={b} -> {decrypted}")