target = 10**7
chainEnd = [0 for i in range(target+1)]

def chain_end_finder(i):
	if i<1:
		return 0
	elif i == 1 or i == 89:
		chainEnd[i] = i
		return i
	next = sum([int(n)**2 for n in str(i)])
	val = 0
	#if next in chainEnd.keys():
	if chainEnd[next] != 0:
		val = chainEnd[next]
	else:
		val = chain_end_finder(next)
	chainEnd[i] = val
	return val

answer = 0
for i in range(target+1):
	if chain_end_finder(i) == 89:
		answer += 1
	if i%10**4 == 0:
		print(i)
print(answer)