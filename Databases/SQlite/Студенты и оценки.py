import sqlite3 as sq

students = [
    (1,'Oleg','Man',19),
    (2,'Maria','woman',35),
    (3,'Sara','woman',18)
]


with sq.connect("Student grades.db") as con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS students(
    id INTEGER,
    name TEXT,
    sex INTEGER,
    old INTEGER,
    image BLOB
    )""")
    #Позволяет добавить записи в таблицу
    cur.executemany('INSERT INTO students VALUES(?,?,?,?)',students)
    cur.execute("UPDATE students SET old = :old WHERE name LIKE 'M%'", {'old': 14})# Обновляем базу данных
    con.commit()


    cur.execute("""CREATE TABLE IF NOT EXISTS marks(
    id integer,
    subject TEXT,
    mark INTEGER
      )""")
#Функция считывание изображения
"""IOError - Возникает когда операция ввода/вывода не работает 
например, заявление для печати или функции Open() при попытке открыть файл, который не существует."""

def readImage(n):
    try:
        with open(f'1103.jpg', 'rb') as f:
            return f.read()
    except IOError as e:
        print(e)
        return False
last_row_id = cur.lastrowid
#Передаем занчение
img = readImage(1)
if img:
    binary = sq.Binary(img)
    cur.execute('INSERT INTO students VALUES (1,"Braian",1, ?)',(binary,))
#Создание бэкапа


for sql in con.iterdump():
    print(sql)

con.commit()
con.close()