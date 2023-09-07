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