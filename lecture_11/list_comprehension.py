str1 = "Кириллица"
print([*str1])

list1 = [*str1]

list2 = [list1[i] for i in [2,4,6,8]]

print(list2)