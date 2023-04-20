import gmpy2
from Crypto.Util.number import GCD, bytes_to_long, getPrime, inverse, long_to_bytes

e = 3

# n will be 8 * (100 + 100) = 1600 bits strong which is pretty good
while True:
    p = getPrime(256)
    q = getPrime(256)
    phi = (p - 1) * (q - 1)
    try:
        d = inverse(e, phi)
        if d != -1 and GCD(e, phi) == 1:
            break
    except:
        pass

n = p * q

flag = b"flag{dog_is_cat}"
pt = bytes_to_long(flag)
ct = pow(pt, e, n)

print(f"n = {n}")
print(f"e = {e}")
print(f"ct = {ct}")

pt = pow(ct, d, n)
decrypted = long_to_bytes(pt)
assert decrypted == flag

print("flag:", long_to_bytes(gmpy2.iroot(ct, e)[0]).decode())
