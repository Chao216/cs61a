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

tee = 10

def outter(a_func):
    tee = 9
    def inner(a_number):
        return a_func(a_number) * tee
    return inner

def cube(n):
    return n * n * n

print(outter(cube)(3))

assert outter(cube)(3) == 243

print("first assertion passed!")

# recap , what does print(return)? None

print(693)
print(print(693))
print(print(print(693)))

# print() will always return None
print(print()) # print() will change line

allen = None
betty = None
print((allen == betty))