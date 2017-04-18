def IsPalidrome(num):
	if str(num) == str(num)[::-1]:
		return True
	else:
		return False

print(IsPalidrome(12345))
print(IsPalidrome(123454321))