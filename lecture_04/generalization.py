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


