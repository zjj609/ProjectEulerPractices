file_url = 'G:\\test_c\\projectEuler\\p081_matrix.txt'
matrix = [map(int, row.split(',')) for row in open(file_url).readlines()]
n, m = len(matrix), len(matrix[0])

for i in xrange(n):
    for j in xrange(m):
    	if i*j > 0:
    		matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1])
    	elif i > 0:
    		matrix[i][j] += matrix[i-1][j]
    	elif j > 0:
    		matrix[i][j] += matrix[i][j-1]
    	else:
    		matrix[i][j] += 0
 
print "Minimal path sum in", n, "by", m, "matrix =", matrix[-1][-1]