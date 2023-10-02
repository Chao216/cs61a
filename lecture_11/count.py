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



