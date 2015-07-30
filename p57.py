def IsAbiggerB(a,b):
	return len(str(a)) > len(str(b))

count = 0
a = 3
b = 2
for i in range(2,1001):
	temp = a 
	a = a+2*b
	b = temp+b
	if IsAbiggerB(a,b):
		count += 1

print count 

