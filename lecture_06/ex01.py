def bark():
	print("精甚细腻，精细的工笔画")

def gdp():
	print("人均生产总值接近八千万")

def chairman(f,g):
	def collection():
		f()
		g()
	return collection

a_func = chairman(bark,gdp)

a_func()