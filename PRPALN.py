'''
USER: rajat1gupta712
TASK: PRPALN
ALGO: ad-hoc
'''

t=input()
def isPalin(s):
    for i in range(len(s)/2):
        if s[i]!=s[len(s)-i-1]:
            return False
    return True
 
while t>0:
    t-=1
    string=raw_input()
    flag=0
    for i in range(len(string)/2):
        if string[i]!=string[len(string)-i-1]:
            flag=1
            ie=len(string)-i-1
            if isPalin(string[:i]+string[i+1:]) or isPalin(string[:ie]+string[ie+1:]):
                print 'YES'
            else:
                print 'NO'
            break
    if flag==0:
        print 'YES'