import sympy as smp

t,h0,v0,g,vp,q = smp.symbols('t h_0 v_0 g v_p q', real = True, positive = True)

h0t = h0- v0*t - smp.Rational(1,2) *g*t**2
dh0dt = g*t - v0
hpt = vp*t + smp.Rational(1,2) *q*t**2
dhpdt = vp +q*t
b = smp.Rational(1,4)

#Задаем переменные
h0 = 1
v0 =5
t = 2
g = 10
vp = 5

q0 = h0t
q1 = h0t - hpt
q2 = dh0dt + dhpdt

print(smp.solve(q1,q0,q2))
print(q1)
print(q2)
print(h0t)
print(b)