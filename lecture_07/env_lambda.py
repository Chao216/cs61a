a = 1

def f(g):
    a = 2
    return lambda y: g(y) * a

print(f(lambda x: a + x)(a))

print(f(lambda x: x* x)(3))


apple = 5

def outter(a_func):
    apple = 7
    return lambda z: a_func(z) * apple

print(outter(lambda x: x + 100)(3)) # here lambda x : x + 100 is "a_func", 3 is z in return lambda expression, apple is 7