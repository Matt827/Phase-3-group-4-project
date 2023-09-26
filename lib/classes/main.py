# import pyfiglet
# from termcolor import cprint

from player import Player
from rooms import Room
from item import Item
from monster import Monster

# result = pyfiglet.figlet_format("Adventures of Mattanoman")

# cprint(result, "red")


# LOCATIONS
moonshadow_grove = Room('Moonshadow Grove', 'Moonshadow Grov, a mystical forest bathed in the silvery glow of the moon, where ancient, luminescent flora and fauna thrive, and whispers of forgotten enchantments linger in the cool night air.', None, None, 25)
whispering_woods = Room('Whispering Woods', 'Whispering Woods, a serene woodland sanctuary where the leaves rustle with secrets, and ancient trees seem to murmur tales of forgotten magic, offering solace to those who seek its tranquil embrace.', None, None, 25)
eldemoor_forest = Room('Eldemoor Forest', 'Eldemoor Forest, an ethereal realm where ancient trees reach for the sky, their trunks adorned with bioluminescent flora that illuminate the forest floor, casting a surreal, enchanting glow over the moss-covered ground.', None, None, 25)
frostfall_glacier = Room('Frostfall Glacier', 'Frostfall Glacier stretches as far as the eye can see, a vast expanse of shimmering ice and snow beneath the towering peaks, where the air is crisp with the promise of adventure and every step echoes in the serene, frozen stillness.', None, None, 25)
silverstrand_beach = Room('Silverstrand Beach', 'Silverstrand Beach is a pristine coastal paradise, where fine, silvery sands stretch alongside crystalline waters, kissed by the gentle caress of a perpetual sunset, creating a timeless haven of tranquility and beauty.', None, None, 25)
moonlit_cove = Room('Moonlit Cove', 'Moonlit Cove is a secluded bay nestled between rugged cliffs, its tranquil waters reflecting the silvery glow of the moon, while ancient, luminescent flora line the shore, casting an otherworldly aura over this hidden sanctuary.', None, None, 25)
misthaven_vale = Room('Misthaven Vale', 'Misthaven Vale is a mystical highland shrouded in perpetual mist, where emerald forests and cascading waterfalls converge, and the air is alive with the soft hum of ancient enchantments, creating an ethereal realm untouched by time.', None, None, 25)
glade_grasslands = Room('Glade Grasslands', 'Glade Grasslands unfurl as an endless expanse of rolling meadows, their emerald blades swaying in harmonious rhythm with the breeze, where wildflowers bloom in a symphony of color, inviting wanderers to bask in the serenity of natures embrace.', None, None, 25)
avalon = Room('Avalon', "Mythical island of legend", None, None, 25)
luminara_falls = Room('Luminara Falls', 'Luminara Falls cascades down a majestic cliffside, its crystalline waters refracting the sunlight into a kaleidoscope of colors, while ethereal wisps of mist dance around the falls, creating a breathtaking, almost otherworldly spectacle.', None, None, 25)
mistral_bay = Room('Mistral Bay', 'Mistral Bay is a picturesque coastal retreat where azure waves gently lap against the shore, kissed by the refreshing caress of a perpetual sea breeze, while rugged cliffs and lush vegetation frame this idyllic sanctuary.', None, None, 25)
thunderpeak_summit = Room('Thunderpeak Summit', 'Thunderpeak Summit looms as the highest pinnacle in a range of ancient, mist-shrouded mountains, its jagged spires seeming to touch the very heavens, where thunderstorms and crackling energy fill the air with an electric charge, creating an awe-inspiring yet perilous realm.', None, None, 25)
shadowfen_swamp = Room('Shadowfen Swamp', 'Shadowfen Swamp sprawls in mysterious gloom, its tangled, moss-draped trees and murky waters shrouded in a perpetual twilight, where haunting cries of unseen creatures echo through the mist, and twisted roots conceal secrets of ages past.', None, None, 25)
shadow_peak = Room('Shadow Peak', 'Shadow Peak stands as a towering monolith amidst a desolate, moonlit wasteland, its jagged spires casting long, eerie silhouettes across the barren expanse, where the air is heavy with an unsettling stillness, harboring the whispers of forgotten legends.', None, None, 25)
crimsonreach_fortress = Room('Crimsonreach Fortress', 'Crimsonreach Fortress is a formidable citadel perched atop a blood-red cliff, its dark, stone walls looming over turbulent seas, while fiery torches light the way through labyrinthine corridors echoing with the history of battles long past.', None, None, 25)
phoenixreach_city = Room('Pheonixreach City', 'Phoenixreach City sprawls as a bustling metropolis of gleaming spires and arched bridges, its streets alive with a vibrant tapestry of cultures, where the air hums with the energy of innovation and the spirit of rebirth.', None, None, 25)
serpents_labrynth = Room("Serpent's Labrynth", 'Serpents Labyrinth winds through an ancient subterranean maze, its shadowy passages illuminated by bioluminescent flora, where the hiss of unseen creatures and the echo of forgotten whispers create an eerie, enigmatic atmosphere.', None, None, 25)
obsidian_abyss = Room('Obsidian Abyss', 'Obsidian Abyss plunges into the depths of the earth, a chasm of smooth, jet-black stone walls that seem to absorb all light, where the air is heavy with a sense of ancient, foreboding power.', None, None, 25)
wyvern_lair = Room('Wyvern Lair', 'Wynvern Lair is a hidden sanctuary nestled within the craggy heart of a mist-shrouded mountain, its caverns adorned with glistening crystals and echoing with the occasional stirring of slumbering wyverns, guarding their ancient treasures.', None, None, 25)
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
    player = Player(name)
    print(f'''
Once upon a time, in the mystical realm of Eldoria, there was a fallen king named {player.name}. 
He had once ruled over a prosperous kingdom, but his reign had been marred by a black dragon. 
The Black Dragon took control of the entire kingdom and took his people into captivity. 
He must now adventure through the land of Elda, battling monsters and foes, and eventually defeating the Black Dragon, Zuko to free his people and reclaim his kingdom.''')
    

    # MONSTERS
    ghost1 = Monster("Ghost", 25, 30, 5, 40, ["Ghostly Essence", "Gold Coin"])
    ghost2 = Monster("Ghost", 25, 30, 5, 40, ["Ghostly Essence", "Gold Coin"])
    ghost3 = Monster("Ghost", 25, 30, 5, 40, ["Ghostly Essence", "Gold Coin"])
    troll1 = Monster("Troll", 18, 45, 10, 15, ["Troll Tooth", "Gold Coin"])
    troll2 = Monster("Troll", 18, 45, 10, 15, ["Troll Tooth", "Gold Coin"])
    troll3 = Monster("Troll", 18, 45, 10, 15, ["Troll Tooth", "Gold Coin"])
    vampire1 = Monster("Vampire", 40, 60, 15, 28, ["Vampire Fang", "Gold Coin"])
    vampire2 = Monster("Vampire", 40, 60, 15, 28, ["Vampire Fang", "Gold Coin"])
    vampire3 = Monster("Vampire", 40, 60, 15, 28, ["Vampire Fang", "Gold Coin"])
    werewolf1 = Monster("Werewolf", 30, 75, 20, 22, ["Werewolf Fur", "Gold Coin"])
    werewolf2 = Monster("Werewolf", 30, 75, 20, 22, ["Werewolf Fur", "Gold Coin"])
    werewolf3 = Monster("Werewolf", 30, 75, 20, 22, ["Werewolf Fur", "Gold Coin"])
    demon1 = Monster("Demon", 45, 90, 25, 15, ["Demon Horn", "Gold Coin"])
    demon2 = Monster("Demon", 45, 90, 25, 15, ["Demon Horn", "Gold Coin"])
    demon3 = Monster("Demon", 45, 90, 25, 15, ["Demon Horn", "Gold Coin"])
    dragon1 = Monster("Zephyrion", 100, 200, 20, 30, ["Dragon Scale", "Dragon Tooth"])
    dragon2 = Monster("Celestiax", 100, 200, 20, 30, ["Dragon Scale", "Dragon Tooth"])
    dragon3 = Monster("Zuko", 100, 200, 30, 30, ["Dragon Scale", "Dragon Tooth"])
    
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
    

    # WEAPONS
    excalibur = Item("Excalibur", "WEAPON", "Legendary Sword", 10, None, None, 15)
    mjolnir = Item("Mjolnir", "WEAPON", "Thunderous Hammer", 20, None, None, 25)
    dragonbone_bow = Item("Dragonbone Bow", "WEAPON", "Wyrmstring Bow", 27, None, None, 32)
    shadowblade = Item("Shadow Blade", "WEAPON", "Stealthy Dagger", 15, None, None, 20)
    soul_reaver = Item("Soul Reaver", "WEAPON", "Cursed Sword", 30, None, None, 35)
    moonlit_dagger = Item("Moonlit Dagger", "WEAPON", "Silvered Blade", 13, None, None, 17)
    serpents_fang = Item("Serpent's Fang", "WEAPON", "Venomous Whip", 16, None, None, 21)
    stormcaller = Item("Stormcaller", "WEAPON", "Lightning Sword", 27, None, None, 32)
    dwarven_crossbow = Item("Dwarvan Crossbow", "WEAPON", "Stour Crossbow", 12, None, None, 17)
    warhammer_of_the_titans = Item("Warhammer of the Titans", "WEAPON", "Colossal Warhammer", 35, None, None, 40)

    # ARMOR
    knight_armor_set = Item("Knights Armor Set", "ARMOR", "none", None, 25, None, 35)
    noble_lord_armor_set = Item("Noble Lord Armor Set", "ARMOR", "none", None, 50, None, 60)
    commander_armor_set = Item("Commander Armor Set", "ARMOR", "none", None, 75, None, 85)
    king_armor_set = Item("King Armor Set", "ARMOR", "none", None, 100, None, 110)

    # POTION
    health_potion = Item("Vitality Elixir", "POTION", "none", None, None, 25, 50)

    
    player.inventory.append(excalibur)
    player.inventory.append(knight_armor_set)
    player.inventory.append(health_potion)
    
    def go_direction(user_input):
        noneType = type(None)
        global current_room
        global prev_room
        direction = user_input[3:]
        next_room = current_room.dict[direction]
        if (isinstance(next_room, noneType)):
            print("Not a room")
        else:
            prev_room = current_room
            current_room = next_room
            print(f"current room: {current_room.name}")
            print(f"previous room: {prev_room.name}")

        # if current_room != None:
        #     direction = user_input[3:]
        #     current_room = current_room.dict[direction].name
        #     print(current_room)
        # else:
        #    print("Not working!")
        
    def help():
        print('''    Commands list:
    Directions:  go up,  go down,  go left,  go right,  go back, 
    Information:  view info,  view inventory,  location details,
    Battle:  attack 
              ''')

    def view_info():
        player.display_info()
        
    def view_inventory():
        player.display_inventory()
        
    def view_room():
        current_room.display_info()
    
    def back():
        global current_room
        global prev_room
        temp = prev_room
        prev_room = current_room
        current_room = temp
        print(f"current room: {current_room.name}")
        print(f"previous room: {prev_room.name}")

    def attack():
        print(f"you did {player.attack} damage! the monsters hp is {current_room.monster.hp - player.attack}")
        print(f"the {current_room.monster.name} did {current_room.monster.attack} damage! your hp is now {player.hp - current_room.monster.attack}")
        
    def drink_potion():
        player.drink_potion()
    
    while True:
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
        elif user_input == "view inventory":
            view_inventory()
        elif user_input == "view info":
            view_info()
        elif user_input == "location details":
            view_room()
        elif user_input == "attack":
            attack()
        elif user_input == "drink potion":
            drink_potion()
        else:
            print("Choose a valid input, use 'help' for more details.")


main()