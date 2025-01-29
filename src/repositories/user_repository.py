from src.database import DatabaseConnection

class UserRepository:
    def __init__(self, connection=None):
        self.connection = connection if connection else DatabaseConnection().get_connection()

    def add_user(self, username, password, role):
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)"
            cursor.execute(sql, (username, password, role))
            self.connection.commit()

    def find_user(self, username, password):
        with self.connection.cursor() as cursor:
            sql = "SELECT username, role FROM users WHERE username=%s AND password=%s"
            cursor.execute(sql, (username, password))
            return cursor.fetchone()

    def find_user_by_username(self, username):
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM users WHERE username=%s"
            cursor.execute(sql, (username,))
            return cursor.fetchone()
