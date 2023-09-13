from math import sqrt

def real_sqrt(n):
    if n > 0:
        return sqrt(n)
    else:
        return 0
    
print(real_sqrt(16))
print(real_sqrt(-9))