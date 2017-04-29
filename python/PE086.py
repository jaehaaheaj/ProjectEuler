# for given a, b, c under condition a<b<c, it is trivial that min((a+b)**2+c**2, (b+c)**2+a**2, (c+a)**2+b**2) == (a+b)**2+c**2
import math
def is_shortest_route_integer(a, b, c):
	route = math.sqrt((a+b)**2+c**2)
	return route == math.floor(route)

M = 0
count = 0

while count <= 10**6:
	M += 1
	for a in range(1, M+1):
		for b in range(a, M+1):
			if is_shortest_route_integer(a, b, M):
				count+=1
	if M%100 == 0:
		print(M, count)

print(M)
