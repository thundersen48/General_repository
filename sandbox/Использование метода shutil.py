import os
import shutil
import time
def file_metadata(file_name):
    stat_info = os.stat(file_name)#информация о файлах и директории
    print(' Mode :', oct(stat_info.st_mode)) #st_mode представляет тип файла и биты режима файла (разрешения). # Функция oct int в 8- ричную
    print(' Created :', time.ctime(stat_info.st_ctime)) #Функция ctime() модуля time преобразует время
    print(' Accessed:', time.ctime(stat_info.st_atime))
    print(' Modified:', time.ctime(stat_info.st_mtime))
#st_ctime : представляет время последнего изменения метаданных в Unix и время создания в Windows. Выражается в секундах.
os.mkdir('journaldev') # создает пустую папку, каталог
# st_atime : представляет время последнего доступа. Выражается в секундах.
# t_mtime : представляет время последней модификации контента. Выражается в секундах.
print('SOURCE FILE:')
file_metadata('file_copy.py')
shutil.copy2('file_copy.py', 'journaldev') # копирует содиржимое и текст исходного файла в каталог и поддерживает метаданные исходного файла.

print('DESTINATION FILE:')
file_metadata('journaldev/file_copy.py') #поиск данных в указанном каталоге.