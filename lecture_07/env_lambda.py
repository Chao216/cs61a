a = 1

def f(g):
    a = 2
    return lambda y: g(y) * a

f(lambda x: a + x)(a)