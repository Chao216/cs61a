str1 = "Кириллица"
print([*str1])

list1 = [*str1]

list2 = [list1[i] for i in [2,4,6,8]]

print(list2)

# you can use [*str] to convert a string to a list of chars

term = [1,2,3,4,5,6]
term2 = [i-10 for i in term]
print(term)
print(term2)
term3 = [i+1 for i in term if i %2 == 0]
print(term3)