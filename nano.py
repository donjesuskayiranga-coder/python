#!/usr/bin/env python3
"""
Exploit for "Secure Dot Product" - picoCTF (300pts, Cryptography)

VULNERABILITY:
  parse_vector() sanitizes input keeping only '0123456789,[]'
  This STRIPS MINUS SIGNS from negative numbers.

  hash_vector() is called on the decoded (unicode-unescaped) string.

  So: trusted vector [-5, 3, -2]  has hash H for string "[-5, 3, -2]"
  We submit "[-5, 3, -2]" → hash check PASSES (same string)
  But parse_vector strips '-' → parses as [5, 3, 2]
  Server computes: dot([5,3,2], key) = 5·k0 + 3·k1 + 2·k2

  Result: we learn sum(|vi| * key[i])  (absolute-value dot product)

KEY RECOVERY:
  5 trusted vectors give 5 equations in 32 unknowns (key bytes ∈ [0,255]).
  Use LLL lattice reduction (Hidden Number Problem / Kannan embedding).
  Requires SageMath: run with `sage exploit.py`
  Falls back to numpy if rank happens to be 32 (unlikely but possible).

  The challenge says "might not always be solvable" → retry until LLL succeeds.

USAGE:
  sage exploit.py            (recommended)
  python3 exploit.py         (needs SageMath or lucky rank-32 case)
"""

import ast, sys, time, socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

HOST = "lonely-island.picoctf.net"
PORT = 53820      # ← update if your instance uses a different port
KEY_LEN = 32


class Conn:
    def __init__(self):
        self.s = socket.create_connection((HOST, PORT), timeout=20)
        self._buf = b""
    def _recv(self):
        d = self.s.recv(4096)
        if not d: raise EOFError
        self._buf += d
    def recvuntil(self, d):
        if isinstance(d, str): d = d.encode()
        while d not in self._buf: self._recv()
        i = self._buf.index(d) + len(d)
        r, self._buf = self._buf[:i], self._buf[i:]
        return r
    def recvline(self): return self.recvuntil(b"\n")
    def sendline(self, d):
        if isinstance(d, str): d = d.encode()
        self.s.sendall(d + b"\n")
    def close(self): self.s.close()


def lll_solve(equations):
    """Recover 32-byte key from (coefficients, dot_product) equations via LLL."""
    m = len(equations)
    A = [eq[0] for eq in equations]
    b = [eq[1] for eq in equations]

    try:
        from sage.all import Matrix, ZZ
        # Kannan embedding: x = y + 128, y in [-128,127]
        # A(y+128) = b  =>  Ay = b - 128*row_sums
        b2 = [b[i] - 128 * sum(A[i]) for i in range(m)]
        S, N = 2**30, 256
        dim = m + KEY_LEN + 1
        M = Matrix(ZZ, dim, dim)
        for i in range(m):            M[i, i] = S
        for i in range(m):
            for j in range(KEY_LEN): M[i, m+j] = A[i][j]
        for j in range(KEY_LEN):      M[m+j, m+j] = N
        for i in range(m):            M[dim-1, i] = (-b2[i]) % S
        M[dim-1, dim-1] = 1

        print("[*] Running LLL via SageMath...")
        for row in M.LLL():
            y = list(row)[m:m+KEY_LEN]
            x = [yi+128 for yi in y]
            if not all(0 <= xi <= 255 for xi in x): continue
            key = bytes(x)
            if all(sum(A[i][j]*key[j] for j in range(KEY_LEN))==b[i] for i in range(m)):
                print("[+] LLL: key found!")
                return key
        print("[-] LLL did not find key this round")
        return None
    except ImportError:
        pass

    # numpy fallback (only works if matrix rank == 32)
    try:
        import numpy as np
        A_np = np.array(A, dtype=float)
        b_np = np.array(b, dtype=float)
        rank = np.linalg.matrix_rank(A_np)
        print(f"[*] numpy fallback, rank={rank}/{KEY_LEN}")
        if rank >= KEY_LEN:
            x, *_ = np.linalg.lstsq(A_np, b_np, rcond=None)
            key = bytes(max(0,min(255,round(xi))) for xi in x)
            if all(sum(A[i][j]*key[j] for j in range(KEY_LEN))==b[i] for i in range(m)):
                return key
    except ImportError:
        print("[-] numpy not available either")
    return None


def attempt():
    conn = Conn()
    try:
        conn.recvuntil(b"IV: ")
        iv = bytes.fromhex(conn.recvline().strip().decode())
        conn.recvuntil(b"Ciphertext: ")
        ct = bytes.fromhex(conn.recvline().strip().decode())
        print(f"IV:  {iv.hex()}")
        print(f"CT:  {ct.hex()}")

        conn.recvuntil(b"Here are the vectors I trust won't leak my key:\n")
        trusted = []
        for _ in range(5):
            line = conn.recvline().strip().decode()
            sep = line.rfind(", '")
            vec = ast.literal_eval(line[1:sep])
            h   = line[sep+3:-2]
            trusted.append((vec, h))
            print(f"  trusted len={len(vec)}: {vec[:3]}{'...' if len(vec)>3 else ''}")

        conn.recvuntil(b"========================================================\n")
        equations = []
        for i, (vec, h) in enumerate(trusted):
            conn.sendline(str(vec))          # exact trusted string → hash passes
            conn.recvuntil(b"Enter its salted hash: ")
            conn.sendline(h)
            resp = conn.recvuntil(b"========================================================\n").decode()
            if "dot product is:" not in resp:
                print(f"[-] Query {i} rejected: {resp[:60]}")
                return None
            dp = int(resp.split("dot product is: ")[1].split()[0])
            coeffs = [0]*KEY_LEN
            for j,v in enumerate(vec[:KEY_LEN]): coeffs[j] = abs(v)
            equations.append((coeffs, dp))
            print(f"  eq {i}: dp={dp}")

        # Check for unit vectors (lucky case)
        known = {}
        for coeffs, dp in equations:
            nz = [(j,c) for j,c in enumerate(coeffs) if c]
            if len(nz)==1:
                j,c = nz[0]
                if dp%c==0 and 0<=dp//c<=255:
                    known[j]=dp//c
                    print(f"[+] Direct: key[{j}]={known[j]}")

        key = None
        if len(known)==KEY_LEN:
            key = bytes(known[j] for j in range(KEY_LEN))
        else:
            key = lll_solve(equations)

        if not key:
            return None
        print(f"Key: {key.hex()}")

        cipher = AES.new(key, AES.MODE_CBC, iv)
        try:
            return unpad(cipher.decrypt(ct), 16).decode()
        except Exception as e:
            print(f"[-] Decrypt error: {e}")
            return None
    finally:
        conn.close()


for n in range(1, 200):
    print(f"\n── Attempt {n} ──")
    try:
        flag = attempt()
        if flag:
            print(f"\n★ FLAG: {flag}")
            sys.exit(0)
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(1)
