#Project Euler Problem 71

N = 3/7.
L = 1000000
mina = N
for b in range(L, L-7, -1):
    a = N - int(b*N) * 1.0/b
    if mina > a != 0: mina, minD = a,b

print "Project Euler 71 Solution =", int(minD*N), "/", minD


def gcd(a, b):
	if b == 0:return a
	return gcd(b, a % b)

print gcd(428570,999997)
