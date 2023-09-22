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