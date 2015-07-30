import string

i = 1
a = ''
while 1:
	a += str(i)
	if len(a)>1000000:
		break
	i += 1

d1 = string.atoi(a[0])
d2 = string.atoi(a[9])
d3 = string.atoi(a[99])
d4 = string.atoi(a[999])
d5 = string.atoi(a[9999])
d6 = string.atoi(a[99999])
d7 = string.atoi(a[999999])

summ = d1 * d2 * d3 * d4 * d5 * d6 * d7

print summ
print d1,d2,d3,d4,d5,d6,d7