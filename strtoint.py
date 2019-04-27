
hrs  = input('Enter Hours :')
h=float(hrs)
rate = input('Enter rate per hour:')
r=float(rate)

if h<=40:
    pay=h*r

elif h>40:
    pay= 40*r + (h-40)*r*1.5

else:
    print("Wrong Parameter")
print(pay)
