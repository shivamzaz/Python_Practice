from sys import stdin
 
t=int(stdin.readline())

def find_gcd(a, b) :
	if b == 0 :
		return a
	else :
		return find_gcd(b, a%b)

for test in range(0,t) :
	n, k = map(int, stdin.readline().split())
	a = map(int, stdin.readline().split())
	for query in range(0, k) :
		gcd = 0
		l, r = map(int, stdin.readline().split())
		for i in range(0, n) :
			if i >= l-1 and i <= r-1 :
				continue
			else:
				gcd = find_gcd(gcd, a[i])
		print gcd