import time
import threading

def get_data(data):
    while True:
        print(f'[{threading.current_thread().name}] - {data}')
        time.sleep(1)


t = threading.Thread(target=get_data, args=(str(time.time()),), daemon= True)
t.start()


























