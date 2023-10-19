from unicodedata import lookup

suits = ['heart', 'diamond', 'spade', 'club']

print([lookup("WHITE " + s.upper() + " SUIT") for s in suits])

# be careful with space

# tuples

print(type(())) # it is an empty tuple

print(type((1,2)))

tup1 = ('apple','linux','buick')

print(tup1)

try:
    tup1[0] = 'Samsung' # TypeError: 'tuple' object does not support item assignment
except:
    print("excepion happened")
else:
    print("no exceptions")
finally:
    print("i will be executed anayway")

try:
    10/0
except:
    print("exception")
else:
    print("no exception")
finally:
    print('print from finally')