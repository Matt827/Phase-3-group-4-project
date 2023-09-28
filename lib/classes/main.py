import pyfiglet
from termcolor import cprint

from player import Player
from rooms import Room
from item import Item
from monster import Monster
from shop import Shop
from __init__ import CONN, CURSOR
from avatars import *



 # WEAPONS
excalibur = Item("Excalibur", "WEAPON", "Legendary Sword", 10, 0, 0, 15, 1, 1, 1)
mjolnir = Item("Mjolnir", "WEAPON", "Thunderous Hammer", 20, 0, 0, 25, 8, 1, 1)
dragonbone_bow = Item("Dragonbone Bow", "WEAPON", "Wyrmstring Bow", 27, 0, 0, 32, 10, 1, 1)
shadowblade = Item("Shadow Blade", "WEAPON", "Stealthy Dagger", 15, 0, 0, 20, 6, 1, 1)
soul_reaver = Item("Soul Reaver", "WEAPON", "Cursed Sword", 30, 0, 0, 35, 13, 1, 1)
moonlit_dagger = Item("Moonlit Dagger", "WEAPON", "Silvered Blade", 13, 0, 0, 17, 4, 1, 1)
serpents_fang = Item("Serpent's Fang", "WEAPON", "Venomous Whip", 16, 0, 0, 21, 7, 1, 1)
stormcaller = Item("Stormcaller", "WEAPON", "Lightning Sword", 27, 0, 0, 32, 12, 1, 1)
dwarven_crossbow = Item("Dwarven Crossbow", "WEAPON", "Stour Crossbow", 12, 0, 0, 17, 3, 1, 1)
warhammer_of_the_titans = Item("Warhammer of the Titans", "WEAPON", "Colossal Warhammer", 35, 0, 0, 40, 16, 1, 1)

# ARMOR
knight_armor_set = Item("Knights Armor Set", "ARMOR", "Flexible Defense", 0, 25, 0, 35, 2, 1, 1)
noble_lord_armor_set = Item("Noble Lord Armor Set", "ARMOR", "Agile Ward", 0, 50, 0, 60, 5, 1, 1)
commander_armor_set = Item("Commander Armor Set", "ARMOR", "Heavy Protection", 0, 75, 0, 85, 11, 1, 1)
king_armor_set = Item("King Armor Set", "ARMOR", "Dragon Scales", 0, 100, 0, 110, 17, 1, 1)

# POTION
health_potion1 = Item("Vitality Elixir", "POTION", "Increase max health by 25", 0, 0, 25, 50, 9, 1, 1)
health_potion2 = Item("Health Elixir", "POTION", "Increase max health by 50", 0, 0, 50, 100, 14, 1, 1)
health_potion3 = Item("Life Elixir", "POTION", "Increase max health by 75", 0, 0, 75, 150, 15, 1, 1)
health_potion4 = Item("Eternal Elixir", "POTION", "Increase max health by 100", 0, 0, 100, 200, 18, 1, 1)


shop1 = Shop("Store", [excalibur, mjolnir, dragonbone_bow, shadowblade, soul_reaver, moonlit_dagger, serpents_fang, stormcaller, dwarven_crossbow, warhammer_of_the_titans, knight_armor_set, noble_lord_armor_set, commander_armor_set, king_armor_set, health_potion1, health_potion2, health_potion3, health_potion4])


# SQL COMMANDS
Room.drop_table()
Room.create_table()

Shop.drop_table()
Shop.create_table()
shop1.save()

Monster.drop_table()
Monster.create_table()

Item.drop_table()
Item.create_table()
excalibur.save()
mjolnir.save()
dragonbone_bow.save()
shadowblade.save()
soul_reaver.save()
moonlit_dagger.save()
serpents_fang.save()
stormcaller.save()
dwarven_crossbow.save()
warhammer_of_the_titans.save()

# ARMOR
knight_armor_set.save()
noble_lord_armor_set.save()
commander_armor_set.save()
king_armor_set.save()

# POTION
health_potion1.save()
health_potion2.save()
health_potion3.save()
health_potion4.save()

