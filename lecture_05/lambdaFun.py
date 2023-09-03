square = lambda x : x * x # take argument x, and return x * x

print(square(9))

buy_milk = lambda x,y,p : p - x * y

print(buy_milk(1.2,3,10))

empty = lambda : "this is a test"

print(empty())

# map(function, iterator)
list1 = list(map(lambda x: x * x, [i for i in range(1,101)]))
print(list1)

list2 = list(map(lambda x: x **2 + 3*x -1,[i for i in range(1,101)]))
print(list2)