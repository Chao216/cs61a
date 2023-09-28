def count_partition(n,m):#here n is the target number, m is max number smaller than n
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partition(n-m, m)
        without_m = count_partition(n, m-1)
        return with_m + without_m
    
print(count_partition(10,3))
print(count_partition(100,13))

# count 10,  3 will be used for sure, then we have 10-3 =7 left
# count 10, without 3,means up to 2

# split [0,3] =====> [0,3) [3] binary seperation