dec2bin = lambda n: bin(n)[2:]

def is_palind(a):
	a = str(a)
	return a == a[::-1]

summ = 0
for i in xrange(1,10**6,2):
	if is_palind(i) and is_palind(dec2bin(i)):
		print i
		summ += i
print summ