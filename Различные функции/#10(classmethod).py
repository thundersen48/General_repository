#@class method

class TestClass:
    def regular_method(self):
        print(self)

    @classmethod#Используем в качестве декоратора(Получаем доступ к классу а не к экземпляру)
    def class_method(cls):
        print(cls)

    def __str__(self):
        return 'TestClass Instance'

t = TestClass()
t.regular_method()
t.class_method()
TestClass.class_method()

#@classmethod используется, когда вам нужно получить методы, не относящиеся к какому-либо конкретному экземпляру
