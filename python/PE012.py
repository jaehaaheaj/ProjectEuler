import operator
import functools

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*int((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def factorize(n):
	factor = {}
	temp = n
	for p in primes(n):
		while(temp%p == 0):
			if(p in factor.keys()):
				factor[p] += 1
			else:
				factor[p] = 1
			temp /= p
			if temp == 1:
				return factor

def num_divisor(n):
	return functools.reduce(operator.mul, [x+1 for x in factorize(n).values()], 1)

n = 5
while True:
	if(num_divisor(int(n*(n+1)/2)) > 500):
		print(int(n*(n+1)/2))
		break
	n+=1

