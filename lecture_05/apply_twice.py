def apply_twice(f,n):# here f is a function, whil n is a number
    return f(f(n))

def square(n):
    return n * n

print(apply_twice(square,10)) 