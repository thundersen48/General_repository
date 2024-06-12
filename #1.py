import sympy as sp

"""
|4x+7y= -9
|5x+8y= -10
"""
x = sp.symbols('x')
y = sp.symbols('y')

EQN1 = sp.Eq(4*x+7*y,-9)
EQN2 = sp.Eq(5*x+8*y,-10)
system = [EQN1,EQN2]
solnSet = sp.linsolve(system,x,y)

print(system)
print(solnSet)