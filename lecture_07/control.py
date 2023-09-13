from math import sqrt

def real_sqrt(n):
    if n > 0:
        return sqrt(n)
    else:
        return 0
    
print(real_sqrt(16))
print(real_sqrt(-9))

def if_(cond,t,f):
    if cond:
        return t
    else:
        return f
    
def eigen_sqrt(n):
    if_(n > 0, sqrt(n), 0)

print(eigen_sqrt(100))
print(eigen_sqrt(-21))

# you wiill receive error because in call function, all arguments will be evaluated including sqrt(n) when n is negative, error happens