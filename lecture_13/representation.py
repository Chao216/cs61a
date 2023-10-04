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

def add_rational(x,y):
    up = numer(x) * denom(y) + numer(y)* denom(x)
    lo = denom(x) * denom(y)
    return rational(up,lo)

print(add_rational(rational(3,7),rational(1,14)))

# Always Remember abstraction in computer science. 

def div_rational(x,y):
    """
    1/3 / 1/2 = 1/3 * 2/1
    """
    up = numer(x)*denom(y)
    lo = denom(x) * numer(y)
    return rational(up,lo)

print(div_rational(rational(1,3),rational(1,6)))

def eq_ratioal(x,y):
    return rational(x) == rational(y)

r1 = rational(1,3)
r2 = rational(2,6)
print(eq_ratioal(r1,r2))