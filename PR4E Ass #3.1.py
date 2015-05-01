hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter Rate per hour:")
r = float(rate)
if h<=40 :
    pay = h*r
if h>40 :
    pay = (40*r)+(r*1.5*(h-40))
    
    
print pay
