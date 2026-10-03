#Методы ljust(), rjust(), center()
text = 'Hello World'

# print(text.ljust(20))
# print(text.rjust(20))
# print(text.center(20))
# print(format(text, '^10'))
#Обработка нескольких значений

form = '{:>10s} {:>10s}'.format('Hello', 'World')
x = 1.2456
print(format(x,'^10.2f'))#Делаем по центру и округляем до 2 знаков после запятой!
#print(form)

""" Объединение и конкатенация строк """


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
        return value
red = int ( my_values.get (' red ' , ['']) [0] or 0 )
green  = my_values.get('green', [''])
if green[0]:
    green = int(green[0])
else:
    green = 0

def get_first_int(values,key,default = 0):
    found = values.get(key, [])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return default

get_first_int(my_values, 'green')