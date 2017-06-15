types = [0 for i in range(1000001)]

thickness = 1
while(thickness < 500):
	i = 1
	while((i + 2 * thickness)**2 - i**2 < 1000**2):
		types[(i + 2 * thickness)**2 - i**2] += 1
		i += 1
	thickness += 1

print("created types array")

answer = 0
for i in range(len(types)):
	if(1<=types[i] and types[i]<=10):
		answer += 1

	if(i%50000==0):
		print(i/10**6)

print(answer)
