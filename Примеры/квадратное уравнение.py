print(' уравнение a•x²+b•x+c=0')
a = input('Введите значение a: ')
b = input('Введите значение b: ')
c = input('Введите значение c: ')
a = float(a)
b = float(b)
c = float(c)
discr = b**2 - 4*a*c
print('Дискриминант = ' + str(discr))
if discr < 0:
    print('Корней нет')
elif discr == 0:
    x = -b / (2 * a)
    print('x = ' + str(x))
else:
    x1 = (-b + discr ** 0.5) / (2 * a)
    x2 = (-b - discr ** 0.5) / (2 * a)
    print('x₁ = ' + str(x1))
    print('x₂ = ' + str(x2))