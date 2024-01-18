r1 = range(10)

t1 = iter(r1)
print(next(t1))
print(next(t1))
print(next(t1))

print("here comes the for loop")
print()
for i in t1:
    print(i)


for i in t1:
    print(i)

bcdedit = ['b', 'c', 'd', 'e', 'd', 'i', 't']

m1= map(lambda x: x.upper(),bcdedit)

next(m1)
next(m1)
next(m1)
print()
print()
l1 = list(m1)

for i in l1:
    print(i)