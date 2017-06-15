def Combination(a, b):
	x = 1
	for i in range(0, b):
		x *= a-i
	for i in range(1, b+1):
		x /= i
	return x

def Homogeneous(a, b):
	return Combination(a+b-1, b)

answer = 0
for i in range(1, 8):
	answer += Combination(7, i) * Homogeneous(i, 20-i) * i # this counts (20, 0, ..., 0). fail!
answer /= Combination(70, 20)

print(answer)