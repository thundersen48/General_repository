import os
import shutil
# (os.remove('D:/robo.txt'))# удаляет файл
# os.makedirs('D:/cosmos')#создает папку
# os.startfile(r'D:/readme.txt') # открывает файл
# print(dir(os))# список методов над роботой с os
# print(os.getcwd())#доступ к рабочему каталогу
# print(os.listdir()) #Перечесление файлов и папок в текущем каталоге
"""
Чтобы получить доступ к древовидной структуре папок используем модуль os.walk() 
"""
def list_files(startpath):
   for root, dirs, files in os.walk(startpath):
       if dir!= '.git':
           level = root.replace(startpath, '').count(os.sep)
           indent = ' ' * 4 * (level)
           print('{}{}/'.format(indent, os.path.basename(root)))
           subindent = ' ' * 4 * (level + 1)
           for f in files:
               print('{}{}'.format(subindent, f))
startpath = os.getcwd()
list_files(startpath)

os.chdir('../../')#поднятие на уровень выше каталога
list_files(os.getcwd())# Структура дерева каталогов

print('Before List:', os.listdir('..'))
shutil.copy('file_copy.py', 'file_copy.py.copy')
print('AFTER LIST:', os.listdir('..'))

