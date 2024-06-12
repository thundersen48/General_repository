import multiprocessing
import time
from random import randint
from datetime import datetime
from multiprocessing import Process
import os

# Создаем файл, который будет генерировать значения до 9000000

#with open('file.txt', 'w') as f_0:
#    for _ in range(100_000_00):
#        f_0.write(f'{randint(0,9)}\n')


def labarator(*args, **kwargs):
    result = 0
    with open('file.txt', 'r') as f_0:
        for s in f_0:
            result += randint(0, int(s)) #Будем генерировать число от 0 до случайного прочитанного числа
            #pass
    print(os.getpid(), result)

#Простой запуск

#if __name__ == '__main__':
#    start = datetime.now()
#    # Передаем процессу функции
#    p = Process(target= labarator)
#    p_1 = Process(target= labarator)
#    p.start()
#    p_1.start()
#    p.join()# Не подйем дльше, пока p не завершится
#    print('p завершился')
#    p_1.join()# не пойдем дальше, пока p_1 не завершится
#    print('p_1 завершился')
#    print(datetime.now()- start)

if __name__ == '__main__':
    start = datetime.now()
    with multiprocessing.Pool(1) as pool:
        pool.map(labarator, range(2))# map()асинхронно выполняет функции для каждого элемента итерабельной таблицы
    print(datetime.now()-start)


"""Pool удобен чтобы одну и ту же функцию вызывать в нескольких потоках с разными аргументами"""
