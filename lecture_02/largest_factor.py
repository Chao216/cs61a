def largest_factor(n):
    if n == 1:
        return 1
    else:
        factor = n -1
        while factor > 0:
            if n % factor == 0:
                return factor
            factor -= 1

ans = largest_factor(1992)
print(ans)