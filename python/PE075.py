def singular_right_triangle_finder(perimeter):
	output = 0
	for i in range(1, perimeter//3 + 1):
		for j in range(i, perimeter):
			if(perimeter - i - j < j):
				break
			if(i**2 + j**2 == (perimeter - i - j)**2):
				output += 1
				if output > 1:
					return False
				break
	return output==1

answer = 0
for i in range(1, 150):
	if singular_right_triangle_finder(i):
		answer+=1

print(answer)

