list1 = [i for i in range(1,11)]

print(sum(list1))

print(sum([2,3,4],5))

print(sum([[1,2,3],[4,5,6]],[]))

print(max(list1))
print(max(1,2,3,2,1,4,66))

# use key= function

print(max(range(5,11),key=lambda x:-x)) # find which one return biggest value

# all

print(all(range(10)))

print(all(range(1,10)))
print(all(range(-10,10)))

print(all(list1))