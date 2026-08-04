class Person():
    def hello (self):
        print('hello')


    @staticmethod
    def goodbye():
        print('Goodbye')


a = Person()#a и b разные объекты id()
b = Person()
print(id(a.goodbye()),id(b.goodbye()),sep='\n')
#Использование статичных методов экономит память и ресурсы компьютера
#Статичный метод это один объект на все экземпляры класса.
