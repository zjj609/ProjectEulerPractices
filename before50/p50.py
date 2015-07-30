
#build prime table
import time

start_time = time.time()

n = 1000000
lis = {}
for i in xrange(2,n):
	if not i in lis:
		lis[i] = 1
		k = 2*i
		while k < n:
			lis[k] = 0
			k += i
lis2 = []

for i in xrange(2,n):
	if lis[i]==1:
		lis2.append(i)

bigger = 0
bigger_count = 0
lenth = len(lis2)

for m in xrange(0,lenth):
	temp = 0
	count = 0
	max_count = 0
	max_num = 0
	for i in xrange(m,lenth):
		temp += lis2[i]
		count += 1
		if temp >= n:
			break
		if lis[temp]==1:
			max_num = temp
			max_count = count
	if max_count > bigger_count:
		bigger_count = max_count
		bigger = max_num
		
print bigger,bigger_count

end_time = time.time()
print end_time - start_time


