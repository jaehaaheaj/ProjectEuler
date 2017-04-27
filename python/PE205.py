def dice_value_generator(face, iterNum, diceValue):
	if(iterNum <= 1):
		return [0]+[1 for x in range(face)]
	else:
		temp = dice_value_generator(face, iterNum-1, diceValue)
		diceValue = [0 for x in range(len(temp)+face)]
		for i in range(1, face+1):
			for j in range(len(temp)):
				diceValue[i+j] += temp[j]
		return diceValue

pyramidal = dice_value_generator(4, 9, [])
cubic = dice_value_generator(6, 6, [])

winCount = 0
for i in range(len(pyramidal)):
	for j in range(i):
		winCount+=pyramidal[i]*cubic[j]

print(winCount/(sum(pyramidal)*sum(cubic)))