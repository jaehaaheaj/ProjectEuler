def tri(n):
	return n*(n+1)/2

def penta(n):
	return n*(3*n-1)/2

def hexa(n):
	return n*(2*n-1)

def findTriple(n):
	count = 0
	i = 1; j = 1; k = 1
	while(count<n):
		if(tri(i)==penta(j) and penta(j)==hexa(k)):
			print(int(tri(i)))
			count += 1
			i+=1
		if(tri(i)<penta(j)):
			i+=1
		elif(penta(j)<hexa(k)):
			j+=1
		elif(hexa(k)<tri(i)):
			k+=1
	return 0

findTriple(3)
