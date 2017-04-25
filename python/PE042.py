def tri(n):
	return int(n*(n+1)/2)

def wordValue(name):
	val = 0
	for i in range(0, len(name)):
		val += ord(name[i]) - ord('A') + 1
	return val

wordsText = open("PE042.txt", "r")
words = wordsText.read().split(",")
words = [i.split("\"")[1] for i in words]

triLimit = max([len(x) for x in words])*26
triList = []
i = 0
while(tri(i)<triLimit):
	triList.append(tri(i))
	i+=1

count = 0
for word in words:
	if(wordValue(word) in triList):
		count+=1
print(count)
