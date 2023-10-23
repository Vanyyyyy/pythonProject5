import sqlite3

def create_and_fill_tables_from_txt(file_path, table_name):
    # Подключаемся к базе данных
    conn = sqlite3.connect('mydatabase.db') # Создает базу данных mydatabase.db, если она не существует
    cursor = conn.cursor()

    # Создаем таблицу
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name} (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        age INTEGER
                        )''')

    # Открываем файл .txt и считываем данные
    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            name, age = data[0], int(data[1])
            cursor.execute(f"INSERT INTO {table_name} (name, age) VALUES (?, ?)", (name, age))

    # Сохраняем изменения
    conn.commit()
    cursor.execute('''select * from mytable''')
    # Закрываем соединение
    conn.close()

# Использование функции
file_path = 'C:\\Users\\Student\\PycharmProjects\\pythonProject5\\mytable.txt' # Укажите путь к вашему файлу .txt
table_name = 'mytable' # Укажите имя таблицы
create_and_fill_tables_from_txt(file_path, table_name)
