import math as m

a = 2.7
b = 4.4

x = float(input())

if x<=3:
    y = m.sqrt(a*(m.pow(x,2)))+ 1
elif x > 3 and x < 6:
    y = m.log(b*x)
elif x>=6:
    y = m.cos((3*x**2)/(1+a*x))

print(y)