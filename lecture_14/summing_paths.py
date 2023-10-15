from tree import *

print_tree(fib_tree(2))

def print_sum(t,sofar):
    sofar = sofar+lable(t)
    if is_leaf(t):
        print(sofar)
    else:
        for b in branches(t):
            print(b,sofar)

lett = tree("H",[
    tree("H",[tree("a"),tree("P",[tree("p",[tree("y")])])])
])

print_tree(lett)
print_sum(lett,' ')