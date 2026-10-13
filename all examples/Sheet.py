import sympy as sp

# Символьные переменные
th1, th2, th3, th4, th5, th6 = sp.symbols('theta_1:7')
a2, a3 = sp.symbols('a_2 a_3')
d1, d4, d5, d6 = sp.symbols('d_1 d_4 d_5 d_6')


def dh_matrix(a, alpha, d, theta):
    c, s = sp.cos, sp.sin
    return sp.Matrix([
        [c(theta), -c(alpha) * s(theta),  s(alpha) * s(theta), a * c(theta)],
        [s(theta),  c(alpha) * c(theta), -s(alpha) * c(theta), a * s(theta)],
        [0,         s(alpha),            c(alpha),           d],
        [0,         0,                   0,                  1]
    ])


# Матрицы перехода по параметрам ДХ
T01 = dh_matrix(0,  sp.pi / 2, d1, th1)
T12 = dh_matrix(a2, 0,         0,  th2)
T23 = dh_matrix(a3, 0,         0,  th3)
T34 = dh_matrix(0,  sp.pi / 2, d4, th4)
T45 = dh_matrix(0, -sp.pi / 2, d5, th5)
T56 = dh_matrix(0,  0,         d6, th6)

# Перемножение матриц
T06 = sp.trigsimp(T01 * T12 * T23 * T34 * T45 * T56)

print("Матрица T06:")
sp.pprint(T06)

# Численный расчет для нулевой конфигурации
params = {
    th1: 0, th2: -sp.pi/2, th3: 0, th4: -sp, th5: 0, th6: 0,
    d1: 0.181, a2: 0.613, a3: 0.571, d4: 0.135, d5: 0.120, d6: 0.117
}

print("\nЧисленное значение T06 (theta = 0):")
sp.pprint(T06.subs(params))


with open("result.txt", "w", encoding="utf-8") as f:
    f.write(f"Матрица T06:\n{sp.pretty(T06)}\n\n")
    f.write(f"Численное значение (theta = 0):\n{sp.pretty(T06.subs(params))}")