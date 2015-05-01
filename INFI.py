from math import *
for t in range(input()) :
	n = input()
	i = 1
	p = 0
	q = 0
	while(i < n) :
		cp1 = n%i == 0
		if(cp1) :
			q = q + 1
			sr = sqrt(i)
			cp2 = i%2 == 0 and sr%1 == 0
			if(cp2) :
				p = p + 1
		
	if(p == 0) :
		print "0\n"
	else :
		p=str(p)
		q=str(q)
		print p+"/"+q
		print "\n"
