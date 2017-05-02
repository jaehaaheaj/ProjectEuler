import operator
import functools

target = 10**5

def primes(m):
    """ Returns  a list of primes < n """
    n = m+1
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*int((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

primeSet = primes(target)

def factorize(n):
	factor = {}
	temp = n
	for p in primeSet:
		if(p>n):
			break
		while(temp%p == 0):
			if(p in factor.keys()):
				factor[p] += 1
			else:
				factor[p] = 1
			temp /= p
			if temp == 1:
				return factor

def mass_multiplication(n):
	return functools.reduce(operator.mul, [x for x in n], 1)

def proper_divisor_sum(n):
	if n < 2:
		return -1
	f = factorize(n)
	k = [x for x in f.keys()]
	v = [x for x in f.values()]
	return mass_multiplication([sum([k[j]**i for i in range(v[j]+1)])for j in range(len(k))])-n

div_sum = [proper_divisor_sum(i) for i in range(target)]
print(div_sum[0])

# do not generate primes every time. use pre-made prime set.
