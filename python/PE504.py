# given quadrilateral can be divided into 4 triangle pieces, using x and y axis to split the area.
# (number of lattice points that the triangles are strictly containing) + (number of lattice points on the x, y axis) - (doubly counted origin)

import math

def numberOfLatticePointsInTriangle(a, b):
	num = 0
	for i in range(1, b):
		num += i*a // b
		if((i*a)%b==0):
			num-=1
	return num

'''
def numberOfLatticePointsInQuad(a, b, c, d):
	num = numberOfLatticePointsInTriangle(a, b) + numberOfLatticePointsInTriangle(b, c) + numberOfLatticePointsInTriangle(c, d) + numberOfLatticePointsInTriangle(d, a)
	num += (a + c - 1) + (b + d - 1)
	num -= 1
	return num
'''

size = 4
triangleCountArray = [[numberOfLatticePointsInTriangle(i, j) for i in range(1, size + 1)] for j in range(1, size + 1)]

print("done")

def numberOfLatticePointsInQuad(a, b, c, d):
	num = triangleCountArray[a-1][b-1] + triangleCountArray[b-1][c-1] + triangleCountArray[c-1][d-1] + triangleCountArray[d-1][a-1]
	num += (a + c - 1) + (b + d - 1)
	num -= 1
	return num

def isSquare(num):
	if(num < 1):
		return False
	return pow(num, 0.5) == math.floor(pow(num, 0.5))

count = 0

for a in range(1, size+1):
	for b in range(1, size+1):
		for c in range(1, size+1):
			for d in range(1, size+1):
				if(isSquare(numberOfLatticePointsInQuad(a, b, c, d))):
					count+=1

print(count)
print("this will take about", 10*pow(10/3, 4)/60, "minutes with my machine")
