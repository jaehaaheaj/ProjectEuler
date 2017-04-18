def maxHorizontal(numList, n):
	maxmult = 0
	for i in range(0, len(numList)):
		for j in range(0, len(numList[i]) - n):
			temp = 1
			for x in range(0, n):
				temp *= numList[i][j+x]
			if temp > maxmult:
				maxmult = temp
	return maxmult

def maxVertical(numList, n):
	maxmult = 0
	for i in range(0, len(numList) - n):
		for j in range(0, len(numList[i])):
			temp = 1
			for x in range(0, n):
				temp *= numList[i+x][j]
			if temp > maxmult:
				maxmult = temp
	return maxmult

def maxBackSlash(numList, n):
	maxmult = 0
	for i in range(0, len(numList) - n):
		for j in range(0, len(numList[i]) - n):
			temp = 1
			for x in range(0, n):
				temp *= numList[i+x][j+x]
			if temp > maxmult:
				maxmult = temp
	return maxmult

def maxSlash(numList, n):
	maxmult = 0
	for i in range(0, len(numList) - n):
		for j in range(0, len(numList[i]) - n):
			temp = 1
			for x in range(0, n):
				temp *= numList[i+n-x][j+x]
			if temp > maxmult:
				maxmult = temp
	return maxmult

numText = open("PE011.txt", "r")
numList = []
for line in numText:
	numList.append(line.split())
numList = [[int(j) for j in i] for i in numList]
print(max(maxHorizontal(numList, 4), maxVertical(numList, 4), maxBackSlash(numList, 4), maxSlash(numList, 4)))