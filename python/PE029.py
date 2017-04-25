numList = []
for i in range(2, 101):
	for j in range(2, 101):
		numList.append(i**j)
print(len(set(numList)))
