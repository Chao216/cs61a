from math import sqrt

# AND

def has_big_sqrt(n):
    return n > 0 and sqrt(n) > 3

for i in range(1,101):
    print(has_big_sqrt(i))

# OR

def by_3_or_by_5(n):
    return n % 3 == 0 or n % 5 == 0

print("*****************************************")

for i in range(1,101):
    print("i = ", i, "\t",by_3_or_by_5(i))


# NOT

print("10 != 100", "\t",10 != 100)

# XOR

# cond 1 must be different from cond 2
# review bitwise operation
a = True
b = False
c = True

print(a ^ b)
print(b ^ c)
print(a ^ c)