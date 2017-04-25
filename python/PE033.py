for a in range(1, 10):
	for b in range(1, 10):
		for c in range(1, 10):
			if(10*a*b + b*c == 10*b*c + a*c and b!=c):
				print(b, c)
