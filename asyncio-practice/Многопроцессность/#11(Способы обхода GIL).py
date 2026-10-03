import multiprocessing

def worker(data):
    #Обрабатываем данные
    result = data * 2
    return result

data = [1,2,3,4,5]

pool = multiprocessing.Pool(multiprocessing.cpu_count())
#Используем многопроцессорный пул для обработки данных
result = pool.map(worker,data)

pool.close()
pool.join()
print('Результаты:', result)