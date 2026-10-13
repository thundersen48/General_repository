def get_sum(a,b):
    """
    возращает сумму аргументов a и b

    :param a: Первый операнд
    :type a: int
    :param b: Второй операнд
    :type b: int
    :return: Return type int
    """
    return a+b
# print(get_sum(1,2))

def get_sum(a,b):
    """"
    возращает сумму аргументов a и b.


    :param a: Первый операнд
    :type a: int
    :param b: Второй операнд
    :type b: int
    :return: type int
    """
    return a + b


# print (get_sum(1,2))


a = 5# глобальная переменная
# def f():
#     a = 10 # Локальная переменная
#     a += 1
#     print(a)
# print(a)
#
# f()
# print(a)

# def f():
#     global a
#     a += 1
# print(a)
# f()
# print(a)


l = [1,'2',3]
def f(l):
    return [i*2 for i in l]
print(f(l))


def f3(l):
    def get_mult(x):
        if isinstance(x, int):
            return x*2
    return [get_mult(i) for i in l if get_mult(i)] #Сделай операцию get_mult в том случае если это будет не None
print (f3(l))









def f4(l):
    def get_mult (x):
            return x*2
    return list(map(get_mult, l))
print (f4(l))





















