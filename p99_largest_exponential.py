import urllib2
from math import log
file2 = open('G:\\test_c\\projectEuler\\p099_base_exp.txt')
pairs2 = file2.read().split('\n')

#file_url = 'https://projecteuler.net/project/resources/p099_base_exp.txt'
#pairs = urllib2.urlopen(file_url).read().split('\n')
mv, ml = 0, 0

for ln, line in enumerate(pairs2, start=1):
    b, e = line.split(',')
    v = int(e) * log(int(b))
    if v > mv:
        mv, ml = v, ln

print "Project Euler 99 Solution =", ml

ll = ['13846,725685','13245,73564']
for i , j in enumerate(ll):
	print i,j

