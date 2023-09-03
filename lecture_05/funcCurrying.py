def curry2(func):
    def g(x):
        def h(y):
            return func(x,y)
        return h
    return g

from operator import add
curry_add = curry2(add)
print(curry_add(2)(5))

print("***********************************************\n")
def f1(x):
    def f2(y):
        def f3(z):
            print(x)
            print(y)
            print(z)
        return f3
    return f2
        
f1(1)(2)(3)

def first(n1):
    def second(n2):
        def third(n3):
            def forth(n4):
                def fifth(n5):
                    return 3 * (n1 ** 5) + 4 * (n2 ** 4) + 5 * (n3 ** 3) + 6 * (n4 ** 2) + 7 * (n5 ** 1)
                return fifth
            return forth
        return third
    return second


res = first(1)(2)(3)(4)(5)
print(res)