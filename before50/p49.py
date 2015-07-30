def IsPrime(a):
	if a<=1:
		return False
	for i in range(2,int(a**0.5)+1):
		if a % i ==0:
			return False
	return True

def IsSameSeq(a,b):
	la = list(a)
	lb = list(b)
	la.sort()
	lb.sort()
	ka = "".join(la)
	kb = "".join(lb)
	if ka == kb:
		return True
	else:
		return False

for n in range(1000,10000):
	if IsPrime(n):
		for i in range(1,(10000-n)/2):
			if IsSameSeq(str(n),str(n+i)):
				if IsSameSeq(str(n),str(n+2*i)):
					if IsPrime(n+i):
						if IsPrime(n+2*i):
							print n,n+i,n+2*i

print IsPrime(5)
print IsSameSeq(str(1009),str(1039))

