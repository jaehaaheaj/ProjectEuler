def CubicToSortedString(n):
	output = [s for s in str(n**3)]
	output.sort()
	return ''.join(output)

permutationCount = {}
i = 0
while True:
	string = CubicToSortedString(i)
	if(string not in permutationCount.keys()):
		permutationCount[string] = []
		permutationCount[string].append(i)
	else:
		permutationCount[string].append(i)
		if(len(permutationCount[string]) == 5):
			print(permutationCount[string][0]**3)
			break
	i+=1


