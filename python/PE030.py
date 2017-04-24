def fifthCheck(n):
	dpsum = 0
	for i in range(0, len(str(n))):
		dpsum += int(str(n)[i])**5
	return dpsum==n


val = 0
for i in range(10, 10**6):
	if(fifthCheck(i)):
		print(i)
		val+=i
print(val)