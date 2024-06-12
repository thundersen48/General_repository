import unicodedata
import sys
text = 'yeah, but no, but yeah, but no, but yeah'

text == 'yeah'

# Совпадение по началу или концу

sovp = text.startswith('yeah')
#print(sovp)

"""Срезание символов"""

# #s = '-------------Maks   $$$$$$$'
# #s2 = s.strip()
# sm = s.lstrip('-')
# print(sm)
# print(s2)

"""Некий деятель ввел текст «pýtĥöñ» в форму на вашей веб-странице, и вы хотите
как-то почистить эту строку."""

s = 'pýtĥöñ\fis\tawesome\r\n'

#Удалим пробел
remap = { ord('\t') : ' ',
 ord('\f') : ' ',
 ord('\r') : None  }

a = s.translate(remap)
#Создаем словарь, отображающий все комб символы unicode на None
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD', a)

b.translate(cmb_chrs)
print(s)
print(b)

"""Хотим вычистить все пробелы"""

def clean_spaces(s):
 s = s.replace('\r','')
 s = s.replace('\t','')
 s = s.replace('\f','')
 return s