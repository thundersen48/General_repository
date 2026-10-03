from collections import defaultdict



d = {
    'a': [1,2,3],
    'b': [4,5]
}

e = {
    'a': {1,2,3},
    'b': {4,5}
}

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'AAPL': 612.78,
    'FB': 10.75
}



prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)
print(min(prices.values()))
print(max(prices.values()))

#Получаем ключ, соответствующий минимальному или максимальному значению

print(min(prices, key = lambda k: prices [k]))
print(max(prices, key = lambda k: prices [k]))

#Чтобы получить минимальное значение, нужно дополнительное обращение

min_value = prices[min(prices, key = lambda k: prices [k])]
print(min_value)