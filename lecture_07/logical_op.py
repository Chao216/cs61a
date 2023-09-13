from math import sqrt

# AND

def has_big_sqrt(n):
    return n > 0 and sqrt(n) > 3

for i in range(1,101):
    print(has_big_sqrt(i))