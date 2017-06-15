points = open("PE102.txt", "r")
triangles = [[int(i) for i in j.split(",") if i != ''] for j in points.read().split("\n")]

def oriChecker(pA, pB, pC):
	dx = pA[0] - pB[0]
	dy = pA[1] - pB[1]
	if(dx != 0):
		a = dy / dx
		b1 = pA[1] - pA[0]*a
		b2 = pC[1] - pC[0]*a
	else:
		b1 = pA[0]
		b2 = pC[0]
	return b1*b2<0

def oriContainingTri(triangle):
	pA = [triangle[0], triangle[1]]
	pB = [triangle[2], triangle[3]]
	pC = [triangle[4], triangle[5]]
	if(oriChecker(pA, pB, pC) and oriChecker(pB, pC, pA) and oriChecker(pC, pA, pB)):
		return True
	else:
		return False

print(triangles[0])
print(oriContainingTri(triangles[0]))

count = 0
for triangle in triangles:
	if oriContainingTri(triangle):
		count += 1

print(count)


