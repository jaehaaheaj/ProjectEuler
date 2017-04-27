#1_2_3_4_5_6_7_8_9_0
#1_2_3_4_5_6_7_8_900
#1_2_3_4_5_6_7_8_9 : 17 digits -> check from sqrt(10**16) to sqrt(2*10**16)
#...9 : ...3**2 or ...7**2

def match_test(n):
	s = str(n)
	return [s[2*i] == str(i+1) for i in range(0, 9)] == [True for i in range(0, 9)]

i = 10**8
#print(i**2)
#print(match_test(11223344556677889))
done = False
while not done:
	for j in [3, 7]:
		if(match_test((i+j)**2)):
			print((i+j)**2 * 100)
			print((i+j)*10)
			done = True
	i+=10

	if(i%10**5 == 0):
		print(i)

# running time : 312.1s