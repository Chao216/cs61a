a = 1

def f(g):
    a = 2
    return lambda y: g(y) * a # here a is 2

print(f(lambda x: a + x)(a))# first a in lambda is global (1) ==> lambda x : 1 + x, second a also global , we get (1 + 1) * 2 == 4

print(f(lambda x: x* x)(3)) # (3 * 3) * 2 == 18.


apple = 5

def outter(a_func):
    apple = 7
    return lambda z: a_func(z) * apple # here the apple is a local variable inside code block

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