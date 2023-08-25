def summation(n,term):
	total,k = 0,1
	while k <= n:
		total,k = total + term(k), k+1
	return total

def cube(x):
	return x * x * x

def sum_cube(n):
	return summation(n,cube)

for x in range(1,101):
	print(sum_cube(x))