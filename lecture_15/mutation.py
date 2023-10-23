a = [10]
b = a
print(a==b)

b.append(30)

print(a)

print(b==a)

c = [10]
d = [10]

print(c==d)

print(c is d)

print( a is b)

# identity
# exp0 is exp1
# if both exp0 and exp1 evaluate to the same object

# equality
# exp0 == exp1
# if both exp0 exp1 evaluates to the same value

# identity ---> Same object
# equality ---> same value

tim = 26
larry = tim

print(larry is tim)
print(larry == tim)

myname = 'chao'
yourname = 'chao'
print(myname == yourname)
print(myname is yourname)

myage = 26
yourage = 26

print(myage == yourage)
print(myage is yourage)

# default mutable argument is dangerous

def f(s=[]):
    s.append(5)
    print(len(s))

# review of default args

def print_fullname(first='Tony',last='lau'):
    print('hello ',first,' ',last,' , how are you?')
    