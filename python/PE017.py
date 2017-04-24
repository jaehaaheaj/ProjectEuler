def numberCost(n):
	if(n==1000):
		return len('one'+'thousand')
	elif(n<1000 and n>0):
		a = n//100
		b = (n%100)//10
		c = n%10
		number = ''
		if(a!=0):
			number += num2string1(a)+'hundred'
			if(not(b==0 and c==0)):
				number += 'and'
		if(b==1):
			number += num2string2(c)
		else:
			number += num2string3(b)+num2string1(c)
		return len(number)
	else:
		return 0

def num2string1(n):
	if(n==1):
		return 'one'
	elif(n==2):
		return 'two'
	elif(n==3):
		return 'three'
	elif(n==4):
		return 'four'
	elif(n==5):
		return 'five'
	elif(n==6):
		return 'six'
	elif(n==7):
		return 'seven'
	elif(n==8):
		return 'eight'
	elif(n==9):
		return 'nine'
	else:
		return ''

def num2string2(n):
	if(n==0):
		return 'ten'
	elif(n==1):
		return 'eleven'
	elif(n==2):
		return 'twelve'
	elif(n==3):
		return 'thirteen'
	elif(n==4):
		return 'fourteen'
	elif(n==5):
		return 'fifteen'
	elif(n==6):
		return 'sixteen'
	elif(n==7):
		return 'seventeen'
	elif(n==8):
		return 'eighteen'
	elif(n==9):
		return 'nineteen'
	else:
		return ''

def num2string3(n):
	if(n==2):
		return 'twenty'
	elif(n==3):
		return 'thirty'
	elif(n==4):
		return 'forty'
	elif(n==5):
		return 'fifty'
	elif(n==6):
		return 'sixty'
	elif(n==7):
		return 'seventy'
	elif(n==8):
		return 'eighty'
	elif(n==9):
		return 'ninety'
	else:
		return ''

# test cases
print(numberCost(342))
print(numberCost(115))
print(numberCost(1001))
print(numberCost(300))

# main loop
answer = 0
for i in range(1, 1001):
	answer += numberCost(i)
print(answer)
