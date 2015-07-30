
def IsDigit(n):
	temp = n
	summ = 0
	while temp > 0:
		summ += JieChen(temp % 10)
		temp /= 10 
	return summ == n

def JieChen(a):
	return reduce(lambda x,y: x*y, range(1,a+1),1)

for j in range(10,1854721):
	if IsDigit(j):
		print j
