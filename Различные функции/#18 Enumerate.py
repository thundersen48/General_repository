#Enumerate - позволят получать доступ к индексу и к значению по итерации к объекту

values = ['a','b','c','d']
for index, value in enumerate(values):
    print(f'{index}:{value}')

print(list(enumerate(values)))
# Составит список от 0 до 3 с значениями[a,b,c,d]
