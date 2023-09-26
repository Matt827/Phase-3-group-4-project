
class Player:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.defense = 0
        self.hp = self.health + self.defense
        self.attack = 5
        self.gold = 0

    def display_info(self):
        print(f'''
        name: {self.name}
        health: {self.health}
        defense: {self.defense}
        hp: {self.hp}
        attack: {self.attack}
        gold: {self.gold}
        ''')