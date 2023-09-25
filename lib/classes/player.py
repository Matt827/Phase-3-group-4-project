
class Player:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.defense = 0
        self.hp = self.health + self.defense
        self.attack = 5
        self.gold = 0
