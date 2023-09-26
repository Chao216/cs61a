def sum_digits(n):
    if n < 10:
        return n
    else:
        return sum_digits(n//10) + n % 10

def luhn_sum(n):
    if n < 10:
        return n
    else:
        return luhn_sum_double(n//10) + n%10
    
def luhn_sum_double(n):
    quotient,remainder = n//10, n%10
    luhn_digit = sum_digits(2*remainder)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(quotient) + remainder


print(luhn_sum(12345))
print(luhn_sum(2))
print(luhn_sum(32))
print(luhn_sum(5105105105105100))
print(luhn_sum(8530))