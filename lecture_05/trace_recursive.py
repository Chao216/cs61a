def trace(func):
    def wrapped(n):
        print("===>",func,"(",n,")")
        return func(n)
    return wrapped

@trace
def sum_digits(n):
    if n < 10:
        return n
    else:
        quotient, remainder = n//10,n%10
        print("remainder:",remainder)
        return sum_digits(quotient)+remainder
        
print(sum_digits(8008208820))




def trace(func):
    def wrapped(n):
        print("===>",func,"(",n,")")
        return func(n)
    return wrapped

@trace
def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return factorial(n-1)*n
        
for i in range(0,11):
    print(factorial(i))


# when two functions recurisvely call each other, we call it mutually recursive

def trace(func):
    def wrapped(n):
        print("===>",func,"(",n,")")
        return func(n)
    return wrapped

@trace
def is_even(n):
    if n == 0:
        return True
    else:
        return is_odd(n-1)

@trace
def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even(n-1)

for i in range(0,11):
    print("**********************")
    print(is_even(i))


#******************************************************************************************

def trace(func):
    def wrapped(n):
        print("===>",func,"(",n,")")
        return func(n)
    return wrapped

@trace
def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n - 7)
        print(n)
cascade(100)