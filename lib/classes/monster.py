
class Monster:
    def __init__(self, name, gold, health, attack, speed, drops):
        self.name = name
        self.gold = gold
        self.health = health
        self.hp = health
        self.attack = attack
        self.speed = speed
        self.drops = drops
        
    def take_damage(self, damage):
        self.hp -= damage