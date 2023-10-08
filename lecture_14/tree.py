def tree(label,branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

def lable(tree_x):
    return tree_x[0]

def branches(tree_x):
    return tree_x[1:]

def is_tree(tree_x):
    if type(tree_x) != list or len(tree_x) <1:
        return False
    for branch in branches(tree_x):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree_x):
    return not branches(tree_x)

print(not True)
print(not 1)
print(not 0)

def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        return tree(lable(left)+lable(right),[left,right])
    
for i in range(6):
    print(fib_tree(i))

def count_leaf(t):
    # simplest case, is a leaf
    if is_leaf(t):
        return 1
    else:
        return sum([count_leaf(b) for b in branches(t)])
print("\n")    
print(count_leaf(tree(1,[tree(2),tree(3)])))
print("\n")
print(fib_tree(10))


print(tree(1,[tree(2),tree(3)]))

print([i**2 for i in range(9)])

for i in range(11):
    print(i,'th fibonacci tree')
    print(count_leaf(fib_tree(i)))

def incremenT_leaves(tree_x):
    if is_leaf(tree_x):
        return tree(lable(tree_x)+1)
    else:
        bs=[incremenT_leaves(b) for b in branches(tree_x)]
        return tree(lable(tree_x),bs)
    

print(incremenT_leaves(tree(12)))
print(incremenT_leaves(
    tree(1,[
        tree(2,[tree(3),tree(4)]),
        tree(5,[tree(6),tree(7)])
    ])
))