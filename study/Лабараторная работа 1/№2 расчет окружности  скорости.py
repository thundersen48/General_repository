import math


Ra = float(input())

if Ra >= 1.25 and Ra <= 2.5:
    Rz = 4*Ra
elif Ra >= 0.32 and Ra <=0.63:
    Rz = 5*Ra
elif (Ra < 0.04):
    Rz = 0.1
else:
    print('Введено некорректное значение')
print('Значение равно',Rz)