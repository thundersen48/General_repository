import math


# Ввод значений
x1 = int(input("Введите начальное значение x (x1): "))
xn = int(input("Введите конечное значение x (xn): "))
d_x =  int(input("Введите шаг (delta_x): "))
a = 2.4
# Использование цикла for для вычисления значений функции
for x in range(x1, xn + 1, d_x):
    y = math.log((a * x + 5) ** 2) / math.sqrt(x + 2) + math.exp(x)
    print(f"При x = {x}, y = {y}")
    x += d_x

