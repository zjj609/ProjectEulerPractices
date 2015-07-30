def IsPrime(a):
	for i in range(2,int(a**0.5)+1):
		if a % i == 0:
			return False
	return True

endnum = 49
lines = 7

primenum = 8
anglenum = 13

while (primenum+0.0)/anglenum > 0.1:
	for i in range(1,5):
		endnum += (lines+1)
		if IsPrime(endnum):
			primenum += 1
	anglenum += 4
	lines += 2
#	print lines,primenum,anglenum,(primenum+0.0)/anglenum

print lines
