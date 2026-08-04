import sqlite3 as sq



#con = sq.connect("saper.db")#Устанавливаем связь с базой данных
with sq.connect('user.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER,
    score INTEGER,
    time INTEGER
    )""")