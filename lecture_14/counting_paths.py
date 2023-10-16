from tree import *

print("\n\n\n\n=======================mytree==========================\n\n")
mytree = tree(3,[
    tree(1,[
        tree(5,[tree(6),tree(7)]),
        tree(8,[tree(9),tree(6)])
    ]),
    tree(4,[
        tree(8,[tree(2),tree(5)]),
        tree(1,[tree(2),tree(3)])
    ]),
    tree(1,[
        tree(7,[tree(3),tree(6)]),
        tree(11,[tree(7),tree(3)])
    ])
])

print_tree(mytree)

def count_paths(t,total):
    if lable(t) == total:
        found =1
    else:
        found = 0

    return found + sum([count_paths(b,total) for b in branches(t)])

for i in range(11):
    print("total = ",i,"\tand we have found ",count_paths(mytree,i),"\tpaths")