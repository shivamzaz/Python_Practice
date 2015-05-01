inp = raw_input("Enter Score:")
s = float(inp)
if (s>1.0) :
    grade = 'E'
elif (s>=0.9) :
    grade = 'A'
elif (s>=0.8) :
    grade = 'B'
elif (s>=0.7) :
    grade = 'C'
elif (s>=0.6) :
    grade = 'D'
elif (s<0.6) :
    grade = 'F'
    
    
if grade!='E' :
    print grade
else :
    print "ERROR"