# LOCATIONS
moonshadow_grove = Room('Moonshadow Grove', 'Moonshadow Grove, a mystical forest bathed in the silvery glow of the moon, where ancient, luminescent flora and fauna thrive, and whispers of forgotten enchantments linger in the cool night air.', None, shop1, 25)
whispering_woods = Room('Whispering Woods', 'Whispering Woods, a serene woodland sanctuary where the leaves rustle with secrets, and ancient trees seem to murmur tales of forgotten magic, offering solace to those who seek its tranquil embrace.', None, None, 25)
eldemoor_forest = Room('Eldemoor Forest', 'Eldemoor Forest, an ethereal realm where ancient trees reach for the sky, their trunks adorned with bioluminescent flora that illuminate the forest floor, casting a surreal, enchanting glow over the moss-covered ground.', None, shop1, 25)
frostfall_glacier = Room('Frostfall Glacier', 'Frostfall Glacier stretches as far as the eye can see, a vast expanse of shimmering ice and snow beneath the towering peaks, where the air is crisp with the promise of adventure and every step echoes in the serene, frozen stillness.', None, None, 25)
silverstrand_beach = Room('Silverstrand Beach', 'Silverstrand Beach is a pristine coastal paradise, where fine, silvery sands stretch alongside crystalline waters, kissed by the gentle caress of a perpetual sunset, creating a timeless haven of tranquility and beauty.', None, shop1, 25)
moonlit_cove = Room('Moonlit Cove', 'Moonlit Cove is a secluded bay nestled between rugged cliffs, its tranquil waters reflecting the silvery glow of the moon, while ancient, luminescent flora line the shore, casting an otherworldly aura over this hidden sanctuary.', None, shop1, 25)
misthaven_vale = Room('Misthaven Vale', 'Misthaven Vale is a mystical highland shrouded in perpetual mist, where emerald forests and cascading waterfalls converge, and the air is alive with the soft hum of ancient enchantments, creating an ethereal realm untouched by time.', None,None, 25)
glade_grasslands = Room('Glade Grasslands', 'Glade Grasslands unfurl as an endless expanse of rolling meadows, their emerald blades swaying in harmonious rhythm with the breeze, where wildflowers bloom in a symphony of color, inviting wanderers to bask in the serenity of natures embrace.', None, None, 25)
avalon = Room('Avalon', "Mythical island of legend", None, shop1, 25)
luminara_falls = Room('Luminara Falls', 'Luminara Falls cascades down a majestic cliffside, its crystalline waters refracting the sunlight into a kaleidoscope of colors, while ethereal wisps of mist dance around the falls, creating a breathtaking, almost otherworldly spectacle.', None, shop1, 25)
mistral_bay = Room('Mistral Bay', 'Mistral Bay is a picturesque coastal retreat where azure waves gently lap against the shore, kissed by the refreshing caress of a perpetual sea breeze, while rugged cliffs and lush vegetation frame this idyllic sanctuary.', None, shop1, 25)
thunderpeak_summit = Room('Thunderpeak Summit', 'Thunderpeak Summit looms as the highest pinnacle in a range of ancient, mist-shrouded mountains, its jagged spires seeming to touch the very heavens, where thunderstorms and crackling energy fill the air with an electric charge, creating an awe-inspiring yet perilous realm.', None, shop1, 25)
shadowfen_swamp = Room('Shadowfen Swamp', 'Shadowfen Swamp sprawls in mysterious gloom, its tangled, moss-draped trees and murky waters shrouded in a perpetual twilight, where haunting cries of unseen creatures echo through the mist, and twisted roots conceal secrets of ages past.', None, None, 25)
shadow_peak = Room('Shadow Peak', 'Shadow Peak stands as a towering monolith amidst a desolate, moonlit wasteland, its jagged spires casting long, eerie silhouettes across the barren expanse, where the air is heavy with an unsettling stillness, harboring the whispers of forgotten legends.', None, shop1, 25)
crimsonreach_fortress = Room('Crimsonreach Fortress', 'Crimsonreach Fortress is a formidable citadel perched atop a blood-red cliff, its dark, stone walls looming over turbulent seas, while fiery torches light the way through labyrinthine corridors echoing with the history of battles long past.', None, shop1, 25)
phoenixreach_city = Room('Pheonixreach City', 'Phoenixreach City sprawls as a bustling metropolis of gleaming spires and arched bridges, its streets alive with a vibrant tapestry of cultures, where the air hums with the energy of innovation and the spirit of rebirth.', None, None, 25)
serpents_labrynth = Room("Serpent's Labrynth", 'Serpents Labyrinth winds through an ancient subterranean maze, its shadowy passages illuminated by bioluminescent flora, where the hiss of unseen creatures and the echo of forgotten whispers create an eerie, enigmatic atmosphere.', None, shop1, 25)
obsidian_abyss = Room('Obsidian Abyss', 'Obsidian Abyss plunges into the depths of the earth, a chasm of smooth, jet-black stone walls that seem to absorb all light, where the air is heavy with a sense of ancient, foreboding power.', None, shop1, 25)
wyvern_lair = Room('Wyvern Lair', 'Wynvern Lair is a hidden sanctuary nestled within the craggy heart of a mist-shrouded mountain, its caverns adorned with glistening crystals and echoing with the occasional stirring of slumbering wyverns, guarding their ancient treasures.', None, shop1, 25)
zukos_stronghold = Room("Zuko's Stronghold", 'Zukos Stronghold, hewn from the living rock of a volcanic peak, stands as a formidable bastion overlooking a fiery landscape, where molten streams cascade down the slopes, and the air resonates with the presence of the majestic dragon, Zuko, guardian of this fiery domain.', None, None, 25)

