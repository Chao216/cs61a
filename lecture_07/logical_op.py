from math import sqrt

# AND

def has_big_sqrt(n):
    return n > 0 and sqrt(n) > 3

for i in range(1,101):
    print(has_big_sqrt(i))

def by_3_or_by_5(n):
    return n % 3 == 0 or n % 5 == 0

print("*****************************************")

for i in range(1,101):
    print("i = ", i, "\t",by_3_or_by_5(i))