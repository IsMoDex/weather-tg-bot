import sqlite3
from datetime import datetime
from config import DATABASE_PATH

# Подключение к базе
conn = sqlite3.connect(DATABASE_PATH, check_same_thread=False)
cursor = conn.cursor()

# Создание таблиц, если не существуют
def init_db():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            command TEXT,
            response TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subscriptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            city TEXT
        )
    ''')
    conn.commit()

# Добавить лог
def log_request(user_id: int, command: str, response: str):
    cursor.execute('''
        INSERT INTO logs (user_id, command, response)
        VALUES (?, ?, ?)
    ''', (user_id, command, response))
    conn.commit()

# Добавить подписку
def add_subscription(user_id: int, city: str):
    # Удалим дубликаты (на случай повторных подписок)
    cursor.execute('DELETE FROM subscriptions WHERE user_id = ?', (user_id,))
    cursor.execute('''
        INSERT INTO subscriptions (user_id, city)
        VALUES (?, ?)
    ''', (user_id, city))
    conn.commit()

# Получить все подписки
def get_all_subscriptions():
    cursor.execute('SELECT user_id, city FROM subscriptions')
    return cursor.fetchall()

# Проверить подписку конкретного пользователя
def get_user_subscription(user_id: int):
    cursor.execute('SELECT city FROM subscriptions WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()
    return result[0] if result else None

# Удалить подписку
def remove_subscription(user_id: int):
    cursor.execute('DELETE FROM subscriptions WHERE user_id = ?', (user_id,))
    conn.commit()
