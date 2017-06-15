year = 1900
month_day = [31, [28, 29], 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

count = 0
total_days = 1
while(year <= 2000):
	isLeapYear = year%4 == 0 and (year%100 != 0 or year%400 == 0)
	for i in range(len(month_day)):

		if(year>1900 and total_days%7 == 0):
			count += 1
		
		day = month_day[i]
		if(i == 1):
			if(isLeapYear):
				day = day[1]
			else:
				day = day[0]

		total_days += day		
	year += 1

print(count)