phoenixreach_city.room_directions(shadow_peak, obsidian_abyss, crimsonreach_fortress, serpents_labrynth)
moonshadow_grove.room_directions(misthaven_vale, shadow_peak, thunderpeak_summit, shadowfen_swamp)
misthaven_vale.room_directions(eldemoor_forest, moonshadow_grove, moonlit_cove, glade_grasslands)
whispering_woods.room_directions(None, moonlit_cove, None, eldemoor_forest)
eldemoor_forest.room_directions(None, misthaven_vale, whispering_woods, frostfall_glacier)
frostfall_glacier.room_directions(None, None, eldemoor_forest, None)
silverstrand_beach.room_directions(None, mistral_bay, None, moonlit_cove)
moonlit_cove.room_directions(whispering_woods, thunderpeak_summit, silverstrand_beach, misthaven_vale)
glade_grasslands.room_directions(None, shadowfen_swamp, misthaven_vale, luminara_falls)
avalon.room_directions(thunderpeak_summit, crimsonreach_fortress, None, None)
luminara_falls.room_directions(None, None, glade_grasslands, None)
mistral_bay.room_directions(silverstrand_beach, None, None, None)
thunderpeak_summit.room_directions(moonlit_cove, avalon, None, moonshadow_grove)
shadowfen_swamp.room_directions(glade_grasslands, None, moonshadow_grove, None)
shadow_peak.room_directions(moonshadow_grove, phoenixreach_city, None, None)
crimsonreach_fortress.room_directions(avalon, None, None, phoenixreach_city)
serpents_labrynth.room_directions(None, wyvern_lair, phoenixreach_city, None)
obsidian_abyss.room_directions(phoenixreach_city, None, None, wyvern_lair)
wyvern_lair.room_directions(serpents_labrynth, None, obsidian_abyss, zukos_stronghold)
zukos_stronghold.room_directions(None, None, wyvern_lair, None)

# Current room player is in and Previous room player was in
current_room = misthaven_vale
prev_room = None

