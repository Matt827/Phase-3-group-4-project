
class Player:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.defense = 0
        self.hp = self.health + self.defense
        self.attack = 5
        self.gold = 1000
        self.inventory = []

    def display_info(self):
        print(f'''
        name: {self.name}
        health: {self.health}
        defense: {self.defense}
        hp: {self.hp}
        attack: {self.attack}
        gold: {self.gold}
        ''')
        
    def display_inventory(self):
        if len(self.inventory) == 0:
            print("nothing in inventory")
        else:
            for item in self.inventory:
                print(f"{item.item_type}: {item.name}")