def IsPalindrome(num):
	return str(num) == str(num)[::-1]

def consecutive_square_sum(start_num, consecutive):
	return sum([i**2 for i in range(start_num, start_num+consecutive)])

target = 10**8

start_num = 1
consecutive = 2
answer = []

while True:
	temp = consecutive_square_sum(start_num, consecutive)
	if temp > target:
		if start_num == 1:
			break
		consecutive += 1
		start_num = 0
	elif IsPalindrome(temp):
		print(temp, start_num, consecutive)
		answer.append(temp)
	start_num += 1

print(sum(set(answer)))