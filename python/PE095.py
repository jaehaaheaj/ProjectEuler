target = 10**6

def primes(m):
    """ Returns  a list of primes < n """
    n = m+1
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*int((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

primeSet = primes(target)
factorSet = [[] for i in range(target)]

# factorize
for p in primeSet:
	tmp_p = 1
	while(1):
		tmp_p *= p 
		if(tmp_p >= target):
			break
		tmptmp_p = tmp_p
		while(1):			
			factorSet[tmptmp_p].append(p)
			tmptmp_p += tmp_p
			if(tmptmp_p >= target):
				break

print('done!')

# proper divisor sum
pdsSet = [-1] * target
for i in range(target):
	factorSum = []
	if(len(factorSet[i]) < 1):
		continue
	prev = factorSet[i][0]
	cnt = 0
	for j in range(0, len(factorSet[i])):
		cnt += 1
		cur = factorSet[i][j]
		if(cur!=prev):
			factorSum.append(sum([prev**i for i in range(cnt)]))
			prev = cur
			cnt = 1
		if(j==len(factorSet[i])-1): # last
			factorSum.append(sum([cur**i for i in range(cnt+1)]))
	
	output = 1
	for num in factorSum:
		output *= num
	pdsSet[i] = output - i

print('done!!')

pdsSet[0] = 0
pdsSet[1] = 0

# [Finished in 53.9s] when target = 10**6

# chain
chainSet = [0] * target

maxCnt = 0
bestChain = []

for i in range(2, target):
	l = [i]
	n = i
	while(1):
		if(pdsSet[n] in l):
			if(pdsSet[n] == l[0]):
				for j in range(len(l)):
					chainSet[l[j]] = len(l)
				if(maxCnt < len(l)):
					maxCnt = len(l)
					bestChain = l
				elif(maxCnt == len(l)):
					bestChain += l
			else:
				for j in range(len(l)):
					chainSet[l[j]] = -1
			break
		else:
			n = pdsSet[n]
			if(n > target):
				for j in range(len(l)):
					chainSet[l[j]] = -1
				break
			else:
				l.append(n)
			
print(min(bestChain))