def delay(arg):
    print("delayed!")
    def g():
        return arg
    return g

delay(delay)()(10086)()
print("**********************")
print(delay(delay)()(delay)()(delay)()(delay)()(163)())
# this will evalues to 163 inside print, see printed result

def lag(arg_1):
    print("you got a lag")
    def postpone(arg_2):
        print("postpne once again")
        return arg_1
    return postpone

print(lag(lag)(1)(lag)(2)(lag)(3)(lag)(4)(lag)(5)(6)(7))
# 6 will be printed out, so in the end it evaluates to 6 inside print
print("\n\n\n\n\n")
def f1(arg1):
    print("f1 called")
    def f2(arg2):
        print("f2 called")
        def f3(arg3):
            print("f3 called")
            return arg1
        return f3
    return f2

print(f1(1)(2)(3))

print(f1(f1)(2)(3)(4)(5)(6))

# summary here. depends on how many args is used in function currying
# group them into a unit
# f1 above use 3 args in function currying
# f1(f1)(2)(3) will evalues to f1, as it is returned
# f1(4)(5)(6) evalues to 4, as 4 is returned in second round

print(f1(f1)(2)(3)(f1)(5)(6)(f1)(8)(9)(f1)(11)(12)(13)(14)(15))
# evalues to 13 inside print