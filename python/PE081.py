numText = open("PE081.txt", "r")
numList = [[int(x) for x in line.split(',')] for line in numText]

r = len(numList)
c = len(numList[0])
maxNum = sum([sum(x) for x in numList])

for i in range(1, r + c + 1):
	for j in range(i + 1):
		if(i-j < r and j < c):
			up = maxNum+1 if i-j-1<0 else numList[i-j-1][j]
			left = maxNum+1 if j-1<0 else numList[i-j][j-1]
			numList[i-j][j] += min(up, left)
		
print(numList[r-1][c-1])