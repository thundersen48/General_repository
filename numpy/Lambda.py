"""
Lambda используется там, где синтаксис языка
не позволяет использовать def
"""
def rectangle_area(a,b):
    return a*b
print(rectangle_area(10,5))
# решение задачи в 1 строчку кода
print((lambda a, b: a*b)(10,5))

#Функция максимума
def maximum(a,b):
    if a > b:
        return a
    else:
        return b
print(maximum(10,3))
# Решение в 1 строчку
print((lambda a,b: a if a>b else b))