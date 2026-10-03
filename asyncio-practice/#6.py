import threading

def worker(num):
    '''функция обработки потока'''
    print('Worker: %d'%num, #%- это остаток от деления
          '; Thread ID: %d' %threading.get_ident())

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args = (i,))
    threads.append(t)
    t.start()

#Ожидание завершения всех потоков
for thread in threads:
    thread.join()