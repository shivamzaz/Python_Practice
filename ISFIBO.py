'''
USER: rajat_gupta712
TASK: Is Fibo
ALGO: Simple Maths
TAG:  HackerRank
'''

from math import *
for i in range(int(raw_input())) :
	n = int(raw_input())
	a = sqrt(5*(n**2)+4)
	b = sqrt(5*(n**2)-4)
	if a % 1 == 0 or b % 1 == 0 :
		print "IsFibo"
	else :
		print "IsNotFibo"
