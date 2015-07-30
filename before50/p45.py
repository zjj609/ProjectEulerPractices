def IsPn(a):
	temp = (24*a+1)**0.5+1
	if temp % 6 == 0:
		return True
	else:
		return False

def IsHn(a):
	temp = (8*a+1)**0.5+1
	if temp % 4 == 0:
		return True
	else:
		return False

def CalTn(a):
	return (a**2+a)/2

i = 286
while 1:
	temp = CalTn(i)
	if IsHn(temp) and IsPn(temp):
		break
	i += 1

print i,temp 