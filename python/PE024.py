def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)


def lexi(digit, n):
	orderList = []
	for i in range(digit-1, 0, -1):
		x = 0
		while n >= factorial(i):
			n -= factorial(i)
			x += 1
		orderList.append(x)
	orderList.append(0)
	return orderList

answer = ''
letters = [x for x in range(10)]
order = lexi(len(letters), 1000000-1)
for i in range(0, len(order)):
	answer += str(letters[order[i]])
	del letters[order[i]]

print(answer)