# Main function houses majority of game functionality
def main():
    
    # Game Introduction
    name = input("What is your name, hero? ")
    result = pyfiglet.figlet_format(f"Adventures of {name}")

    cprint(result, "red")
    player = Player(name)
    cprint(f'''
Once upon a time, in the mystical realm of Eldoria, there was a fallen king named {player.name}. 
He had once ruled over a prosperous kingdom, but his reign had been marred by a black dragon. 
The Black Dragon took control of the entire kingdom and took his people into captivity. 
He must now adventure through the land of Elda, battling monsters and foes, and eventually defeating the Black Dragon, Zuko to free his people and reclaim his kingdom.
''', 'yellow')
    

    # MONSTERS
    ghost1 = Monster("Malevolent Ghost", 25, 30, 5, 40, [excalibur], 1, ghost_1_avatar)
    ghost2 = Monster("Sinister Ghost", 25, 30, 5, 40, [knight_armor_set], 3, ghost_2_avatar)
    ghost3 = Monster("Wicked Ghost", 25, 30, 5, 40, [dwarven_crossbow], 2, ghost_3_avatar)
    troll1 = Monster("Ruthless Troll", 18, 45, 10, 15, [moonlit_dagger], 4, troll_1_avatar)
    troll2 = Monster("Malignant Troll", 18, 45, 10, 15, [noble_lord_armor_set], 6, troll_2_avatar)
    troll3 = Monster("Nefarious Troll", 18, 45, 10, 15, [shadowblade], 8, troll_3_avatar)
    vampire1 = Monster("Malefic Vampire", 40, 60, 15, 28, [serpents_fang], 12, vampire_1_avatar)
    vampire2 = Monster("Twisted Vampire", 40, 60, 15, 28, [mjolnir], 10, vampire_2_avatar)
    vampire3 = Monster("Sinister Vampire", 40, 60, 15, 28, [health_potion1], 13, vampire_3_avatar)
    werewolf1 = Monster("Malefic Werewolf", 30, 75, 20, 22, [dragonbone_bow], 5, werewolf_1_avatar)
    werewolf2 = Monster("Diabolical Werewolf", 30, 75, 20, 22, [commander_armor_set], 14, werewolf_2_avatar)
    werewolf3 = Monster("Dark Werewolf", 30, 75, 20, 22, [stormcaller], 9, werewolf_3_avatar)
    demon1 = Monster("Demonic Demon", 45, 90, 25, 15, [soul_reaver], 11, demon_1_avatar)
    demon2 = Monster("Cursed Demon", 45, 90, 25, 15, [health_potion2], 15, demon_2_avatar)
    demon3 = Monster("Corrupt Demon", 45, 90, 25, 15, [health_potion3], 16, demon_3_avatar)
    dragon1 = Monster("Zephyrion", 100, 200, 20, 30, [warhammer_of_the_titans], 17, dragon_1_avatar)
    dragon2 = Monster("Celestiax", 100, 200, 20, 30, [king_armor_set], 18, dragon_2_avatar)
    dragon3 = Monster("Zuko", 100, 200, 30, 30, [health_potion4], 20, dragon_3_avatar)

    ghost1.save()
    ghost2.save()
    ghost3.save()
    troll1.save()
    troll2.save()
    troll3.save()
    vampire1.save()
    vampire2.save()
    vampire3.save()
    werewolf1.save()
    werewolf2.save()
    werewolf3.save()
    demon1.save()
    demon2.save()
    demon3.save()
    dragon1.save()
    dragon2.save()
    dragon3.save()

    #Assign monsters to rooms
    phoenixreach_city.monster = demon3
    moonshadow_grove.monster = ghost1
    misthaven_vale.monster = None
    whispering_woods.monster = ghost3
    eldemoor_forest.monster = ghost2
    frostfall_glacier.monster = troll1
    silverstrand_beach.monster = werewolf1
    moonlit_cove.monster = troll2
    glade_grasslands.monster = troll3
    avalon.monster = werewolf3
    luminara_falls.monster = vampire2
    mistral_bay.monster = demon1
    thunderpeak_summit.monster = vampire1
    shadowfen_swamp.monster = vampire3
    shadow_peak.monster = werewolf2
    crimsonreach_fortress.monster = demon2
    serpents_labrynth.monster = dragon1
    obsidian_abyss.monster = dragon2
    wyvern_lair.monster = None
    zukos_stronghold.monster = dragon3

    keys = {
        "glacier_key" : False,
        "water_key" : False,
        "flame_key" : False
    }
    
    def display_keys():
        print()
        print("Keys: ")
        for key in keys:
            print(f"{key}: {keys[key]}")
        print()

    def glacier_puzzle():
        cprint("Your have entered a challenge room! Solve the puzzle to win the key! Collect all three keys to battle the final boss!", "grey")
        print()

        print("""Welcome to FrostFall Glacier. The land of the ice! The glacier key lives here.
However, the binicles (binary icicles) are preventing you from reaching the key. It is your duty to
solve and shatter these binicles to obtain the key. Good luck! """)
        print()

        def puzzle(binary, answer):
            while True:
                print(f"BINARY NUMBER: {binary}")
                user_input = input("What is this binary number in decimal? >> ")
                if user_input == answer:
                    print("Correct!")
                    break
                else:
                    print("Not quite. Try again")
                    continue
            
        puzzle("10101010", "170")
        puzzle("11110001", "241")
        puzzle("01010101", "85")

        print("Great you now have the glacier key!")

        keys["glacier_key"] = True

    def water_puzzle():
        cprint("Your have entered a challenge room! Solve the puzzle to win the key! Collect all three keys to battle the final boss!", "grey")
        print()

        print("""Welcome to Silverstrand Beach. Your feet on the sands feel nice and warm. However, you
have a task to compelete. To get to the water key, your job is to decipher these floating
(decimal) numbers to text. Good luck!
              
side note: 
- use the ASCII table
- no spaces (except when told to space)
- case sensitive
""")
        print()

        def puzzle(ascii, answer):
            while True:
                print(f"DECIMAL NUMBERS: {ascii}")
                user_input = input("Convert decimal numbers to characters >> ")
                if user_input == answer:
                    print("Correct!")
                    break
                else:
                    print("Not quite. Try again")
                    continue

        puzzle("82 97 99 104 101 108", "Rachel")
        puzzle("83 76 73 84 72 69 82", "SLITHER")
        puzzle("79 110 101 SPACE 80 105 101 99 101", "One Piece")

        print("Nice! You now have the water key!")

        keys["water_key"] = True

    def flame_puzzle():
        cprint("Your have entered a challenge room! Solve the puzzle to win the key! Collect all three keys to battle the final boss!", "grey")
        print()

        print("""Welcome to Pheonixreach city, the civilization of flame.
The flame key is surrounded by flames. The flames are flashing bright continously.
Your task is to decipher the flashes and obtain the flame key! Good luck! 

side note:
- no spaces (except when told)
- use morse code translator
- not case sensitive """)
        print()

        def puzzle(morse, answer):
            while True:
                print(f"MORSE CODE: {morse}")
                user_input = input("Convert the morse code to text >> ")
                if user_input.lower() == answer.lower():
                    print("Correct")
                    break
                else:
                    print("Not quite. Try again")
                    continue

        puzzle(".-.. | . | -... | .-. | --- | -.", "lebron")
        puzzle(".--. | -.-- | - | .... | --- | -.", "python")
        puzzle("--. | .-. | . | . | -- SPACE .-.. | . | .", "greem lee")

        print("Congrats! You now have the flame key")

        keys["flame_key"] = True

    def go_direction(user_input):
        noneType = type(None)
        global current_room
        global prev_room
        direction = user_input[3:]
        next_room = current_room.dict[direction]

        if (next_room == zukos_stronghold):
            for key in keys:
                if keys[key] == False:
                    print("Collect all the keys first")
                    return

        if (isinstance(next_room, noneType)):
            print("You cannot travel here, select a different direction")
        else:
            prev_room = current_room
            current_room = next_room

            print(" ")
            print(f"You are now in: {current_room.name}")
            cprint(f"{current_room.description}", "blue")
            
            if current_room.gold > 0:
                print(f"You found {current_room.gold} gold in {current_room.name}")
                player.gold += current_room.gold
                current_room.gold = 0
                print(" ")

            if current_room == frostfall_glacier and keys["glacier_key"] == False:
                glacier_puzzle()
            elif current_room == silverstrand_beach and keys["water_key"] == False:
                water_puzzle()
            elif current_room == phoenixreach_city and keys["flame_key"] == False:
                flame_puzzle()

        
    def help():
        print('''  Commands list:
    Directions:  go up,  go down,  go left,  go right,  go back, 
    Information:  view info,  inventory,  location details,  keys
    Items:  equip,  unequip
    Battle:  attack,  retreat
              ''')

    def view_info():
        player.display_info()
        
    def view_inventory():
        print()
        print("Inventory: ")
        player.display_inventory()
        print()
        
    def view_room():
        current_room.display_info()

    def shop_view():
        # print(Item.view_table())
        # for shop_item in current_room.shop.items:
        #         print(f"TYPE: {shop_item.item_type}  NAME: {shop_item.name}  COST: {shop_item.cost}\n")
        CURSOR.execute("SELECT name, type, description, damage, defense, potion, cost FROM items")
        CONN.commit()
        result = CURSOR.fetchall()
        for item in result:
            print(str(f"NAME: {item[0]}   TYPE: {item[1]}    DESCRIPTION: {item[2]}    DAMAGE: {item[3]}    DEFENSE: {item[4]}    POTION: {item[5]}     COST: {item[6]} \n"))
        # print(result)


    def shop_buy():
        item_input = input("What item do you want to buy? >> ")
        selected_item = None
        for shop_item in current_room.shop.items:
            if shop_item.name.lower() == item_input.lower():
                selected_item = shop_item

        if selected_item == None:
            print("Item does not exist")
            return

        if (player.gold >= selected_item.cost):
            Item.remove_item_shop(selected_item.id)
            current_room.shop.items.remove(selected_item)
            player.gold -= selected_item.cost
            player.inventory.append(selected_item)
            print(f"Successfully purchased {selected_item.name}")
        else:
            print("Shop Onwer: You don't have enough gold!")
        
    def shop_sell():
            while True:
                view_inventory()

                item_input = input("Shop Owner: What are you selling? >> ")
                selected_item = None

                for item in player.inventory:
                    if item.name.lower() == item_input.lower():
                        selected_item = item

                if selected_item == None:
                    print("Item does not exist in your inventory")
                    continue
                else:
                    selected_item.add_item_shop()
                    player.inventory.remove(selected_item)
                    print("SOLD")
                    player.gold += selected_item.cost
                    current_room.shop.items.append(selected_item)
                    break

    def shop():
        if current_room.shop == None:
            print("There is no shop here")
        else:
            print("Shop Owner:   Welcome!! What would you like?\n")
            shop_view()
            while True:
                print(f"Gold: {player.gold}")
                shop_input = input("Shop Owner: Would you like to buy, sell, view or quit? >> ")
                if shop_input == "view":
                    shop_view()
                elif shop_input == "buy":
                    shop_buy()
                elif shop_input == "sell":
                    shop_sell()
                elif shop_input == "quit":
                    print("Shop Owner: Thank you for stopping by!")
                    break

    def drops():
            monster_drops = current_room.monster.drops

            for drop in monster_drops:
                drop.remove_item_monster(drop.id)
                if drop != None:
                    print(f"{current_room.monster.name} dropped {drop.name} and now in inventory")
                    player.inventory.append(drop)
            print(f"Monster dropped {current_room.monster.gold} gold")
            player.gold += current_room.monster.gold
            print(f"Current Gold: {player.gold}")
            print()
        

    def battle():
        if current_room.monster == None:
            print("There are no monsters in this room.")
        else:
            cprint(current_room.monster.avatar, "red")
            print(f"You are in battle with {current_room.monster.name}!")
            while True:
                # PLAYER ATTACKS
                battle_input = input("attack or retreat? >> ")
                if battle_input == "attack":
                    # PLAYER DOES DMG TO MONSTER
                    current_room.monster.take_damage(player.attack)
                    cprint(f"You did {player.attack} damage {current_room.monster.name} has {current_room.monster.hp} health.", "green")

                    # MONSTER DIES
                    if (current_room.monster.hp <= 0):
                        print()
                        cprint(f"{current_room.monster.name} has been vanquished!", "yellow")
                        #player hp should be reset
                        player.hp = player.max_hp
                        #monster should drop items
                        drops()
                        #monster should be deleted
                        CURSOR.execute(f"DELETE FROM monsters WHERE name='{current_room.monster.name}'")
                        CONN.commit()
                        current_room.monster = None
                        break

                    # MONSTER DOES DMG TO PLAYER
                    player.take_damage(current_room.monster.attack)
                    cprint(f"You took {current_room.monster.attack} damage, you now have {player.hp} health.", "red")

                    # PLAYER DIES
                    if (player.hp <= 0):
                        player_loses = pyfiglet.figlet_format("YOU LOSE")
                        cprint(player_loses, "red")
                        cprint(f"You have been defeated by {current_room.monster.name}...", "red")
                        return False
                    
                elif battle_input == "retreat":
                    print("You have retreated from battle.")
                    #player and monster hp should be reset
                    player.hp = player.max_hp + player.defense
                    current_room.monster.hp = current_room.monster.health
                    break

            # INDICATES THAT THE PLAYER IS ALIVE
            return True

    
    def back():
        global current_room
        global prev_room
        temp = prev_room
        prev_room = current_room
        current_room = temp
        print()
        print(f"You are back in {current_room.name}")
        print()

    
    def view_equipment():
        player.display_equipment()

    def equip(user_input):
        item_name = user_input[6:]
        curr_item = None
        for item in player.inventory:
            if item.name.lower() == item_name.lower():
                curr_item = item
            
        if curr_item is None:
            print()
            cprint(f"{item_name} not found in inventory", "red")
            print()
            return
    
        if curr_item.item_type == "WEAPON" and player.weapon != curr_item:
            if (player.weapon != None):
                player.attack -= player.weapon.damage
            player.weapon = curr_item
            player.attack += curr_item.damage
            print()
            cprint(f"Successfully equipped {curr_item.name}", "green")
            print()
        elif curr_item.item_type == "ARMOR" and player.armor != curr_item:
            if (player.armor != None):
                player.max_hp -= player.armor.defense
                player.hp = player.max_hp
            player.armor = curr_item
            player.max_hp += curr_item.defense
            player.hp = player.max_hp
            print()
            cprint(f"Successfully equipped {curr_item.name}", "green")
            print()
        else:
            print()
            cprint("Cannot equip", "red")
            print()

    def unequip(user_input):
        item_name = user_input[8:]

        if (player.armor != None):
            if (player.armor.name.lower() == item_name.lower()):
                player.max_hp -= player.armor.defense
                player.hp = player.max_hp
                player.armor = None
                print()
                cprint(f"Successfully unequipped {item_name}", "green")
                print()
            else:
                print()
                cprint(f"{item_name} was not unequipped", "red")
                print()


        if (player.weapon != None):
            if (player.weapon.name.lower() == item_name.lower()):
                player.attack -= player.weapon.damage
                player.weapon = None
                print()
                cprint(f"Successfully unequipped {item_name}", "green")
                print()
            else:
                print()
                cprint(f"{item_name} was not unequipped", "red")
                print()


    while True:
        alive = True
        user_input = input(">> ")

        if user_input == "go up":
            go_direction(user_input)
        elif user_input == "go down":
            go_direction(user_input)
        elif user_input == "go left":
            go_direction(user_input)
        elif user_input == "go right":
            go_direction(user_input)
        elif user_input == "go back":
            back()
        elif user_input == "help":
            help()
        elif user_input == "inventory":
            view_inventory()
        elif user_input == "view info":
            view_info()
        elif user_input == "equipment":
            view_equipment()
        elif user_input[:5] == "equip" and len(user_input) > 5 and user_input[5] == " ":
            equip(user_input)
        elif user_input[:7] == "unequip" and len(user_input) > 7 and user_input[7] == " ":
            unequip(user_input)
        elif user_input == "location details":
            view_room()
        elif user_input == "shop":
            shop()
        elif user_input == "battle":
            alive = battle()
        elif user_input == "keys":
            display_keys()
        else:
            print("Choose a valid input, use 'help' for more details.")

        if (alive == False):
            print("You're dead")
            break

        CURSOR.execute("SELECT * FROM monsters WHERE name = 'Zuko'")
        CONN.commit()
        zuko_result = CURSOR.fetchall()
        if len(zuko_result) < 1:
            winning_message = pyfiglet.figlet_format("YOU WIN!!!!!!")
            cprint(winning_message, "green")


main()