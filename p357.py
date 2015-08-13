import time
time1 = time.clock()

maxlimit =  10**8

size = (maxlimit - 3) / 2
a = [False] * size
b = [False] * maxlimit
s = 0
primes = []
while s < size:
    t = 2 * s
    p = t + 3
    primes.append(p)
    b[p] = True
    for n in range(t * (s + 3) + 3, size, p):
        a[n] = True
    s = s + 1
    while s < size and a[s]:
        s = s + 1

def IsPrime(a):
	if a == 1:
		return False
	if a == 2:
		return True
	for i in xrange(2,int(a**0.5)+1):
		if a%i == 0:
			return False
	return True

def IsPrimeGenerating(n):
	if n%4 == 0:
		return False
	for i in range(1,int(n**0.5)+1):
		if n%i == 0:
			if not b[i+n/i]:
				return False
	return True

time2 = time.clock()
print time2-time1

summ = 1

for pn in primes:
	temp = pn - 1
	if IsPrimeGenerating(temp):
		summ += temp 

print summ
time3 = time.clock()
print time3-time1