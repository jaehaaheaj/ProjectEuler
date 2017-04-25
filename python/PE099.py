# a**b > c**d <=> b log(a) > d log(c)

import math
numText = open("PE099.txt", "r")
maxNum = 0
index = 0
i = 0
for line in numText:
	numList = line.split(',')
	if(maxNum < int(numList[1]) * math.log(int(numList[0]))):
		maxNum = int(numList[1]) * math.log(int(numList[0]))
		index = i 
	i+=1
print(index+1)