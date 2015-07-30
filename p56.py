import string 

def SumDigitNum(a):
	strin = str(a)
	lenth = len(strin)
	summ = 0
	for i in range(0,lenth):
		summ += string.atoi(strin[i]) 
	return summ

max_sum = 0

for i in range(1,100):
	for j in range(1,100):
		temp_sum = SumDigitNum(i**j)
		if temp_sum > max_sum:
			max_sum = temp_sum

print max_sum