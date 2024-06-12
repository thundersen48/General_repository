import numpy as np
from sympy import *
from sympy.physics.mechanics import *
from scipy.integrate import solve_ivp
init_vprinting()
import matplotlib.pyplot as plt
#Константы
g = 9.81
k = 40
m = 1
#Позиция
x0 = 0
x_dot0 = 0

def spring_mass(t,y):
    return(y[1], g-k*y[0]/m)

sol = solve_ivp(spring_mass,[0,5],(x0,x_dot0),t_eval = np.linspace(0,5,5*30))
x,x_dot = sol.y
t = sol.t

m, g ,k, t = symbols('m g k t')
x = dynamicsymbols("x")# x - функция времени

x_dot = diff(x,t)
x_ddot = diff(x_dot,t)

T = 1/2*m*x_dot**2#Кинетическая энергия
V = -m*g*x + 1/2*k/x**2# Потенциальная энергия
L = T -V

# Решаем уравнение  эйлера лагранжа
eqn = diff(diff(L,x_dot), t) - diff(L,x)
sln =  solve(eqn, x_ddot)[0]
Eq(x_ddot, sln)
#Визуализируем график

plt.plot(t,x)
plt.plot(t,x_dot,'b', lw=2)
plt.title(f"Spring mass system. K/m ={k/m}, g = {g}")
plt.legend()
plt.xlabel('Time(second)')
plt.ylabel(r'$x$ (m), $\dotx$(m/s)')
plt.grid()
plt.show()