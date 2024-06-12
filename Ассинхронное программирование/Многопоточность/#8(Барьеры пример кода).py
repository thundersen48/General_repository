from time import sleep
import random
import threading
from threading import currentThread



def test(barrier):
    slp = random.randint(3,7)
    time.sleep(slp)
    print(f'Поток[{currentThread().name} запущен в ({time.ctime()})]')

    barrier.wait() # Данный метод будет ждать пока все потоки запустятся
    print(f'Поток [{currentThread().name}] Преодолел барьер в ({time.ctime()})')

bar = threading.Barrier(5) # Барьер будет ждать выполнение 5 потоков
"""Запускаем 5 потоков """
for i in range (5):
    threading.Thread(target= test, args=(bar,), name= f" thr-{i}").start()
