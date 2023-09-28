from __init__ import CURSOR, CONN

class Room:

    def __init__(self, name, description, monster, shop, gold):
        self.name = name
        self.description = description
        self.monster = monster
        self.shop = shop
        self.gold = gold
        self.save()

        self.dict = {
            "up": None,
            "down": None,
            "left": None,
            "right": None
        }

    def room_directions(self, room_up, room_down, room_left, room_right):
        self.dict["up"] = room_up
        self.dict["down"] = room_down
        self.dict["left"] = room_left
        self.dict["right"] = room_right
        
    def display_info(self):
        print(f'''
    location: {self.name}
    monster: {self.monster.name if self.monster != None else None}
    shop: {True if self.shop != None else False}
    gold: {self.gold}
              ''')
        
    # SQL METHODS
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS rooms (
                room_id INTEGER PRIMARY KEY,
                name TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS rooms;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO rooms (name) VALUES (?)
        """

        CURSOR.execute(sql, (self.name, ))
        CONN.commit()
        
    
    