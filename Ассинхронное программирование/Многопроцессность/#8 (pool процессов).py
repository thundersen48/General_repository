import os
from multiprocessing import Pool
from time import sleep

#Главный процесс
def f(x):# Функция принимает число
    print(os.getpid(), 'sleep!')#Печатаем id нашего процесса
    sleep(1)# Спим 1 секунду
    return x * x #Возвращаем квадрат x

#два процесса дочерние
if __name__ == '__main__':
    pool = Pool(6)# По сути это телеграф, указываем ему кол-во кабинок, запускаем кол-во функций(указываем кол-во процессов)
    #pool.map(f,(1,2,3,4,5,6))
    #res =pool.apply(f,(2,))# Дожидаемя завершения работы, не будем идти дальше
    #print(res)
    res = pool.map_async(f,(2,3,4,5,6,7))#Принимает только один результат, следовательно выполняясь в процессе она принимает 1 аргумент!
    #print(res.get())
    multiple_results = [pool.apply_async(f, args=(i,)) for i in range(4)]
    print(multiple_results)
    for res in multiple_results:
        print(res.get())
    pool.close()
    pool.join()