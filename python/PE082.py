array = open("PE082.txt", "r")
numArray = [[int(i) for i in j.split(",") if i != ''] for j in array.read().split("\n")]

updatedArray = []
updatedArray.append([numArray[x][0] for x in range(len(numArray))])

for i in range(len(numArray) - 1):
	col_new = [0 for x in numArray[i + 1]]
	updated_col_1 = updatedArray[i]
	col_1 = [numArray[x][i] for x in range(len(numArray))]
	col_2 = [numArray[x][i + 1] for x in range(len(numArray))]
	for j in range(len(col_2)):
		val = sum(updated_col_1) + sum(col_2)
		for k in range(len(col_1)):
			temp = col_2[j] + updated_col_1[k]
			if(j < k):

				path_a = sum(col_2[j + 1 : k + 1])
				path_b = sum(col_1[j : k])
				temp += min(path_a, path_b)
			else:
				path_a = sum(col_2[k : j])
				path_b = sum(col_1[k + 1 : j + 1])
				temp += min(path_a, path_b)
			val = min(val, temp)
		col_new[j] = val
	updatedArray.append(col_new)

print(min(updatedArray[len(numArray) - 1]))
