maxlimit = 10**6
lis = {}
for i in xrange(2,maxlimit+2):
	if not i in lis:
		lis[i] = 1
		k = i*2
		while k < maxlimit+2:
			lis[k] = 0
			k += i

def IsPrimeGenerating(n):
	if n%4 == 0:
		return False
	for i in range(1,int(n**0.5)+1):
		if n%i == 0:
			if lis[i+int(n/i)]==0:
				return False
	return True

summ = 1
for n in xrange(2,maxlimit+1,4):
	print n
	if IsPrimeGenerating(n):
		summ += n

print summ