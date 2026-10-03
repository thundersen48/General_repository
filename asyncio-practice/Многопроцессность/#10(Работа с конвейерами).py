from multiprocessing import Pipe, Process


def pipe_worker(p: Pipe):
    some_data = 100500# Ложим данные
    p.send(some_data)# Читаем данные

def pipe_worker_2(p: Pipe):
    print(p.send(111))


if __name__ == '__main__':
    #Работа с конвейерами
    parent_pipe, child_pipe = Pipe() #Возвращение двух концов родительского и дочернего
    p = Process(target=pipe_worker, args=(child_pipe, ))# В один конец мы посылаем данные, а с друго будем их читать
    p.start()
    p1 = Process(target=pipe_worker_2, args=(child_pipe, ))
    p1.start()
    print('Информация из дочернего процесса:', parent_pipe.recv())
    parent_pipe.send('Информация из главного процесса')
    p.join()
    p1.join()