def poly(n):
    """we will return 2 * (n **3)+4*(n**2)+9*n-1
    >>> poly(1)
    14
    >>> poly(2)
    49
    >>> poly(3)
    116
    """
    return 2 * (n ** 3) + 4 * (n ** 2) + 9 * n -1

assert poly(1) == 14
assert poly(2) == 49
assert poly(3) == 116