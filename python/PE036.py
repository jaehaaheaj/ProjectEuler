def IsPalindrome(num):
	return str(num) == str(num)[::-1]

def IsBinaryPalindrome(num):
	return IsPalindrome(str(bin(num))[2:])

val = 0
for i in range(0, 1000000+1):
	if(IsPalindrome(i) and IsBinaryPalindrome(i)):
		val += i
print(val)