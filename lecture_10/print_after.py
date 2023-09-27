def later_print(n):
    if n < 10:
        print(n)
    else:
        later_print(n//10)
        print(n)

later_print(123456)
print("\n\n\n")
def print_first(n):
    if n < 10:
        print(n)
    else:
        print(n)
        print_first(n//10)

print_first(56789)

def complete(n):
    later_print(n)
    print(n)
    print_first(n)

complete(10086)