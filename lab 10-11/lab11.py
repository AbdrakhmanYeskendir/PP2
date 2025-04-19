# -*- coding: utf-8 -*-
import psycopg2

# Подключение к базе данных
conn = psycopg2.connect(
    host='localhost',
    database='suppliers',
    user='postgres',
    password='123'
)
cursor = conn.cursor()

# Добавить или обновить одного пользователя
def insert_or_update_user(name, phone_number):
    if not phone_number.isdigit() or len(phone_number) > 10:
        print(f" Некорректный номер телефона: {phone_number}")
        return

    cursor.execute("SELECT COUNT(*) FROM phone WHERE user_name = %s", (name,))
    count = cursor.fetchone()[0]

    if count > 0:
        cursor.execute("UPDATE phone SET score = %s WHERE user_name = %s", (phone_number, name))
        print(f" Контакт {name} обновлён.")
    else:
        cursor.execute("INSERT INTO phone (user_name, score) VALUES (%s, %s)", (name, phone_number))
        print(f" Контакт {name} добавлен.")

    conn.commit()

# Массовое добавление/обновление пользователей
def insert_multiple_users(data_list):
    for name, phone_number in data_list:
        if not phone_number.isdigit():
            print(f" Некорректный номер телефона: {phone_number} для {name}")
            continue

        cursor.execute("SELECT COUNT(*) FROM phone WHERE user_name = %s", (name,))
        count = cursor.fetchone()[0]

        if count > 0:
            cursor.execute("UPDATE phone SET score = %s WHERE user_name = %s", (phone_number, name))
        else:
            cursor.execute("INSERT INTO phone (user_name, score) VALUES (%s, %s)", (name, phone_number))

    conn.commit()
    print(" Контакты добавлены или обновлены.")

# Поиск по шаблону
def collecting_info_by_pattern(pattern):
    pattern_like = f"%{pattern}%"
    cursor.execute(
        "SELECT user_id, user_name, score FROM phone WHERE user_name LIKE %s OR score::TEXT LIKE %s ORDER BY user_id",
        (pattern_like, pattern_like)
    )
    rows = cursor.fetchall()
    print(f"\n🔍 Найдено записей: {len(rows)}")
    for row in rows:
        print(f"ID: {row[0]}, Имя: {row[1]}, Телефон: {row[2]}")

# Пагинация
def collecting_info_with_pagination(limit, offset):
    cursor.execute("SELECT user_id, user_name, score FROM phone ORDER BY user_id LIMIT %s OFFSET %s", (limit, offset))
    rows = cursor.fetchall()
    print(f"\n Найдено записей: {len(rows)}")
    for row in rows:
        print(f"ID: {row[0]}, Имя: {row[1]}, Телефон: {row[2]}")

# Удаление по имени
def delete_user_by_name(name):
    cursor.execute("DELETE FROM phone WHERE user_name = %s RETURNING user_id;", (name,))
    deleted = cursor.fetchone()
    conn.commit()
    if deleted:
        print(f"🗑 Контакт {name} удалён.")
    else:
        print(" Контакт не найден.")

# Удаление по телефону
def delete_user_by_phone(phone_number):
    cursor.execute("DELETE FROM phone WHERE score = %s RETURNING user_id;", (phone_number,))
    deleted = cursor.fetchone()
    conn.commit()
    if deleted:
        print(f"🗑 Контакт с номером {phone_number} удалён.")
    else:
        print(" Контакт не найден.")

# Меню операций
if __name__ == '__main__':
    try:
        print("\n📱 Меню:")
        print("1 - Добавить/обновить контакт")
        print("2 - Поиск")
        print("3 - Удалить")
        print("4 - Добавить несколько")
        print("5 - Пагинация")

        op = input("Выберите операцию: ").strip()

        if op == "1":
            name = input("Имя: ").strip()
            phone = input("Телефон (11 цифр): ").strip()
            insert_or_update_user(name, phone)

        elif op == "2":
            pattern = input("Введите часть имени или номера: ").strip()
            collecting_info_by_pattern(pattern)

        elif op == "3":
            mode = input("Удалить по:\n1 - Имени\n2 - Телефону\nВыбор: ").strip()
            if mode == "1":
                name = input("Имя: ").strip()
                delete_user_by_name(name)
            elif mode == "2":
                phone = input("Телефон: ").strip()
                delete_user_by_phone(phone)

        elif op == "4":
            count = int(input("Сколько контактов добавить: "))
            contacts = []
            for _ in range(count):
                name = input("Имя: ").strip()
                phone = input("Телефон: ").strip()
                contacts.append((name, phone))
            insert_multiple_users(contacts)

        elif op == "5":
            limit = int(input("Сколько записей показать: "))
            offset = int(input("Сколько пропустить: "))
            collecting_info_with_pagination(limit, offset)

        else:
            print(" Неверная операция.")

    except Exception as e:
        print(" Ошибка выполнения:", e)

    finally:
        cursor.close()
        conn.close()
        print("🔚 Завершено. Соединение с базой закрыто.")
