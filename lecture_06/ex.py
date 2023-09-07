# take a function and return a function

# let us start with take a function

def addone(x):
	return x + 1

def transform(n, term):
	res = term(n)
	return res
ans1 = transform(10,addone)
print(ans1)