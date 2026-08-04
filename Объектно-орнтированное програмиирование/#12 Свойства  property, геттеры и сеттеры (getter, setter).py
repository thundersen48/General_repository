class Person:
    def __init__(self,name):
        self.name = name

    def get_name(self):
        print('From get_name()')
        return self._name

    def set_name(self, value):
        print('From set_name()')
        self._name = value

    #name = property(fget=get_name,fset=set_name)

#Альтернативная запись получения объекта
    name = property()
    name = name.getter(get_name)
    name = name.setter(set_name)




p = Person('Dima')# читаем имя
#p.name = 'Ivan'# Устанавливаем ему новое значение.
print(p.__dict__)