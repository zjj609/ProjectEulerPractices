#Project Euler Problem 206

def match(n):
    s = str(n)
    return not all(int(s[x*2]) == x+1 for x in range(9))

n = 138902663    # sqrt(19293949596979899)
while match(n*n): 
	print n
	if n%10 == 3:
		n -= 6
	elif n%10 == 7:
		n -= 4

print "Project Euler 206 Solution =", n*10    #add the trailing zero