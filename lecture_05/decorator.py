# Online Python - IDE, Editor, Compiler, Interpreter

def trace(func):
    def target(n):
        print("===>",func,"(",n,")")
        return func(n)
    return target
    
@trace
def square(n):
    return n * n
    
print(square(9))

def track(a_func):
    def wrapped(para1):
        print("Track is working")
        print(a_func," is running")
        return a_func(para1)
    return wrapped
    
@track
def sum_naturals(n):
    total, k = 0,1
    while n >= k:
        total, k = total+k, k+1
    return total

for i in range(1,11):
    print(sum_naturals(i))