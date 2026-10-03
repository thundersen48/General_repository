import multiprocessing




Rlock = multiprocessing.RLock()
"""В процессах мы передаем аргумент внутрь нашего процесса"""

def get_value(l):
    l.acquire()
    pr_name = multiprocessing.current_process().name
    print(f'Процесс [{pr_name}] запущен')


multiprocessing.Process(target= get_value, args= (Rlock,)).start()
multiprocessing.Process(target= get_value, args= (Rlock,)).start()