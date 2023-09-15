from operator import mul, add

def square(n):
    return mul(n,n)

def pirate(arggg):
    print("matty")
    def plunder(arggg):
        return arggg
    return plunder

print(pirate(pirate))
# pirate(pirate) returns the pirate function

print(pirate(pirate(pirate)))
# the expression above also evaluates to the pirate funxtion itself

# print(pirate(pirate(pirate))(5)(7))

# you will see error and traxkbsck below, as pirate(5) will returns 5, integer is not callable!!!

"""
matty
<function pirate.<locals>.plunder at 0x7c7951c540>
matty
matty
<function pirate.<locals>.plunder at 0x7c7951dc60>
matty
matty
Traceback (most recent call last):
  File "/storage/emulated/0/Coding/evals.py", line 18, in <module>
    print(pirate(pirate(pirate))(5)(7))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'int' object is not callable"""


print(pirate(pirate(pirate))(5))


# currying with same arg name

def f1(arrg):
    print("f1 called")
    def f2(arrg):
        print("f2 called")
        def f3(arrg):
            print("f3 called")
            def f4(arrg):
                print("f4 called")
                def f5(arrg):
                    print("f5 called")
                    return arrg
                return f5
            return f4
        return f3
    return f2

f1(1)(2)(3)(4)(5)
print("###########")
f1(1)
print(" will different args name cause error")

def f1(arrg):
    print("f1 called")
    def f2(arrg1):
        print("f2 called")
        def f3(arrg2):
            print("f3 called")
            def f4(arrg3):
                print("f4 called")
                def f5(arrg4):
                    print("f5 called")
                    return 3/arrg4

                return f5
            return f4
        return f3
    return f2

f1(1)
print(f1(1))

# even nested function use different paramenter names, you don't have to give all args


def func1(arg):
    print(arg)
    return arg

func1(123)

print("\n")

def outter(arg1):
    print(arg1)
    def inner(arg2):
        print(arg2)
        return arg2
    return inner

outter(123)(456)

print()

def wrapper(arg):
    print(arg)
    def stuffing(arg):
        print(arg)
        return arg
    return stuffing

wrapper('Tony')

print()

wrapper('Alex')('Ella')


print()

def ring1(arg1):
    print(arg1)
    def ring2(arg2):
        print(arg2)
        return arg2
    return ring2

ring1("Sam Smith")
print()
ring1("May")("June")

# ring1()("Harry")

# again test f1

# f1()(2)(3)()(5)

f1(1)(2)(3)

# ring1("peter")()

# summary 
# in function currying aka nested function
# you don't have to pass in all arguments
# only pass to the level you need

# if you want to call a inside function with arg, then you have to give a argument
# otherwise, you will recive missing arg error

print()

def layer1(arg1):
    print(arg1)
    def layer2():
        print("layer2 is called")
        def layer3(arg2):
            print(arg2)
            return arg2
        return layer3
    return layer2

layer1(123)()(789)
# because layer2() takes no arg, so the expression above works perfectly correct.
