max_num = 0
max_p = 0
for p in range(12,1001):
	temp_num = 0
	for a in range(3,p/3):
		for b in range(a,p/2):
			if (p-a-b)**2==a**2+b**2:
					temp_num += 1
	if temp_num > max_num:
		max_num = temp_num
		max_p = p

print max_p
print max_num
