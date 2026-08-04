#Написать программу для вычисления значения функции разложенной в ряд (сумму ряда) и количество итераций.
# В формулах эпсилон заданная степень точности; n - порядковый номер очередного члена ряда
import math as m


def calculate(x, eps):
    n = 1
    summ = 0
    while True:
        expression  = n*m.pow(x,(n-1))
        if abs(expression) <= eps:
            break
        summ += expression
        n += 1
    return summ, n-1

eps_values = [0.001, 0.0005, 0.001]
x_values = [0.51, 0.708, 0.9]

for eps in eps_values:
    for x in x_values:
        result, iterations = calculate(x, eps)
        print(f"При E = {eps}, x = {x}: Значение функции = {result}, Количество итераций = {iterations}")







