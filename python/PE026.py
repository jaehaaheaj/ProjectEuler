def cycle_length(n):
	i = 1
	while True:
		if (10**i-1) % n == 0:
			return i
		i+=1


cycle_list = [-1 if i%2 == 0 or i%5 == 0 else cycle_length(i) for i in range(1000)]
print(cycle_list.index(max(cycle_list)))
