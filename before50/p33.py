d = 1
for x in range(1,10):
	for y in range(1,x):
		q,r = divmod(9*x*y,10*y-x)
		if r==0 and q<=9:
			d *= x/float(y)
			print x,y

print d