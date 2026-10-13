#Callable - поверяет является ли объект функцией.

class Class:
    pass

def func():
    print('hi')

def func2():
    def inner():
        pass

    return inner

func3 = lambda x: x+1
not_func = 'hello'

print(callable(Class))
print(callable(func))
print(callable(func2()))
print(callable(func3))
print(callable(func3))
print(callable(not_func))

