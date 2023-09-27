from __init__ import CONN, CURSOR

class Monster:
    def __init__(self, name, gold, health, attack, speed, drops):
        self.name = name
        self.gold = gold
        self.health = health
        self.hp = health
        self.attack = attack
        self.speed = speed
        self.drops = drops
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS monsters (
            MonsterId INTEGER PRIMARY KEY,
            name TEXT,
            gold INTEGER,
            health INTEGER,
            attack INTEGER,
            speed INTEGER
            )
        """
        
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS monsters;
        """

        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO monsters (name, gold, health, attack, speed)
            VALUES(?, ?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.gold, self.health, self.attack, self.speed))
        CONN.commit()
        self.id = CURSOR.lastrowid
    
        
    def take_damage(self, damage):
        self.hp -= damage