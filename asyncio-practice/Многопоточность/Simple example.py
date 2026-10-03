import time
import threading

def get_data(thr_name, data):
    while True:
    print(f'[{threading.currentThread().name}] -{data}')
    time.sleep(1)

thr = threading.Thread(target = get_data, args =(str(time.time())), name='thr-1')# Ставим запятую, чтобы python воспринимал как кортеж
thr.start()