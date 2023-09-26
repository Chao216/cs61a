def sum_digits_iter(n):
        if n < 10:
            return n
        else:
            sum = 0
            while n > 0:
                 quotient,remainder = n//10, n%10
                 n,sum = quotient, sum+remainder

            return sum

print(sum_digits_iter(123))
print(sum_digits_iter(456))

