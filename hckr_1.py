t=int(raw_input())
while(t):
	l=[]
	c=[]
	x=[]
	p=[]
	cnt=0
	a,b=map(int,raw_input().split())
	for i in range(0,a,1):
		str=raw_input()
		p=len(str)
		l.append(p)
	c=l
	#for i in range(0,a,1):
	#	c[i]=l[i]
	l.sort()
	p=list(set(l))
	g=len(p)
	for i in range(0,g,1):
		h=l.count(p[i])
		x.append(h)
		#k+=1
	for i in range(0,g,1):
		if(x[i]==b):
			cnt+=1
	if(cnt==g):
		print("Possible")
	else:
		print("Not possible")
	t-=1
	
	
	
		
		


	
	
