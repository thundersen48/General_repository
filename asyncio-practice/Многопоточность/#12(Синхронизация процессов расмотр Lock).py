import multiprocessing




lock = multiprocessing.Lock()
"""В процессах мы передаем аргумент внутрь нашего процесса"""
def get_value(l):
    l.acquire()
    pr_name = multiprocessing.current_process().name
    pass


multiprocessing.Process(target= get_value, args= (lock,))