# read txt file and get list of numbers - from PE011
numText = open("PE013.txt", "r")
numList = []
for line in numText:
	#numList.append(line.split())
	numList.append(line)
#numList = [[int(j) for j in i] for i in numList]
numList = [int(i) for i in numList]

print(str(sum(numList))[0:10])