from collections import Counter
from operator import itemgetter
#slice() - создает объект среза, который может быть использован везде где применяют срезы
# Синтаксис slice(start,stop,step)

items = [0,1,2,3,4,5,6]
a = slice(2,4)
#print(items[2:4])# Получим срез от 2 до 4
#print(items[1:4])# Получим срез от 1 до 3
items[a] = [10,11]
#print(items)

"""Накладка среза на последовательность"""

s = 'Hello'
#print(a.indices(len(s)))
#for i in range(*a.indices(len(s))):
    #print(s[i])

#Узнать какие последовательность элементов встречается чаще всего

words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
         'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
         'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
         'my', 'eyes', "you're", 'under']


word_counts = Counter(words)
top_there = word_counts.most_common(3) # most_common - позволяет выделить элементы, которые встречаются чаще всего
#print(top_there)

# Если я хочу увеличить счёт вручную, то использую сложение
morewords = ['why','are','you','not','looking','in','my','eyes']
for word in morewords:
    word_counts[word] +=1
word_counts.update(morewords)# аналогичная команда
#print(word_counts['why'])

a = Counter(words)
b = Counter(morewords)
c = a+b# Объединение счётчиков
#print(c)

'''Сортировка списка словарей по общему ключу'''
rows = [
{'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
{'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
{'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
{'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

rows_by_fname = sorted(rows, key = itemgetter('fname'))
rows_by_uid = sorted(rows, key = itemgetter('fname'))
