

def IsSameCon(a,b):
	al = list(a)
	bl = list(b)
	al.sort()
	bl.sort()
	ak = "".join(al)
	bk = "".join(bl)
	if ak == bk:
		return True
	else:
		return False

def IsSeqNum():
	for i in xrange(1000000,1666666):
		for mul in range(2,7):
			if not IsSameCon(str(i),str(i*mul)):
				break
			if mul == 6:
				return i
	return 0

print IsSeqNum()
