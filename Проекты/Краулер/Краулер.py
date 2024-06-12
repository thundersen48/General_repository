import lxml
import requests
from bs4 import BeautifulSoup
from queue import Queue #Библиотека очередь

'''
Краулер - это бот, который ходит по веб-страницам и сохраняет их содержимое
Они используюстя поисковыми движками для исследования веб-сайта.
'''

DOMAIN = 'https://inf1.info/adder'
URLS_QUEUE = Queue()
URLS_BASE = set()
FILTER = {'#', ''}


def crawler():

    while True:
#Создаем условие, чтобы генератор While не работал бесконечно! Пустая ли очередь?
        if URLS_QUEUE.qsize() == 0:
            break

        url = URLS_QUEUE.get()
        URLS_BASE.add(url) #Добавляем множество, чтобы не получить дубли

        response = requests.get(url) # Забираем домен
        response.raise_for_status() # Проверка на ошибки
        print('Scan URL', DOMAIN, 'STATUS CODE', response.status_code ) #Какой url и статус

        soup = BeautifulSoup(response.content,'lxml' ) #Забираем все ссылки на страницу

        for link in soup.find_all('a'):
            link  = link.get('href')# Забираем атрибут
            print(link)
            if any(part in link for part in FILTER): #Условие для фильтра
                continue
            URLS_QUEUE.put(link)# закидываем ссылку в очередь
            breakpoint()


#Запускаем только напрямую из этого файла
if __name__ == '__main__':
    URLS_QUEUE.put(DOMAIN)
    crawler()
    try:
        crawler()
    except requests.HTTPError as error:
        print(error)
        