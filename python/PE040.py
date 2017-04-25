string = ''
i = 1
while(len(string)<1000000):
	string+=str(i)
	i+=1

val = 1
for i in range(0, 7):
	val *= int(string[10**i - 1])
print(val)
