onemillion = 1000000
ply = [1]
summ = 1
for i in range(1,101):
	summ *= i
	ply.append(summ)

count = 0
for n in range(10,101):
	for r in range(n,1,-1):
		if ply[n]/(ply[r]*ply[n-r]) > onemillion:
			count += 1

print ply[23]/(ply[10]*ply[13]) > onemillion
print count



