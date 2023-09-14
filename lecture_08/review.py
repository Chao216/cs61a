def delay(arg):
    print("delayed!")
    def g():
        return arg
    return g

delay(delay)()(10086)()
print("**********************")
delay(delay)()(delay)()(delay)()(delay)()(6)()
