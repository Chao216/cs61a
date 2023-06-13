def square(x):
    ''' This is a practice of docstring in function square
    x is the value input which you want to square
    simply rise to 2nd power
    '''
    return x ** 2



def absolute(x):
    """return the absolute value of input x"""
    if x < 0 :
        return -x
    elif x == 0:
        return 0
    else:
        return x

def aggregate(x):
    """sum until xth natural number"""
    total, i = 0, 1
    if x == 1:
        return 1
    else:    
        while i < x:
            total , i = total + i, i +1
        return total
    

    