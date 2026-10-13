class Person():
    #def create(self):
    def __init__(self,name):
        self.name = name

        def display(self):
            print(self.name)



p = Person('Maks')
#p.create()#Создаем новое свойство и присваиваем значение Maks
#print(p.display)#Экземпляр класса на этапе создания абсолютно пустой
print(p.__dict__)
#Чтобы упростить себе задачу инициализации экземпляра и его методов  использую метод init


