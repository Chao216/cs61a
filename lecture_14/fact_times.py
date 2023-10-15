def fact_times(n,k):
    if n == 0:
        return k
    else:
        return fact_times(n-1,k*n)

def fact(n):
    return fact_times(n,1)

for i in range(11):
    print(fact(i))