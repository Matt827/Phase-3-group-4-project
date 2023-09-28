from __init__ import CURSOR, CONN

class Item:
    
    all = []

    def __init__(self, name, item_type, description, damage, defense, potion, cost, monster_id, shop_id, id=None):
        self.name = name
        self.item_type = item_type
        self.description = description
        self.damage = damage
        self.defense = defense
        self.potion = potion
        self.cost = cost
        self.monster_id = monster_id
        self.shop_id = shop_id
        self.id = id

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS items (
            ItemId INTEGER PRIMARY KEY,
            ShopsId INTEGER,
            MonstersId INTEGER,
            name TEXT,
            type TEXT,
            description TEXT,
            damage INTEGER,
            defense INTEGER,
            potion INTEGER,
            cost INTEGER,
            FOREIGN KEY (ShopsId) REFERENCES shop(ShopId)
            FOREIGN KEY (MonstersId) REFERENCES monsters(MonsterId)
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
            INSERT INTO items (name, ShopsId, MonstersId type, description, damage, defense, potion, cost)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.shop_id, self.monster_id, self.item_type, self.description, self.damage, self.defense, self.potion, self.cost))
        CONN.commit()
        self.id = CURSOR.lastrowid

    # REMOVE ITEM FROM MONSTER
    def remove_item_monster(self, id):
        self.monster_id = None
        sql = """
            UPDATE items
            SET MonstersId = NULL
            WHERE id = ?;
        """
        CURSOR.execute(sql, (id, ))
        CONN.commit()

    # REMOVE ITEM FROM SHOP
    @classmethod
    def remove_item_shop(cls, id):
        sql = """
            DELETE FROM items
            WHERE id = ?
        """
        CURSOR.execute(sql, (id, ))
        CONN.commit()
    
    def add_item_shop(self):
        self.save()
    