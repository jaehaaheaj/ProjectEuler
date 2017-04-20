n = 2**1000
s = str(n)
answer = 0
for i in range(0,len(s)):
	answer += int(s[i])
print(answer)
