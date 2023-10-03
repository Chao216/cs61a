from math import gcd # greatest common divisor, gcd is moved to math module now !

print(gcd(12,64))

def rational(x,y):
    g = gcd(x,y)

    return[x//g,y//g]

# print(rational(64,61440))

def numer(x):
    return x[0]

def denom(x):
    return x[1]

print(numer(rational(4,12)))
print(denom(rational(9,3)))

def mul_rational(x,y):
    up = numer(x) * numer(y)
    lo = denom(x) * denom(y)
    return rational(up,lo)

print(mul_rational(rational(1,3),rational(1,2)))