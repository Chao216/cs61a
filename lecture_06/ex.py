# take a function and return a function

# let us start with take a function

def addone(x):
	return x + 1

def square(x):
	return x * x



def transform(n, term):
	res = term(n)
	return res


ans1 = transform(10,addone)
print(ans1)

ans2 = transform(7,square)
print(ans2)

# now return a function

def make_function(n):
	def add_some(x):
		return x + n
	return add_some

add_5 = make_function(5)

ans3 = add_5(10)
print(ans3)

minus_7 = make_function(-7)

ans4 = minus_7(1000)
print(ans4)

# re-cap function currying

def make(a):
	def some(b):
		def more(c):
			def intr(d):
				def ths(e):
					print(a," + ", b, " + ", c, " + ", d, " + ", e)
					return a + b + c + d + e
				return ths
			return intr
		return more
	return some

ans_curry = make(1)(2)(3)(4)(5)
print(ans_curry)