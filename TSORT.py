'''
USER: rajat1gupta712
TASK: TSORT
ALGO: Sorting
'''

from sys import stdin
 
t=int(stdin.readline())
l=stdin.readlines()
l.sort(key=int)
print '\n'.join(l) 