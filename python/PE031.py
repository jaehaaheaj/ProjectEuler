coinList = [200, 100, 50, 20, 10, 5, 2, 1]
target = 200

def coinRec(i, coinSum):
	if(coinSum == target):
		return 1

	if(len(coinList)<=i):
		return 0
	
	val = 0
	coinNum = 0
	while(coinSum + coinList[i]*coinNum <= target):
		val += coinRec(i+1, coinSum + coinList[i]*coinNum)
		coinNum += 1

	return val



# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p)

print(coinRec(0, 0))