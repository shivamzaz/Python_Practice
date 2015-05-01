dc = list()
dd = list()
dorg = list()

for i in range(int(raw_input())) :
	s = raw_input()
	dc.append(s)

s = raw_input()
dd = s.split()


for elem in dd :
	if elem not in dc:
		dorg.append(elem)
		ch = elem[0]
		for word in dc :
			if word.startswith(ch) :
				dorg.append(word)
	else:
		dorg.append(elem)

print ' '.join(dorg)