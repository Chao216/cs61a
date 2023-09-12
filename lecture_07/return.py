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

# a_func(x) == z outcome is either true or false
# search function will loop x +1 until true is satisified
# z ===>  x, x will increase until conditiion is meet

reverse_cube = inverse(cube)
print(reverse_cube(27))
print(reverse_cube(8))

def reverse(origin_func): # a function to reverse
    def mirror_func(num): # the wanted function, take a num arg
        return search((lambda c : origin_func(c)==num)) # return c
        ##########################################################
        # suppose origin func is square
        # search(lambda c : square(c)== num )
        # c starts from 0
        # if square(c) != num, we get false
        # loop in search continue
        # try square(1)... square(2)...square(3)......
        # until find correct c, and get c returned

    return mirror_func
    # as high order function, the mirror function is then returned


## thin of origin_func(x) == z
## now we need mirror_func(z) == x
def plusfive(n):
    return n + 5

revPlusFive = reverse(plusfive)
print(revPlusFive(100))

def mulnine(n):
    return n * 9

test = reverse(mulnine)
print(test(63))