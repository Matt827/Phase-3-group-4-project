from __init__ import CURSOR, CONN

class Item:
    
    all = []

    def __init__(self, name, item_type, description, damage, defense, potion, cost):
        self.name = name
        self.item_type = item_type
        self.description = description
        self.damage = damage
        self.defense = defense
        self.potion = potion
        self.cost = cost

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS items (
            ItemId INTEGER PRIMARY KEY,
            ShopsId INTEGER,
            name TEXT,
            type TEXT,
            description TEXT,
            damage INTEGER,
            defense INTEGER,
            potion INTEGER,
            cost INTEGER,
            FOREIGN KEY (ShopsId) REFERENCES shop(ShopId)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS items;
        """

        CURSOR.execute(sql)
        CONN.commit()


    def save(self):
        sql = """
            INSERT INTO items (name, ShopsId, type, description, damage, defense, potion, cost)
            VALUES(?,?, ?, ?, ?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, 1, self.item_type, self.description, self.damage, self.defense, self.potion, self.cost))
        CONN.commit()
        self.id = CURSOR.lastrowid
