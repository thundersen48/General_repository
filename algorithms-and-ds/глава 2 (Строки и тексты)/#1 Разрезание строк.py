import re
from urllib.request import urlopen

line = 'asdf fjdk; afed, fjek,asdf, foo'

#Разделение линии на подстроки, используя набор символов, включающий точку с запятой ;, запятую , и пробел \s.
l = re.split(r'[;,\s]*',line)
fields = re.split(r'(;|,|\s)\s*', line)
print(l)
print(fields)

#переформирование строки с разделителями.
values = fields[::2]
delimiters = fields[1::2] + ['']
print(delimiters)
''.join(v+d for v,d in zip(values, delimiters))
"""Чтобы проверить начало и конец строки удобно пользоваться методом endswitch()"""

filename = 'spam.txt'
b = filename.endswith('.txt')
#print(b)

name = ['http://www.python.org']

def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

"""Организация срезов"""

f = 'Apple'
print(f[4:] == 'e')