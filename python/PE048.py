val = 0
for i in range(1, 1001):
	val += i**i%10**10
print(val%10**10)