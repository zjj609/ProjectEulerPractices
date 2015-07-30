
def IsPn(a):
	temp = (24*a+1)**0.5+1
	if temp % 6 == 0:
		return True
	else:
		return False

def CalPn(a):
	return a*(3*a-1)/2


k = 2
stop_flag = True
while stop_flag:
	pk = CalPn(k)
	for j in range(1,k):
		pj = CalPn(j)
		if IsPn(pk-pj) and IsPn(pk+pj):
			stop_flag = False
			break;
	k += 1

print k,j
print pk,pj
