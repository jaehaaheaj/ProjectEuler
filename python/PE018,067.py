PE018Text = open("PE018.txt", "r")
PE067Text = open("PE067.txt", "r")

numList018 = []
for line in PE018Text:
	line+=" 0"
	line = "0 " + line
	numList018.append(line.split())
numList018 = [[int(j) for j in i] for i in numList018]

numList067 = []
for line in PE067Text:
	line+=" 0"
	line = "0 " + line
	numList067.append(line.split())
numList067 = [[int(j) for j in i] for i in numList067]

print(numList018)

def maxTrianglePath(numList):
	for i in range(0, len(numList)-1):
		for j in range(0, len(numList[i])-1):
			numList[i+1][j+1] += max(numList[i][j], numList[i][j+1])
	return max(numList[len(numList)-1])

print(maxTrianglePath(numList018))
print(maxTrianglePath(numList067))
