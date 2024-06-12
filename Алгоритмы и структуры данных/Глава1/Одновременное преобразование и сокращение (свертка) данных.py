import os
"""
Вам нужно выполнить функцию сокращения (т. е. sum(), min(), max()), но сначала
необходимо преобразовать или отфильтровать данные.
"""

# Подсчет суммы квадратов

nums = [1,2,3,4,5]

s = sum(x*x for x in nums)
#print(s)

#Определяем есть ли файлы в каталоге

files = os.listdir('../Heapq')
if any(name.endswith('.py') for name in files):
    print('Yes')
else:
    print('No')


portfolio = [
{'name':'GOOG', 'shares': 50},
{'name':'YHOO', 'shares': 75},
{'name':'AOL', 'shares': 20},
{'name':'SCOX', 'shares': 65}
]

min_shares = min(portfolio, key = lambda s: s['shares'])
print(min_shares)