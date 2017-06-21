import numpy as np

def f(n) : 
	return sum([(-n)**i for i in range(11)])

answer = 0
for k in range(1, 11):
	x = np.array([[j**i for i in range(k-1, -1, -1)] for j in range(1, k+1)])
	y = np.array([f(i) for i in range(1, k+1)])
	z = np.linalg.solve(x, y)
	xx = np.array([(k+1)**i for i in range(k-1, -1, -1)])
	answer += np.dot(z, xx)

print(answer)

