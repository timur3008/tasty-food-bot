import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

class DatabaseConnection:
    def __init__(self):
        self.connection, self.cursor = self.connect()

    def connect(self) -> tuple:
        connection = psycopg2.connect(host=DB_HOST, user=DB_USER, database=DB_NAME, password=DB_PASSWORD)
        cursor = connection.cursor()
        return connection, cursor
    
class DatabaseTables(DatabaseConnection):
    def __init__(self):
        super().__init__()

    def create_tables(self) -> None:
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
                chat_id BIGINT UNIQUE
            );
            
            CREATE TABLE IF NOT EXISTS purchases(
                id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
                name TEXT,
                price INTEGER,
                image TEXT,
                user_id INTEGER REFERENCES users(id)               
            );
                            
            CREATE TABLE IF NOT EXISTS history(
                id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
                name TEXT,
                price INTEGER,
                image TEXT,
                user_id INTEGER REFERENCES users(id) 
            );
        ''')
        self.connection.commit()

db_tables = DatabaseTables()

class User(DatabaseTables):
    def __init__(self):
        super().__init__()

    def get_user(self, chat_id: int) -> tuple:
        self.cursor.execute('SELECT id FROM users WHERE chat_id = %s;', (chat_id,))
        self.connection.commit()
        return self.cursor.fetchone()
    
    def add_user(self, chat_id: int) -> None:
        self.cursor.execute('INSERT INTO users(chat_id) VALUES (%s);', (chat_id,))

class Purchase(DatabaseTables):
    def __init__(self):
        super().__init__()

    def add_product(self, name: str, price: int, image: str, chat_id: int) -> None:
        user_id = users_repo.get_user(chat_id=chat_id)[0]
        query = 'INSERT INTO purchases(name, price, image, user_id) VALUES (%s, %s, %s, %s);'
        self.cursor.execute(query, (name, price, image, user_id))
        self.connection.commit()
        print('successfully added')

    def get_products(self, chat_id: int) -> list[tuple]:
        user_id = users_repo.get_user(chat_id=chat_id)
        self.cursor.execute('SELECT id, name, price, image FROM purchases WHERE user_id = %s;', (user_id,))
        self.connection.commit()
        return self.cursor.fetchall()
    
    def delete_one_product(self, chat_id: int, id: int) -> None:
        user_id = users_repo.get_user(chat_id=chat_id)
        self.cursor.execute('DELETE FROM purchases WHERE user_id = %s AND id = %s;', (user_id, id))
        self.connection.commit()
    
    def delete_products(self, chat_id: int) -> None:
        user_id = users_repo.get_user(chat_id=chat_id)
        self.cursor.execute('DELETE FROM purchases WHERE user_id = %s;', (user_id))
        self.connection.commit()

    def add_to_history(self, name: str, price: int, image: str, chat_id: int) -> None:
        user_id = users_repo.get_user(chat_id=chat_id)
        self.cursor.execute(
            'INSERT INTO history(name, price, image, user_id) VALUES (%s, %s, %s, %s);', 
            (name, price, image, user_id)
        )
        self.connection.commit()

    def get_history(self, chat_id: int) -> list[tuple]:
        user_id = users_repo.get_user(chat_id=chat_id)
        self.cursor.execute('SELECT name, price, image FROM history WHERE user_id = %s;', (user_id,))
        self.connection.commit()
        return self.cursor.fetchall()

users_repo = User()
purchases_repo = Purchase()