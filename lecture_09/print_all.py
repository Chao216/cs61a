def print_all(x):
    print(x)
    return print_all

# it simply print a x, and return it self

print_all(2)(3)(4)(5)(6)

# as it keeps return print_all(). you can keep printing infinitely!

def keep_bark():
    print("精甚细腻")
    return keep_bark

keep_bark()()()