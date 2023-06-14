def fib(n):
    """return the nth fibonacci number"""

    pred, curr = 0,1 # first fibonacci number is 0, and second is 1
    k = 1     #think of i as a counter

    while k < n: # we need do n times addition
        pred, curr = curr, pred+ curr #current will be pred, and current will be pred + current
        k += 1 # incrase k by 1
    return curr

fib(100)