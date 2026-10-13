import numpy as np
import sympy as sp


def solve_fkp_symbolic():
    d1, theta2, d3 = sp.symbols('d1 theta2 d3')
    L1, L2, L3 = sp.symbols('L1 L2 L3')

    # Матрица T01
    T01 = sp.Matrix([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, L1 + d1],
        [0, 0, 0, 1]
    ])

    # Матрица T12 (a2=0, alpha2=-90 градусов)
    T12 = sp.Matrix([
        [sp.cos(theta2), 0, -sp.sin(theta2), 0],
        [sp.sin(theta2), 0, sp.cos(theta2), 0],
        [0, -1, 0, 0],
        [0, 0, 0, 1]
    ])

    # Матрица T23 (d3 = L2 + d3 + L3)
    T23 = sp.Matrix([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, L2 + d3 + L3],
        [0, 0, 0, 1]
    ])

    T03 = T01*T12*T23
    return T03


def calculate_fkp_numeric(d1_val, theta2_deg, d3_val):
    L1 = 0.46
    L2 = 0.37
    L3 = 0.13


    theta2_rad = np.radians(theta2_deg)

    # Расчет по аналитическим формулам
    total_extension = L2 + d3_val + L3

    x = -total_extension * np.sin(theta2_rad)
    y = total_extension * np.cos(theta2_rad)
    z = L1 + d1_val

    return np.array([x, y, z])


if __name__ == "__main__":
    #Вывод матрицы однородных преобразований
    T03_sym = solve_fkp_symbolic()
    sp.pprint(T03_sym)

    #Численный расчет
    print("\nЧисленный расчет ПЗК")

    # Задание обобщенных координат:
    # d1 (м), theta2 (градусы), d3 (м)
    q_d1 = 0.15
    q_theta2 = 30.0
    q_d3 = 0.20

    pos = calculate_fkp_numeric(q_d1, q_theta2, q_d3)

    print(f"Входные параметры: d1 = {q_d1} м, theta2 = {q_theta2}°, d3 = {q_d3} м")
    print(f"Координаты схвата: X = {pos[0]:.4f} м, Y = {pos[1]:.4f} м, Z = {pos[2]:.4f} м")