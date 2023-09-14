def delay(arg):
    print("delayed!")
    def g():
        return arg
    return g

delay(delay)()(10086)()
print("**********************")
delay(delay)()(delay)()(delay)()(delay)()(6)()

def lag(arg_1):
    print("you got a lag")
    def postpone(arg_2):
        print("postpne once again")
        return arg_1
    return postpone

print(lag(lag)(1)(lag)(2)(lag)(3)(lag)(4)(lag)(5)(6)(7))