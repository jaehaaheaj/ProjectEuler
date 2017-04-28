def right_triangle_finder(perimeter):
	output = 0
	for i in range(1, perimeter//3 + 1):
		for j in range(i, perimeter):
			if(perimeter - i - j < j):
				break
			if(i**2 + j**2 == (perimeter - i - j)**2):
				output += 1
				break
	print(perimeter)
	return output

count = [right_triangle_finder(i) for i in range(0, 1001)]
print(count.index(max(count)))

