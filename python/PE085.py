# Combination from PE015
def Combination(a, b):
	x = 1
	for i in range(0, b):
		x *= a-i
	for i in range(1, b+1):
		x /= i
	return int(x)

def RectangleCount(a, b):
	return Combination(a+1, 2) * Combination(b+1, 2)

# find minimum length of longer edge
longlimit = 1
while RectangleCount(longlimit, longlimit)<2000000:
	longlimit+=1
print(longlimit)

# loop
delta = 2000000
area = 0
for i in range(1, longlimit+1):
	j = i
	while RectangleCount(i, j)<2000000:
		j+=1
		deltaNew = abs(2000000 - RectangleCount(i, j))
		if deltaNew < delta:
			delta = deltaNew
			area = i*j

print(area)

