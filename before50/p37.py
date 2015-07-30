import math    
import string
   
def IsPrime(n):    
	if n <= 1:    
		return False   
	for i in range(2, int(math.sqrt(n)) + 1):    
		if n % i == 0:    
			return False   
	return True   

def IsTrunc(n):
	if not IsPrime(n):
		return False
	a = str(n)
	lenth = len(a)
	for i in range(1,lenth):
		if not IsPrime(string.atoi(a[i:])):
			return False
		if not IsPrime(string.atoi(a[:i])):
			return False
	return True
	
i = 11
count = 0
summ = 0
while(count<11):
	if IsTrunc(i):
		count += 1
		summ += i
		print i
	i += 1

print count 
print summ


