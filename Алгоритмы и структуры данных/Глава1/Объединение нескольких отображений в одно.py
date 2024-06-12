from collections import ChainMap
from collections import namedtuple
from collections import Counter


a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
#Деалем проверку, сначала в словаре a затем в b
c = ChainMap(a,b)
#print(c['z'])

#print(len(c))
#Операции, которые изменяют отображение, всегда действуют на первое отображение в списке

Values = ChainMap()
Values['x'] = 1
Values = Values.new_child() #Добавляем новое отображение
Values['x'] = 2
Values = Values.new_child()
Values['x'] = 3
#Удаляем последнее отображение
Values = Values.parents
#print(Values)

"""Слияние словарей с помощью метода update()"""

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

merged = dict(b)
merged.update(a)
print(merged['x'])

#Подсчет кол-во оьъектов каждого типа:

Request = namedtuple("Request", ("type", "text"))

requests = [
  Request(type="question", text="Как пасти котов?"),
  Request(type="problem", text="Бакланы портят стадион"),
  Request(type="idea", text="Переводчик с лисьего на русский"),
  Request(type="problem", text="Кот крадёт электричество"),
  Request(type="problem", text="Мыши похитили 540 кг марихуаны"),
  Request(type="idea", text="Холодильник с таймером"),
]

stats = Counter(req.type for req in requests)

print(dict(stats))