"""
Способы передачи данных конвейеры и очереди
queue и pipe
"""
"""Pipe -труба """
from multiprocessing import Queue, Pipe, Process
from queue import Empty
from time import sleep
#Worker принимает число
def worker(a: int, q: Queue= None):
    cnt = 0
    while cnt < 3:
        sleep(.1) #Какое то долгое вычисление
        q.put(cnt)#Кладем данные
        cnt+=1
    print('W1 завершен!')

def worker2(a: int, q: Queue):
    cnt = 0
    while cnt < 3:
        sleep(.1) # Какое-то долгое вычисление
        cnt += 1
    print('!!!', q.get())
    q.put(1241231234)


if __name__ == '__main__':
    q = Queue()# Объект типа очередь
    p = Process(target = worker, args=(2, q))
    p.start()
    p1 = Process(target = worker2, args=(2, q))
    p1.start()
    #sleep(1)
#Отрабатываем ошибку
    try:
        for _ in range(10):
            print(q.get(timeout=1))
    except Empty as err:
        print('Empty q', err)
    q.put(123123)
    p1.join()
    p.join()
