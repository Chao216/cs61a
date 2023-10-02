list1 = list(map(lambda x: 3*x,[i for i in range(1,11)]))
print(list1)

# the expression above used map, lambda, range together to create a new list

for i in range(1,30):
    print(i,"\tin list1\t",i in list1)