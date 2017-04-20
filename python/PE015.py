# calculate 20C20

def Combination(a, b):
	x = 1
	for i in range(0, b):
		x *= a-i
	for i in range(1, b+1):
		x /= i
	return x

def GridPath(h, w):
	return int(Combination(h+w, h))

print(GridPath(20, 20))