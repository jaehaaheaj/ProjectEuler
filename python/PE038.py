def ToDigits(n):
	output = []
	while(n!=0):
		output.append(n%10)
		n = n//10
	return output

def pandigitalMultiple(n):
	output = []
	i = 1
	while(True):
		numList = [i * x for x in range(1, n+1)]
		if(IsLengthTooLong(numList)):
			break
		if(pandigitalChecker(numList)):
			string = ''
			for num in numList:
				string += str(num)
			output.append(string)
		i+=1

	return output

def pandigitalChecker(numList):
	checkList = []
	for num in numList:
		checkList += ToDigits(num)
	checkList.sort()
	return [x for x in range(1, 10)] == checkList

def IsLengthTooLong(numList):
	output = False
	if(sum([len(str(x)) for x in numList])>9):
		output = True
	return output

# for n more than 9, no need to try since k in (k, (1, ..., 9)) can't be bigger than 1.

answerList = []
for i in range(2, 10):
	for answer in pandigitalMultiple(i):
		answerList.append(answer)
answerList.sort(reverse = True)
print(answerList[0])