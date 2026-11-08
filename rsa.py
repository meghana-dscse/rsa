p = int(input("Enter p: "))
q = int(input("Enter q: "))
e = int(input("Enter public key e: "))
m = int(input("Enter message: "))

n = p * q
phi = (p-1) * (q-1)

d = pow(e, -1, phi)

c = pow(m, e, n)
print("Encrypted:", c)

print("Decrypted:", pow(c, d, n))