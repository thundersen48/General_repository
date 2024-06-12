from scipy import integrate
from scipy.integrate import quad
import numpy as np
import math as m

def target_function(x):
    return 2.0 * x ** 2

#Вычисляем определенный интеграл от a до b
result1 = integrate.quad(target_function, 0.0, 4.0)

print(result1)

def integrand(t, n, x):
    return np.exp(-x*t) / t**n

result2 = integrate.quad(integrand,0.0,4.0,args=(0,2))
print(result2)


def integrand2(x):
    return 8+2*x-x**2
result3 = integrate.quad(integrand2,-2.0,4.0)
print(result3)

def integrand3(x):
    return x/(m.sqrt(m.pow(x,4)+16))

result4 = integrate.quad(integrand3,0.0,m.sqrt(3))
print(result4)


def grayscott1d(y, t, f, k, Du, Dv, dx):

    u = y[::2]
    v = y[1::2]

    # dydt is the return value of this function.
    dydt = np.empty_like(y)

    # Just like u and v are views of the interleaved vectors
    # in y, dudt and dvdt are views of the interleaved output
    # vectors in dydt.
    dudt = dydt[::2]
    dvdt = dydt[1::2]

    # Compute du/dt and dv/dt.  The end points and the interior points
    # are handled separately.
    dudt[0]    = G(u[0],    v[0],    f, k) + Du * (-2.0*u[0] + 2.0*u[1]) / dx**2
    dudt[1:-1] = G(u[1:-1], v[1:-1], f, k) + Du * np.diff(u,2) / dx**2
    dudt[-1]   = G(u[-1],   v[-1],   f, k) + Du * (- 2.0*u[-1] + 2.0*u[-2]) / dx**2
    dvdt[0]    = H(u[0],    v[0],    f, k) + Dv * (-2.0*v[0] + 2.0*v[1]) / dx**2
    dvdt[1:-1] = H(u[1:-1], v[1:-1], f, k) + Dv * np.diff(v,2) / dx**2
    dvdt[-1]   = H(u[-1],   v[-1],   f, k) + Dv * (-2.0*v[-1] + 2.0*v[-2]) / dx**2

    return dydt

rng = np.random.default_rng()
y0 = rng.standard_normal(5000)
t = np.linspace(0, 50, 11)

f = 0.024
k = 0.055
Du = 0.01
Dv = 0.005
dx = 0.025
