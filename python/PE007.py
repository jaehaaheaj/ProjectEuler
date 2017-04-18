# using Primes
def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*int((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

#print(len(primes(100))) # 25
#print(len(primes(10000))) # 1229
#print(len(primes(1000000))) # 78498

target = 10001
print(primes(1000000)[target-1])