l=[1,2,3,'Hello',['test',10],'world',True]
name = ['Ivanov','Puzankov','Milkin']
# print(l[4][1])
l[2] = 'world'
# l[0:2] = [10, 15]
l.append('new')
l.extend(['Другой список'])
l2=['hi', 19,'прибавление списка']
l= l + l2
l.insert(1,'добавление нового элемента')# добавляет новый элемент с заменной старого
# l.remove('world')
# l.remove('Hello')
# el=l.pop(1)
# l.sort()
l3=['hello','hi', 'David','world','test']
# l3.sort();
# l3=sorted(l3)# сортирует список
list.reverse(l3)#разворачивает список
print(l, l.count('test'),l3,sep='\n')
print('h'> 'a')
