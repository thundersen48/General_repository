"""
Используя семафоры мы можем ограничить одновременное кол-во выполняемых потоков
"""
from threading import Thread, BoundedSemaphore, currentThread
import random

max_connections = 5 # указываем кол-во потоков
pool = BoundedSemaphore(value=max_connections)
"""
Псоле выполнения 5 токов происходит запуск следующих
"""
def test():
    while True:
        with pool: #Используем with для более короткой записи
            slp = random.randint(1, 5)
            print(f"{currentThread().name}-sleep({slp})")
            time.sleep(slp)


for i in range(10):
    Thread(target=test, name = f"thr-{i}").start()
Thread(target=test).start()