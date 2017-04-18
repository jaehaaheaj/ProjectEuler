endCondition = False
for i in range(1, 1000):
	for j in range(1, i):
		k = 1000 - i - j
		if k > 0 and i**2 + j**2 == k**2:
			print(i*j*k)
			endCondition = True
			break
	if endCondition:
		break
