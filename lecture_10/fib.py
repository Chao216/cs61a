def trace(func):
    print(func, " is called!")
    def wrapped(n):
        return func(n)
    return wrapped

@trace
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
for i in range(1,36):
    print(fib(i))

print(fib(10))