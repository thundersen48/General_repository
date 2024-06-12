class Person:
    def __init__(self,name):
        self.name = name

    def __repr__(self):    #Определяет строковое значение объекта изнутри
        return f'Person({self.name})'

    def __mul__(self,x):
        if type(x) is not int:
            raise Exception('Invalid argument, must be int')
        self.name = self.name * x

    def __call__(self, y):
        print(y)

p = Person('Maks')
p(4)
print(p)