
lis = {}
n = 1
temp = 1
while temp < 500:
	lis[temp] = 1
	n += 1
	temp = n*(n+1)/2

f = open('p042_words.txt')
summ = 0
start = 0
count = 0
char = f.read(1)
while char:
	if char == '"' and start == 0:
		start = 1		
	if char >= 'A' and char <= 'Z':
		summ += (ord(char)-64)
	if char == '"' and start == 1:
		print summ   	#check this code. something is wrong
		start = 0
		if summ in lis:
			count += 1
		summ = 0
	char = f.read(1)
f.close()
print count

