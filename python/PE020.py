mult = 1
for i in range(1, 100+1):
	mult*=i
s = str(mult)

summ = 0
for i in range(0, len(s)):
	summ+=int(s[i])

print(summ)