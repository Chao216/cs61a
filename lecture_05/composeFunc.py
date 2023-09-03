def square(n):
    return n * n
def triple(n):
    return n * 3

def compose1(f,g):
    def h(n):
        return f(g(n))
    
    return h

