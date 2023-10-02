def count(a_list,digit):
    total = 0
    k = 0
    while k < len(a_list) -1:
        if a_list[k] == digit:
            total += 1
        k += 1
    print("we found ", total, " ",digit, " in the list")
    return total

count([1,1,1,2,2,2,3,1,1,1,1,1,3,2,1,2,3,2,1],1)



def new_count(list_,n):
    count = 0
    for i in list_:
        if i == n:
            count += 1
    print("we found ", count, " ",n, " in the list")
    return count
new_count([2,3,2,3,2,3,4,3,2,3,5,4,6,43,2],3)