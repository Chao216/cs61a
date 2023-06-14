def prime_factors(n):
    '''a function that returns prime factors of number n'''
    while n > 1:
        k = get_smallest_prime_factor(n)
        print(k)
        n = n // k

def get_smallest_prime_factor(n):
    k = 2
    while n % k != 0:
        k += 1
    return k

prime_factors(100)