import math as m

a = 1.83
b = 2.27

x = float(input())

if x<=-1:
    y = a+b*m.exp(x)
elif x > -1:
    y = m.pow(3,m.cos((a*x)**2))

print(y)
