import time
import os
import threading
from threading import Thread
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
#  ThreadPoolExecutor - Это класс потоков, представляющий пул потоков для выполнения i-o bound задач, блокирование выполнения потока

def func_sleep():
    """функция с i/o операции"""
    """Запрашиваем идентификатор потока и идентификатор процесса"""
    print(f'Это поток {threading.get_ident()} из процесса {os.getpid()}')
    time.sleep(1)

def func_heavy_match():
    """функция с тяжелыми вычислениями"""
    cnt = 0
    for _ in range(50_000_000):
        cnt += 1
print(f'Это поток {threading.get_ident()} из процесса {os.getpid()}')



start_time = datetime.now()
# th_1 = Thread(target=func_heavy_match())
# th_2 = Thread(target=func_heavy_match())
# th_3 = Thread(target=func_heavy_match())
# th_1.start()
# th_2.start()
# th_3.start()
# th_3.join()
# th_2.join()
# th_1.join()
with ThreadPoolExecutor(max_workers=3) as t:
    [t.submit(func_heavy_match) for _ in range(3)]
print(f'{datetime.now()- start_time}')