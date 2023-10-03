from math import gcd # greatest common divisor, gcd is moved to math module now !

print(gcd(12,64))

def rational(x,y):
    g = gcd(x,y)

    return[x//g,y//g]

print(rational(64,61440))