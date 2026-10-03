import os
import shutil
import stat
import statistics
import time

a = os.stat("D:\info\primer.txt")
b = os.stat('M:\games\Disco Elysium\Disco Elysium.exe')
c = os.stat('M:\файлы\inventor')
print(time.ctime(b.st_ctime))# время последнего изменения
print(time.ctime(a.st_atime))# время последнего доступа
print(os.stat(r"D:\info"))#Информация о файлах и директориях