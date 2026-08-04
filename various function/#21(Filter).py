#Filter - Позволяет фильтровать значение в итерируемом объекте
# filter - 1 аргумент функция, второй аргумент итерируемый объект
def filter_func(value):
    return value % 2 == 0

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]# Итерируемый объект(Список чисел)
#evens = filter(lambda x: x % 2 == 0, lst)# Передаем функцию фильтрации, с помощью lambda функии создаюм перменную x
def func_filter(num):
    if num % 2 == 0:
        return True
    else:
        return False
evens_2 = filter(func_filter, lst)


print(evens_2)
print(list(evens_2))