from multiprocessing import Process, Pool, Lock
from time import sleep
from random import random

def releaser(l):
    print('Выполнение какой-то работы')
    l.release()

def file_writer(start: int, finish:int, l:Lock):
    l.acquire()
    for i in range(start, finish): # Берем число от start до finish
        with open('locker.txt', 'a') as f_o:  # a - append
            sleep(1)
            print(i)
            # Выводим число на экран
            f_o.write(str(i) + '\n')# Записываем число в файл
    p = Process(target= releaser, args=(l,))
    p.start()

if __name__ == '__main__':
    lock = Lock()
    p1 = Process(target=file_writer, args=(0,5, lock))
    p2 = Process(target=file_writer, args=(5,10, lock))
    p1.start()
    p2.start()
    p2.join()
    p1.join()