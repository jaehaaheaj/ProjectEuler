def nameValue(name):
	val = 0
	for i in range(0, len(name)):
		val += ord(name[i]) - ord('A') + 1
	return val


namesText = open("PE022.txt", "r")
names = namesText.read().split(",")
names = [i.split("\"")[1] for i in names]
names.sort()

scores = [nameValue(names[i])*(i+1) for i in range(0, len(names))]
print(sum(scores))