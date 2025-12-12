import sqlite3
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def create_table(self):
        with self.connection:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER UNIQUE,
                    first_name TEXT,
                    last_name TEXT,
                    patronymic TEXT,
                    email TEXT,
                    phone TEXT,
                    city TEXT,
                    course TEXT,
                    reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            logger.info("Таблица users создана или уже существует")

    def user_exists(self, user_id):
        """Проверяет, существует ли пользователь в БД"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,)).fetchone()
            return result is not None

    def add_user(self, user_id, first_name, last_name, patronymic, email, phone, city, course):
        """Добавляет нового пользователя"""
        with self.connection:
            self.cursor.execute('''
                INSERT INTO users (user_id, first_name, last_name, patronymic, email, phone, city, course)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (user_id, first_name, last_name, patronymic, email, phone, city, course))
            self.connection.commit()
            logger.info(f"Добавлен новый пользователь: {first_name} {last_name} (ID: {user_id})")

    def get_user(self, user_id):
        """Получает данные пользователя"""
        with self.connection:
            return self.cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,)).fetchone()

    def close(self):
        """Закрывает соединение с БД"""
        self.connection.close()


# Функция для инициализации БД
def init_db():
    """Инициализирует базу данных"""
    db = Database('db.sqlite')
    db.create_table()
    db.close()
    print("✅ База данных инициализирована")


if __name__ == "__main__":
    init_db()
