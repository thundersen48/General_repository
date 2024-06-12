import sqlite3 as sq

#con = sq.connect("saper.db")#Устанавливаем связь с базой данных
with sq.connect('saper.db') as con:
    cur = con.cursor()#Cursor
#Передаем команды для базы данных
    cur.execute('DROP TABLE IF EXISTS users')
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL, 
    sex INTEGER NOT NULL DEFAULT 1, 
    old INTEGER,
    score INTEGER
    )""")

con.close()