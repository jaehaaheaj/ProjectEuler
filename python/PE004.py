def IsPalidrome(num):
	if str(num) == str(num)[::-1]:
		return True
	else:
		return False

#print(IsPalidrome(12345))
#print(IsPalidrome(123454321))

limit = 999
ans = 0
for i in range(limit, 100, -1):
	for j in range(limit, i-1, -1):
		if IsPalidrome(i*j) and i*j > ans:
			ans = i * j

print(ans)

