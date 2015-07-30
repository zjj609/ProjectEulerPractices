import string

def ReverseNum(a):
	strin = str(a)[::-1]
	return string.atoi(strin)

def IsPalindrome(a):
	if a == ReverseNum(a):
		return True
	else:
		return False

allcount = 0
for n in range(10,10000):
	result = n + ReverseNum(n)
	count = 1
	while True:
		if count >= 50:
			allcount += 1
			print n
			break
		if IsPalindrome(result):
			break
		result = result + ReverseNum(result)
		count += 1

print allcount