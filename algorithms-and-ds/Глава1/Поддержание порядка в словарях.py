from collections import OrderedDict

# Упорядочневание ключей в соответствии с порядком добавления!
d = OrderedDict() #Присваиваем значения 1234 именам
d['foo'] = 1
d['Bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key, d[key])


# Сортировка минимального и максимального значения

prices = {

    'Acme': 45.23,
    'AAPL': 612.78,
    'ibm': 205.55,
    'hpq': 37.20
}
# Чтобы найти максимальную и минимальную цены используем zip()

min_price = min(zip(prices.values(), prices.keys())) # Где keys, название ключа
max_price = max(zip(prices.values(), prices.keys()))
print(min_price)
print(max_price)


d = {}
for key, values in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)