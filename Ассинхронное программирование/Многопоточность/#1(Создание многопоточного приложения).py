import threading

def hello_from_thread():
    print(f'Привет от потока {threading.current_thread()}!')

hello_thread = threading.Thread(target= hello_from_thread)
hello_thread.start()

total_threads = threading.active_count() # Подсчет активных или запущенных в данный момент потоков
thread_name = threading.current_thread().name # имя текущего потока

print(f'В данным момент python выполняет {total_threads} потока')
print(f' имя текущего потока {thread_name}')
hello_thread.join()
