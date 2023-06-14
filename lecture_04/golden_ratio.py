""" in this section, we will meet higher order functions"""

def improve(update, close, guess=1): # we passed a update function, nd close function, and guess with default value of 1
    while not close(guess):# if close function doesn't return True
        guess = update(guess) # then we update guess with the update function
    return guess # and we will return the refined guess until while loop finish.

def golden_update(guess):
    return 1/guess + 1 # repeate this process later

def square_close_to_plusone(guess):
    return approx_eq(guess*guess, guess+1) # we will evaluate guess* guess and guess +1 with abstract function

def approx_eq(a,b, tolerence= 1e-15):# we will pass in 2 inputs, a, and b, and compare with tolerence
    return abs(a-b) < tolerence # if difference is small enough, return true.

improve(golden_update, square_close_to_plusone, 21)