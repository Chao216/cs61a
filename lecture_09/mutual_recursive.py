def is_even(n):
    if n == 0:
        return True
    else:
        return is_odd(n-1)
    
def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even(n-1)
    
for i in range(1,11):
    print(i, "\t is even? \t",is_even(i))

# above is a demo of mutual recrusive
