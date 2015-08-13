import time
time1 = time.clock()

def primes(ubound):
    size = (ubound - 3) / 2
    a = [False] * size
    s = 0
    primes = []
    while s < size:
        t = 2 * s
        p = t + 3
        primes.append(p)
        for n in range(t * (s + 3) + 3, size, p):
            a[n] = True
        s = s + 1
        while s < size and a[s]:
            s = s + 1
    return primes

pprimer = primes(100000000)
print pprimer[0],pprimer[1],pprimer[-1]

time2 = time.clock()
print time2-time1