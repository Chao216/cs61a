def addone(n):
    """return value with one added

    >>> addone(1)
    2
    >>> addone(3)
    4
    >>> addone(9)
    10
    """

    return n +1


from doctest import run_docstring_examples as rde

rde(addone,globals(),True)

def cube(n):
    """return cubed value

    >>> cube(1)
    1
    >>> cube(2)
    8
    >>> cube(3)
    27
    """

    return n * n * n

rde(cube,globals(),True)