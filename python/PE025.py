index = 2
(f1, f2) = (1, 1)
target = 1000
while(len(str(f2))<target):
	(f1, f2) = (f2, f1+f2)
	index+=1

print(index)