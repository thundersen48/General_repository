

"""Кусочно-линейная аппроксимация"""


def trapezoid_rule(func, a, b, rtol = 1e-8, nseg0 = 1):
    """Правило трапеций
       rtol - желаемая относительная точность вычислений
       nseg0 - начальное число отрезков разбиения"""
    nseg = nseg0
    old_ans = 0.0
    dx = 1.0 * (b - a) / nseg
    ans = 0.5 * (func(a) + func(b))
    for i in range(1, nseg):
        ans += func(a + i * dx)

    ans *= dx
    err_est = max(1, abs(ans))
    while (err_est > abs(rtol * ans)):
        old_ans = ans
        ans = 0.5 * (ans + midpoint_rectangle_rule(func, a, b, nseg)) # новые точки для уточнения интеграла
                                                                      # добавляются ровно в середины предыдущих отрезков
        nseg *= 2
        err_est = abs(ans - old_ans)

    return ans

