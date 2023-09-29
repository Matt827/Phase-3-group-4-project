from __init__ import CURSOR, CONN

class Shop:
    def __init__(self, name, id, items=[]):
        self.name = name
        self.id = id
        self.items = items
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS shop (
            ShopId INTEGER PRIMARY KEY,
            name TEXT
            )
        """

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS shop;
        """

        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        

        CURSOR.execute('INSERT INTO shop (name) VALUES (?);', (self.name,))
        CONN.commit()
        self.id = CURSOR.lastrowid