import threading
import time
#Когда несколько потоков обращаются к 1 ресурсу мы можем получить ошибку, если не синхронизируем их!

class ThreadCounter:

    def __init__(self):
        self.counter = 0
        self.lock = threading.Lock()

    def count(self,thread_no): #Thread_no - номер потока
        while True:
            self.lock.acquire()# 1 поток получает блокировку, пока не снимет ее
            self.counter += 1  # Когда поток разблокируется другие потоки могут работать!
            print(f'{thread_no}: Просто увеличение счетчика на {self.counter}')
            time.sleep(1)
            print(f'{thread_no}: работа завершилась, сейчас значение {self.counter}')
            self.lock.release()

tc = ThreadCounter()

for i in range(10):
    t = threading.Thread(target= tc.count, args=(i,))
    t.start()