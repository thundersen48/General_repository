class Foo:
    def show(self):
        print('Hi')
def add_attribute(self):
    self.z = 9

Test = type('Test', (Foo,), {'x':5, 'add_attribute':add_attribute}) # Класс test, () - определяет родительский класс; {} - определяет аттрибуты
t = Test()
t.add_attribute()
print(t.z)

class Meta(type):
    def __new__(self, class_name, bases, attrs):
        print(attrs)
        return type(class_name, bases, attrs)

class Dog(metaclass = Meta):
    x = 5
    y = 8

    def hello(self):
        print("Hello")