def inverse_cascade(n):
    # 1
    # 12
    # 123
    # 12345

    # 123456
    
    # 12345
    # 1234
    # 123
    # 12
    # 1

    if n//10 > 0:
        inverse_cascade(n//10)
        print(n)
    else:
        print(n)

inverse_cascade(8008208820)

def solve_inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f,g,n):
    if n: # n != 0
        f(n)
        g(n)

grow = lambda n: f_then_g(grow,print, n//10)
shrink = lambda n: f_then_g(print,shrink,n//10)

solve_inverse_cascade(8008208820)