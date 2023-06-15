"""in this section, we will build nested functions"""

def make_adder(n): # this function is in global frame
    def adder(k): #this is nested 
        return k + n
    return adder # as a higher order function, it returns a function

add_ten = make_adder(10)

add_ten(6)
