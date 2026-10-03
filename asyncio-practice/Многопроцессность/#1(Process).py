import time
from multiprocessing import Process
import os


CNT = 0

def f():
    global CNT
    print(f'F начала работать из', os.getpid()) #Получаем индификатор текущего процесса
    time.sleep(3)
    CNT += 2
    print(f'f:{CNT} from', os.getpid())


if __name__ == '__main__': # Идет проверка главного исполняемого файла
    p = Process(target= f, args=())
    p.start()
    p_1 = Process(target=f, args=())
    p_1.start()
    print('Finished!')

"""Получим параллельность выполнения программы"""

"""
Зачем нужен Process ?
мы можем облегчить написание кода, это удобнее чем писать с fork!
Управлять процессами очень удобно
"""