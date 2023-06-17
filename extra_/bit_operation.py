"""bit operation is much fast than arithmetic operation"""

a = 0
b = 1
print(f"a = : ",a)
print(f"b = : ",b)
print(f"a & b : ",a & b)
print(f"a | b : ", a | b)
print(f"a ^ b : ", a ^ b)
print(f"~ a = ; ", ~a)
print(f"~ b = ; ", ~b)
print(f"a >> 5 : ", a >> 5)
print(f"b << 15 : ", b << 15)

c = 17
d = 21

print(bin(c))
print(bin(d))

print(f"c & d   ", bin( c & d))
print(f"c | d   ", bin( c | d))
print(f"c ^ d   ", bin( c ^ d))

print(f"~c   ", bin(~c))
print(f"~d   ", bin(~d))

print(f" c >> 2", bin(c >> 2))
print(f" d << 2", bin(d << 2))
