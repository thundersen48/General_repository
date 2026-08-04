def upper_attr(future_class_name, future_class_parents, future_class_attr):
  """
    Возвращает объект-класс, имена атрибутов которого
    переведены в верхний регистр
  """

  attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
  # переводим их в верхний регистр
  uppercase_attr = dict((name.upper(), value) for name, value in attrs)

  # создаём класс с помощью `type`
  return type(future_class_name, future_class_parents, uppercase_attr)

__metaclass__ = upper_attr # это сработает для всех классов в модуле

class Foo(object):
  # можно определить __metaclass__ здесь, чтобы сработало только для этого класса
  bar = 'bip'

#print(hasattr(Foo, 'bar'))
#print (hasattr(Foo, 'BAR'))


f = Foo()
#print(f.bar)




def get_first_name(self):
  return self.first_name

def get_last_name(self):
  return self.last_name

def get_middle_name(self):
  return self.middle_name

def init(self, first_name, last_name, middle_name):
  self.first_name = first_name
  self.last_name = last_name
  self.middle_name = middle_name

class BaseUser(object):
  def __str__(self):
    return '<user-object/>' # Возвращение просто строки

attrs = {
  'first_name': '',
  'last_name': '',
  'middle_name':'',
  'get_first_name': get_first_name,
  'get_last_name': get_last_name,
  'get_middle_name': get_middle_name,
  '__init__': init
}

bases = ( #Кортеж, состоящий из родительских классов которые мы будет использовать для создания User
  BaseUser,

)
User = type('User', bases, attrs) #Новый класс User, Bases - определяет родительские классы, dict - определяет словарь с пространством времен для класса
User1 = User('John', 'Test', 'Te100vi4')
print(str(User1))
print(User1.get_first_name())
print(User1.get_last_name())
print(User1.get_middle_name())
def build_class(class_name, base_classes, attrs):
  new_attr = {}
  for attr in attr.items():
    new_attr[attr.lower()] = value # Приводим названия с верхнего регистра в нижний
  return  type(class_name, base_classes, new_attrs)
