'''
lis = {}
n = 1000000000
for i in xrange(2,n):
	print i
	if not i in lis:
		lis[i] = 1
		k = i*2
		while k < n:
			lis[k] = 0
			k += i
			print k
'''
import math

def IsPrime(a):
	if a <= 1:
		return False
	for i in xrange(2,int(math.sqrt(a)) + 1):
		if a % i == 0:
			return False
	return True

for x in xrange(7654321,1234567,-2):
#	print x
	if "" == "1234567"[:].strip(str(x)):
		if IsPrime(x):
			break
print x

