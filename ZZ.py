'''
USER: rajat1gupta712
TASK: PRPALN
ALGO: ad-hoc
'''

for test in range(int(raw_input())):
	counter=0
	str_org = raw_input()
	n = len(str_org)
	
	for i in range(int(len(str_org)//2)) :

		str_cut1 = str_org[:i] + str_org[(i+1):]
		str_rev1 = str_cut1[::-1]
		str_cut2 = str_org[:n-i-1] + str_org[(n-i):]
		str_rev2 = str_cut2[::-1]
		if str_cut1 == str_rev1 :
			counter = counter+1
			break
		elif str_cut2 == str_rev2:
			counter = counter+1
			break
	if counter != 0:
		print "YES"
	else:
		print "NO"