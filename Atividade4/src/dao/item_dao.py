import sqlite3
from src.models.item import Item

# Nome: Johannes Mattheus Krouwel   RA: 20.01248-9

class ItemDAO:

    _instance = None

    def __init__(self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = ItemDAO()
        return cls._instance

    def _connect(self):
        self.conn = sqlite3.connect('./databases/sqlite.db')

    def get_all(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Itens;
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(Item(id=resultado[0], nome=resultado[1], preco=resultado[2], link=resultado[3]))
        self.cursor.close()
        return resultados
    
    def inserir_item(self, item):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            INSERT INTO Itens (
                id, 
                nome, 
                preco,
                link)
            VALUES(
                '{item.id}','{item.nome}','{item.preco}','{item.link}');
        """)
        self.conn.commit()
        self.cursor.close()

    def pegar_item(self, id):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Itens
            WHERE id = '{id}';
        """)
        item = None
        resultado = self.cursor.fetchone()
        if resultado != None:
            item = Item(id=resultado[0], nome=resultado[1], preco=resultado[2], link=resultado[3])
        self.cursor.close()
        return 
        
    def pegar_id(self, id):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Itens
            WHERE id = '{id}';
        """)
        id = None
        resultado = self.cursor.fetchone()
        if resultado != None:
            id = Item(id=resultado[0])
        self.cursor.close()
        return id

    def pegar_nome(self, id):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Itens
            WHERE id = '{id}';
        """)
        nome = None
        resultado = self.cursor.fetchone()
        if resultado != None:
            nome = Item(nome=resultado[1])
        self.cursor.close()
        return nome

    def pegar_preco(self, id):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Itens
            WHERE id = '{id}';
        """)
        preco = None
        resultado = self.cursor.fetchone()
        if resultado != None:
            preco = Item(preco=resultado[2])
        self.cursor.close()
        return preco

    def pegar_link(self, id):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Itens
            WHERE id = '{id}';
        """)
        link = None
        resultado = self.cursor.fetchone()
        if resultado != None:
            link = Item(link=resultado[3])
        self.cursor.close()
        return link

    def atualizar_item(self, item):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                UPDATE Itens SET
                nome = '{item.nome}',
                preco = {item.preco}
                link = '{item.link}'
                WHERE id = '{item.id}'
            """)
        except:
            return False
        return True

    def search_all_for_name(self, nome):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Itens
            WHERE nome LIKE '{nome}%';
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(Item(id=resultado[0], nome=resultado[1], preco=resultado[2], link=resultado[3]))
        self.cursor.close()
        return resultados