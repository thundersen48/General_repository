import sqlite3

# Подключение к базе данных или создание новой, если ее нет
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Создание таблицы пользователей
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')

# Создание таблицы задач
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        task TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
''')

# Вставка примерных данных в таблицу пользователей
cursor.execute("INSERT INTO users (name, email) VALUES ('Maksim', 'dicersmaks@mail.ru')")
cursor.execute("INSERT INTO users (name, email) VALUES ('Stepan', 'Spuzankov211@gmail.com')")

# Вставка примерных задач для пользователей
cursor.execute("INSERT INTO tasks (user_id, task) VALUES (1, 'Выполнить уроки')")
cursor.execute("INSERT INTO tasks (user_id, task) VALUES (2, 'Приготовить что-то вкусное')")

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()

print("База данных успешно создана и заполнена.")
