import time
from multiprocessing import Process
import os
from datetime import datetime




def sleeper():
    time.sleep(10)
    print(f' процесс {os.getpid()} был завершён!')

# Контролируем скрипт, как он был запущен
if __name__ == '__main__': # Идет проверка главного исполняемого файла
    start = datetime.now()
    p = Process(target = sleeper(), args= (10,))
    p_1 = Process(target = sleeper(), args= (100,))
    p_1.start()
    p.start()
    print('Два процесса были запущены')
    #Ожидаем завершения процессов
    p_1.join()
    p.join()
    print(f'Программа в процесее main {os.getpid()} была завершена! за время', datetime.now() - start)