from collections import namedtuple

Stock = namedtuple('Stock', ['name','shares', 'price', 'date', 'time'])

# Создание экземпляра прототипа
stock_prototype = Stock('', 0, 0.0, None, None)
# Функция для преобразования словаря в Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)
# **  - позволяет взять словарь с парами ключ-значение и распаковать его в именованные аргументы в вызове функции
a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_stock(a))