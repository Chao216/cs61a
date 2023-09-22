# use decorator based on higher order function

def decorator1(func1):
    print("hello, I am decorator 1")
    def wrapped(num):
        return func1(num)
    return wrapped

@decorator1
def square(n):
    return n * n

square(100)

def decorator2(func2):
    print("decorator2 triggered !")
    print()
    print(func2)
    print()
    def wrappred(number):
        return func2(number)
    return wrappred
    print("hello, I am decorator 2 again")

@decorator2
def plusfive(n):
    return n + 5

plusfive(10)

def whichfunc(a_func):
    print(a_func," is being called!")
    def inner(a):
        return a_func(a)
    return inner

@whichfunc
def f1(a):
    @whichfunc
    def f2(b):
        @whichfunc
        def f3(c):
            @whichfunc
            def f4(d):
                @whichfunc
                def f5(e):
                    return a + b + c + d + e
                return f5
            return f4
        return f3
    return f2

f1(1)(2)(3)(4)(5)