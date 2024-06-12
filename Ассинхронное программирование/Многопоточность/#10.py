import threading, time

def worker(barrier):
    th_name = threading.current_thread().name
    print(f'{th_name} в ожидании барьера с {barrier.n_waiting} другими')
    try:
        worker_id = barrier.wait()
    except threading.BrokenBarrierError:
        print(f'{th_name} сброшен')
    else:
        print(f'{th_name} прохождение барьера {worker_id}')

# число потоков, при использовании
# барьеров оно должно быть постоянным
NUM_THREADS = 3

# обратите внимание происходит установка
# барьера на 1 больше чем запускается потоков
barrier = threading.Barrier(NUM_THREADS + 1)

threads = []
# создаем и запускаем потоки
for i in range(NUM_THREADS):
    th = threading.Thread(name=f'Worker-{i}',
                          target=worker,
                          args=(barrier,),
                         )
    threads.append(th)
    print(f'Запуск {th.name}')
    th.start()
    time.sleep(0.3)