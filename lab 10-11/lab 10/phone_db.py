import psycopg2

conn = psycopg2.connect(
    host='localhost',
    database='eska',
    user='postgres',
    password='123'
)

cursor = conn.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS phone (
    user_id SERIAL PRIMARY KEY,
    user_name VARCHAR(100) NOT NULL,
    score INT DEFAULT 0
);
"""
cursor.execute(create_table_query)

conn.commit()

cursor.close()
conn.close()

print("Таблица 'phone' успешно создана!")