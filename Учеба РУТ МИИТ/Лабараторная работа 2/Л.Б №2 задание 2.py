import math



x1 = int(input("Введите начальное значение x (x1): "))
xn = int(input("Введите конечное значение x (xn): "))
d_x =  float(input("Введите шаг (delta_x): "))


print("Вычисление значений функции y = f(x) для x от", x1, "до", xn, "с шагом", d_x)
x = x1
a = 2.4
while x <= xn:
    y = math.log((a*x + 5)**2)/math.sqrt(x + 2) + math.exp(x)
    print("y =", y, "при x =", x)
    x += d_x

