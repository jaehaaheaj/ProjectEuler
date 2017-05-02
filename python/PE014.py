seqLen = {}
target = 10**6

def find_length(i):
	if i==1:
		return 1
	next = i//2 if i%2==0 else 3*i+1
	length = 0
	if next in seqLen.keys():
		length = seqLen[next] + 1
	else:
		length = find_length(next) + 1
	seqLen[i] = length
	return length

maxVal = 0
answer = 0	
for i in range(1, target+1):
	temp = find_length(i)
	seqLen[i] = temp
	if maxVal < temp:
		maxVal = temp
		answer = i

print(answer)


