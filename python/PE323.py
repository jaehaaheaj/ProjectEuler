def f(n):
	val = 0
	for i in range(n):
		val += (1 - (1/2)**n)**32 - (1 - (1/2)**i)**32
	return val

print(f(10000)) # not sure where the value converges, but this is the answer