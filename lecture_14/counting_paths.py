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
    tree(1)
])

print_tree(mytree)