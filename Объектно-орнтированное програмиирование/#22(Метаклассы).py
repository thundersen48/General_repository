class Meta(type):
    def __init__(cls, name, bases, namespace):
        super(Meta, cls).__init__(name, bases, namespace) # Переопредление магического метода __init__
        print("Creating new class: {}".format(cls))

    def __call__(cls): # Создаем новый экземпляр
        new_instance = super(Meta, cls).__call__()
        print("Class {} new instance: {}".format(cls, new_instance))
        return new_instance
#Синглетон - это класс, который может наследовать 1 экземпляр!
class SingletonBase:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls, *args, **kwargs)

        return cls.instance

class A(SingletonBase):
    pass

class B(A):
    pass

print(A())
print(B())

