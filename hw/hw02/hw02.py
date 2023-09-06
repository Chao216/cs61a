from operator import add, mul

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1


HW_SOURCE_FILE = __file__


def product(n, term):
    
    "*** YOUR CODE HERE ***"
    total, k = term(1), 1
    while k < n:
        total,k = total * term(k+1),k+1
    # print("print first question")
    return total


def accumulate(merger, start, n, term):

    "*** YOUR CODE HERE ***"
    total,k=start,1
    while (k <= n) and n>0:
        total, k = merger(total,term(k)),k+1
    return total


def summation_using_accumulate(n, term):
   
    "*** YOUR CODE HERE ***"
    total,k=term(0),1
    while k <= n:
        total,k = total+term(k),k+1
    return total


def product_using_accumulate(n, term):
   
    "*** YOUR CODE HERE ***"
    total,k= term(1),1
    while k < n:
        total,k = total*(term(k+1)),k+1
    return total
