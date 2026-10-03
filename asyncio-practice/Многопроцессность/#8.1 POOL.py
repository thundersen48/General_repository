import time
import multiprocessing
from multiprocessing import Pipe

a,b = Pipe()
a.send([1,'hello'])# Отправка данных
#print(b.recv())#получение данных
#Наша функция использует данные отправляя канал
def send_data(conn):
    conn.send('Чтение данных')
    conn.send('Чтение данных 2')
    conn.close()

def send_data2(conn):
    conn.send('Hello IT')

if __name__ == '__main__':
    output_c, input_c = Pipe()
    multiprocessing.Process(target=send_data,args=(input_c,)).start()
    multiprocessing.Process(target=send_data2,args=(input_c,)).start()
    print('data:', output_c.recv())
    print('data:', output_c.recv())
    print('data:', output_c.recv())