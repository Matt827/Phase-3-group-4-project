
class Player:

    def __init__(self, name):
        self.name = name
        self.defense = 0
        self.hp = 100
        self.max_hp = 100
        self.attack = 5
        self.gold = 1000
        self.inventory = []
        self.armor = None
        self.weapon = None

    def display_info(self):
        print(f'''
        name: {self.name}
        hp: {self.hp} / {self.max_hp}
        defense: {self.defense}
        attack: {self.attack}
        gold: {self.gold}
        ''')
        
    def display_inventory(self):
        if len(self.inventory) == 0:
            print("nothing in inventory")
        else:
            for item in self.inventory:
                print(f"{item.item_type}: {item.name}")

    def display_equipment(self):
        print(f"WEAPON : {self.weapon.name}" if self.weapon != None else f"WEAPON : {self.weapon}")
        print(f"ARMOR : {self.armor.name}" if self.armor != None else f"ARMOR : {self.armor}")

    def take_damage(self, dmg):
        self.hp -= dmg