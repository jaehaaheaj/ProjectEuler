# http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/
# at the link, there are bunch of ways to get list of primes under n
# slight modification for python 3

# this is used in : 007
def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*int((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

print(primes(100))



# 