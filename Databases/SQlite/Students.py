import sqlite3 as sq
#insert - Добавление записи в таблицу
#select - Выборка данных из таблицы, перечисляем поля col1, col2, from <table_name>



#con = sq.connect("saper.db")#Устанавливаем связь с базой данных
with sq.connect('example.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE  IF NOT EXISTS students(
    name TEXT,
    university TEXT DEFAULT 1,
    old INTEGER,
    bachelorcourse INTEGER,
    IQ INTEGER
    )""")

    
#Передаем команды для базы данных
con.commit()#Сохранение изменений
con.close()#Закрытие соединения






"""
    cur.execute('SELECT * FROM users WHERE score <1000 ')
    result = cur.fetchall()
    print(result)

result = cur.fetchone()# Возвращает первую запись
print(result)

result2 = cur.fetchmany(2)
print(result2)
"""