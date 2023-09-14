def f(x):
    return g(x-10)

def g(y):
    # return abs(h(y+1)) - h(y /* 1)
    # /* will give syntax error
    return abs(h(y+1)) - h(1 / y)

def h(z):
   # z * z
   # if no return, Nonetype error
    return z * z

print(f(13))
# print(f(10))
# cause divide by zero error

