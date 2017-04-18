target = 600851475143
answer = 0
i = 2
while i<=target:
	if i == target:
		answer = i
		break
	elif target%i==0:
		target/=i
		i = 2
	else:
		i+=1
print(answer)