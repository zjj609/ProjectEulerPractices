import time

start_time = time.time()

def IsPrime(a):
	for i in range(2,int(a**0.5)+1):
		if a % i == 0:
			return False
	return True

lis = {2:1,3:1,5:1,7:1}

n = 9
while True:
	if IsPrime(n):
		lis[n] = 1
	elif n%2 == 1:
		i = 1
		flag = 0
		while (n-2*i*i)>1:
			if n-2*i*i in lis:
				flag = 1
			i += 1
		if flag == 0:
			break
		else:
			flag = 0
	n += 1

end_time = time.time()

print n
print end_time - start_time
