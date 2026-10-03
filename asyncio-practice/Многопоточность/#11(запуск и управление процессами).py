import multiprocessing
import time
"""

def test():
    while True:
        print(time.time())
        print(f'{multiprocessing.current_process()}')
        time.sleep(1)

time.sleep(10)
pr = multiprocessing.Process(target = test, name = 'Процесс - 1')
pr.start()
print('Процесс запущен!')
print(pr.is_alive())# на выводе получим True или false если наш процесс не работает
print(pr.pid) #Получим id процесса
print(pr.terminate())# Убиваем процесс
"""

# Инициализация процесса в виде класса

class process(multiprocessing.Process):
    def run(self):
        print("work")

pr = process() # Инициализация класса
pr.start()