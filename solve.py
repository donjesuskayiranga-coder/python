from sympy import factorint
from Crypto.Util.number import long_to_bytes

n = 8749002899132047699790752490331099938058737706735201354674975134719667510377522805717156720453193651
e = 65537
ct = 3834152707673200098217711830451812292969443248147329830146346725533249396845301509591469898509446306

factors = factorint(n)
print("Factors:", factors)

phi = 1
for p, exp in factors.items():
 phi *= (p - 1) * (p ** (exp - 1))

d = pow(e, -1, phi)
m = pow(ct, d, n)
flag = long_to_bytes(m)
print("Flag:", flag.decode())