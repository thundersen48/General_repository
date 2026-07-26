#Ввод значений:
x = float(input("Введите x: "))
n = int(input("Введите n: "))
k = 1

def mul(k):
    res = 1.0
    # Цикл, в котором переменная m принимает значения от 1 до k + n
    for m in range(1, k + n):
        if m == 3 or m ==2: #пропуск,когда числитель и знаменатель равны нулю
            continue
        res *= (m ** 3.0 - 8.0) / (m - 3.0)
    return res

def sum(x, n):
    res = 0.0
    for k in range(1, n ):
        tmp = (k - 2.0) * (x ** (3.0 * k + 1.0))
        if tmp == 0:
            continue # пропуск, когда знаменатель равен нулю (дробь равна бесконечности)
        tmp = (-3.0 ** (3.0 * k + 1.0)) / tmp
        if tmp == 0:
            continue
        res += tmp * mul(k)
    return res

print("Результат: ",(sum(x, n)))

