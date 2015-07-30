def prime(n):
    lis = {}
    for i in xrange(2,n+1):     
        if not i in lis:
            lis[i] = 1
            k = i*2
            while k <= n:
                lis[k] = 0
                k = k+i
    return lis

def WeiShu(a):
	temp = a
	weishu = 0
	while(temp>0):
		temp /= 10
		weishu += 1
	return weishu

def FanZhuan(a,x):
	temp = a/10
	temp += (10**(x-1))*(a % 10)
	return temp



n = 999999
lis2 = prime(n)
count = 0
for i in xrange(2,n+1):
	if(lis2[i]==1):
		weishu = WeiShu(i)
		if(weishu == 1):
			count+=1
		else:
			change_num = i
			temp_count = 0
			for j in range(1,weishu):
				change_num = FanZhuan(change_num,weishu);
				if(lis2[change_num] == 1):
					temp_count+=1
			if(temp_count == (weishu-1)):
				count+=1

print count


