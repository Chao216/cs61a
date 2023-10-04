def tree(label,branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

def lable(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) <1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not is_tree(tree)

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
print(count_leaf(tree(1)))
print("\n")
print(fib_tree(10))

print("\n",is_leaf(3))