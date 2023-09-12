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
