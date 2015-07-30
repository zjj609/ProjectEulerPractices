# p38
import string

for n in range(9876,9213,-1):
	p = str(n)+str(n*2)
	if not '123456789'[:].strip(p):
		break
print p


