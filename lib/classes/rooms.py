
class Room:

    def __init__(self, name, description, monster, shop, gold):
        self.name = name
        self.description = description
        self.monster = monster
        self.shop = shop
        self.gold = gold

    dict = {
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

        