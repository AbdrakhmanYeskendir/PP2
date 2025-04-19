import psycopg2
import csv
import os

# -*- coding: utf-8 -*-

conn = psycopg2.connect(
    host='localhost',
    database='eska',
    user='postgres',
    password='123'
)
cursor = conn.cursor()

def new_column():
    add_column_query = """
    ALTER TABLE phone
    ADD COLUMN IF NOT EXISTS user_c SERIAL;
    """
    cursor.execute(add_column_query)
    conn.commit()
    print("Столбец 'user_c' успешно добавлен в таблицу 'phone'.")

def insert_name(user_name, score):
    try:
        insert_query = """
        INSERT INTO phone (user_name, score) 
        VALUES (%s, %s) RETURNING user_id, user_name, score;
        """
        cursor.execute(insert_query, (user_name, score))
        conn.commit()
        user_data = cursor.fetchone()
        print(f"Пользователь добавлен: ID = {user_data[0]}, Имя = {user_data[1]}, Баллы = {user_data[2]}")
        return user_data[0]
    except Exception as e:
        print("Ошибка при добавлении пользователя:", e)
        conn.rollback()
        return None

def update(num, val1, val2):
    try:
        if num == 1:
            update_query = """
                UPDATE phone
                SET score = %s
                WHERE user_name = %s
                RETURNING user_id, user_name, score;
                """
        elif num == 2:
            update_query = """
                UPDATE phone
                SET user_name = %s
                WHERE score = %s
                RETURNING user_id, user_name, score;
                """
        cursor.execute(update_query, (val1, val2))
        conn.commit()
        user_data = cursor.fetchone()
        if user_data:
            print(f"Данные обновлены: ID = {user_data[0]}, Имя = {user_data[1]}, Баллы = {user_data[2]}")
        else:
            print("Запись не найдена.")
    except Exception as e:
        print("Ошибка при обновлении:", e)
        conn.rollback()

def delete_user(user_name):   
    try:
        delete_query = """
        DELETE FROM phone
        WHERE user_name = %s
        RETURNING user_id, user_name;
        """
        cursor.execute(delete_query, (user_name,))
        conn.commit()
        user_data = cursor.fetchone()
        if user_data:
            print(f"Пользователь удален: ID = {user_data[0]}, Имя = {user_data[1]}")
        else:
            print("Пользователь не найден.")
    except Exception as e:
        print("Ошибка при удалении:", e)
        conn.rollback()

def get_all_users():
    cursor.execute("SELECT user_id, user_name, score FROM phone;")
    rows = cursor.fetchall()
    print("Все пользователи:")
    for row in rows:
        print(f"ID: {row[0]}, Имя: {row[1]}, Баллы: {row[2]}")

def list_to_CSV():
    cursor.execute("SELECT user_id, user_name, score FROM phone ORDER BY score DESC;")
    rows = cursor.fetchall()
    with open('users.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["user_id", "user_name", "score"])
        writer.writerows(rows)
    print("Данные экспортированы в users.csv")

def get_users_sorted_by_score():
    cursor.execute("SELECT user_id, user_name, score FROM phone ORDER BY score DESC;")
    rows = cursor.fetchall()
    print("Пользователи по убыванию баллов:")
    for row in rows:
        print(f"ID: {row[0]}, Имя: {row[1]}, Баллы: {row[2]}")

def import_from_csv():
    file_path = input("Введите путь к CSV файлу: ").strip()
    if not os.path.isfile(file_path):
        print("Файл не найден.")
        return
    try:
        with open(file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                user_name = row['user_name']
                score = int(row['score'])
                insert_name(user_name, score)
        print("Импорт завершен.")
    except Exception as e:
        print("Ошибка при импорте из CSV:", e)

if __name__ == '__main__':
    operation = input(
        "Выберите операцию:\n"
        "1 - Добавить пользователя\n"
        "2 - Обновить пользователя\n"
        "3 - Удалить пользователя\n"
        "4 - Показать всех пользователей\n"
        "5 - Показать пользователей по убыванию баллов\n"
        "6 - Экспортировать в CSV\n"
        "7 - Добавить новый столбец\n"
        "8 - Импортировать из CSV\n"
        ">>> "
    )

    if operation == "1":
        count = int(input("Сколько пользователей вы хотите добавить? "))
        for i in range(count):
            print(f"\nПользователь {i+1}:")
            name = input("  Введите имя: ")
            score = int(input("  Введите баллы: "))
            insert_name(name, score)

    elif operation == "2":
        num = int(input("1 - изменить баллы по имени\n2 - изменить имя по баллам\n>>> "))
        if num == 1:
            name = input("Введите имя: ")
            score = int(input("Введите новые баллы: "))
            update(num, score, name)
        elif num == 2:
            score = int(input("Введите баллы: "))
            name = input("Введите новое имя: ")
            update(num, name, score)
    elif operation == "3":
        name = input("Введите имя для удаления: ")
        delete_user(name)
    elif operation == "4":
        get_all_users()
    elif operation == "5":
        get_users_sorted_by_score()
    elif operation == "6":
        list_to_CSV()
    elif operation == "7":
        new_column()
    elif operation == "8":
        import_from_csv()
    else:
        print("Неверный выбор.")

    cursor.close()
    conn.close()
