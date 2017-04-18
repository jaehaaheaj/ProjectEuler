def SumSquare(n):
	sum = 0
	for i in range(1,n+1):
		sum += i
	return sum**2

def SquareSum(n):
	sum = 0
	for i in range(1,n+1):
		sum += i**2
	return sum

n = 100
print(SumSquare(n) - SquareSum(n))