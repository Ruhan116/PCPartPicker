import sqlite3
from hashlib import sha256

class UserModel:
    def __init__(self, db_path='data/database/database.sqlite'):
        # Connect to the SQLite database
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        # Create the users table if it doesn't exist
        query = '''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def hash_password(self, password):
        return sha256(password.encode()).hexdigest()

    def create_user(self, username, email, password):
        # Create a new user in the database
        try:
            hashed_password = self.hash_password(password)
            query = '''
            INSERT INTO users (username, email, password)
            VALUES (?, ?, ?)
            '''
            self.conn.execute(query, (username, email, hashed_password))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            # If username or email already exists
            return False

    def verify_user(self, username, password):
        hashed_password = self.hash_password(password)
        query = '''
        SELECT * FROM users WHERE username = ? AND password = ?
        '''
        cursor = self.conn.execute(query, (username, hashed_password))
        return cursor.fetchone() is not None

    def get_user(self, username):
        query = '''
        SELECT * FROM users WHERE username = ?
        '''
        cursor = self.conn.execute(query, (username,))
        return cursor.fetchone()


