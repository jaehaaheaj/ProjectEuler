val = 0
for i in range(2, 101):
	for j in range(1, 101):
		numString = str(i**j)
		val = max(val, sum([int(x) for x in numString]))

print(val)

