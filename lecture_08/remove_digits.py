def remove(n, digit):
    """remove digits from number n

    >>> remove(123,2)
    >>> 13
    >>> remove(10086,0)
    >>> 186
    >>> remove(1024,0)
    >>> 124
    """
    kept, cycle = 0, 0

    while n > 0:
        n, last = n // 10, n % 10 # quotient, remainder
        if last != digit:
            kept = kept + last * (10**cycle) # becasue of decimal, we use 10**n to carry over
            cycle += 1 # here is the magnitude increase in decimal number
    return kept


print(remove(8008208820,0))
print(remove(4399,3))
