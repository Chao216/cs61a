""" REMEMBER Don't Repeat and generalize the function"""

from math import pi, sqrt

def area(x,shape_constant):
    assert x > 0, "X must be a positive number" #some message to give if input is negative 
    return x ** 2*shape_constant

def circle(x):
    return area(x, pi)

def square(x):
    return area(x,1)

def hexgon(x):
    return area(x, 3*sqrt(3)/2)

def sum_naturals(n):
    """sum up to the nth natural number"""

    total, k = 0, 1

    while k <= n:
        total, k = total + k, k +1

    return total

def identity(x):
    return x

def cube(x):
    return pow(x,3)

from operator import mul

def pi_term(x):
    return 8/ mul(4*x-3,4*x-1)

def summation(n,term):

    total,k = 0,1

    while k <= n:
        total, k = total + term(k), k+1

    return total

