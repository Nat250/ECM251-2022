import sqlite3
from src.models.user import User

class UserDAO:

    _instance = None

    def __init__(self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = UserDAO()
        return cls._instance

    def _connect(self):
        self.conn = sqlite3.connect('./databases/sqlite.db')

    def get_all(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Users;
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(User(username=resultado[0], password=resultado[1], email=resultado[2]))
        self.cursor.close()
        return resultados
    
    def inserir_pedido(self, user):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            INSERT INTO Users (
                username,
                password,
                email)
            VALUES(
                '{user.username}',
                '{pedido.password}',
                '{pedido.email}'
            );
        """)
        self.conn.commit()
        self.cursor.close()

    def pegar_user(self, username):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Users
            WHERE username = '{username}';
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(User(username=resultado[0], password=resultado[1], email=resultado[2]))
        self.cursor.close()
        return resultados

    def atualizar_pedido(self, user):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                UPDATE Users SET
                username = '{user.username}',
                password = {user.password},
                email = '{user.email}'
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True

    def search_all_for_name(self, username):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Users
            WHERE username LIKE '{username}%';
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(User(username=resultado[0], password=resultado[1], email=resultado[2]))
        self.cursor.close()
        return resultados