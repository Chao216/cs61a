# return will exit the code block
def demo():
    print("sentence before return")
    return None
    print("senetnce after return")

demo()

def search(a_func):
    x = 0
    while not a_func(x): # when a_func(x) is not true
        x += 1
    # will liip until condition is true
    return x

def bigger_than_ten(x):
    return x > 10 # here true or false will be returned

print(search(bigger_than_ten))

def cube(x):
    return x * x * x

def inverse(a_func): # pass in a function to be used later
    # we are looking for a function that do reverse job
    return lambda z: search(lambda x :a_func(x) == z)

reverse_cube = inverse(cube)
print(reverse_cube(27))
print(reverse_cube(8))
