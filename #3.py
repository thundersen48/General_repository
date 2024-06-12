from sympy import symbols, Eq, solve

# Определяем символьные переменные
x, y = symbols('x y')

# Задаем систему уравнений
eq1 = Eq(2*x + y, 5)
eq2 = Eq(x - y, 1)

# Решаем систему уравнений
solution = solve((eq1, eq2), (x, y))

# Выводим решение
print("Решение системы уравнений:")
print(f"x = {solution[x]}, y = {solution[y]}")
