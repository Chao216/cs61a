dic1 = {"chao":26,"jiaxing":26,"yulei":27}

print(dic1)

# remember to iterate through, don't foregt ()
for i in dic1.items():
    print(i)

for i in dic1.keys():
    print(i)

for i in dic1.values():
    print(i)

for i, j in zip(dic1.keys(),dic1.values()):
    print(i, " = ", j)

l1 = ['chao','lei','jiaxing']
l2 = ['coffee','coke','tea']

for i,j in zip(l1,l2):
    print(i," enjoys drink ", j)

list2 = {1:["apple","grape"]}
print(list2[1][0])