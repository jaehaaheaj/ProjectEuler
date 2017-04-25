# combination from PE015

def Combination(a, b):
	x = 1
	for i in range(0, b):
		x *= a-i
	for i in range(1, b+1):
		x /= i
	return x

count = 0
for i in range(1, 101):
	for j in range(0, i+1):
		if(Combination(i, j)>1000000):
			count+=1
print(count)