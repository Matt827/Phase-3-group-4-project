# Once upon a time, in the mystical realm of Eldoria, there was a fallen king named Mattonoman.
# He had once ruled over a prosperous kingdom, but his reign had been marred by a black dragon. 
# The Black Dragon took control of the entire kingdom and took his people into captivity. 
# He must now adventure through the land of Elda, battling monsters and foes, and eventually defeating the Black Dragon, Zuko to free his people and reclaim his kingdom.

# import pyfiglet
# from termcolor import cprint

from player import Player
from rooms import Room
from item import Item
from monster import Monster

# result = pyfiglet.figlet_format("Adventures of Mattanoman")

moonshadow_grove = Room('Moonshadow Grove', 'Moonshadow Grov, a mystical forest bathed in the silvery glow of the moon, where ancient, luminescent flora and fauna thrive, and whispers of forgotten enchantments linger in the cool night air.', None, None, 25)
whispering_woods = Room('Whispering Woods', 'Whispering Woods, a serene woodland sanctuary where the leaves rustle with secrets, and ancient trees seem to murmur tales of forgotten magic, offering solace to those who seek its tranquil embrace.', None, None, 25)
eldemoor_forest = Room('Eldemoor Forest', 'Eldemoor Forest, an ethereal realm where ancient trees reach for the sky, their trunks adorned with bioluminescent flora that illuminate the forest floor, casting a surreal, enchanting glow over the moss-covered ground.', None, None, 25)
frostfall_glacier = Room('Frostfall Glacier', 'Frostfall Glacier stretches as far as the eye can see, a vast expanse of shimmering ice and snow beneath the towering peaks, where the air is crisp with the promise of adventure and every step echoes in the serene, frozen stillness.', None, None, 25)
silverstrand_beach = Room('Silverstrand Beach', 'Silverstrand Beach is a pristine coastal paradise, where fine, silvery sands stretch alongside crystalline waters, kissed by the gentle caress of a perpetual sunset, creating a timeless haven of tranquility and beauty.', None, None, 25)
moonlit_cove = Room('Moonlit Cove', 'Moonlit Cove is a secluded bay nestled between rugged cliffs, its tranquil waters reflecting the silvery glow of the moon, while ancient, luminescent flora line the shore, casting an otherworldly aura over this hidden sanctuary.', None, None, 25)
misthaven_vale = Room('Misthaven Vale', 'Misthaven Vale is a mystical highland shrouded in perpetual mist, where emerald forests and cascading waterfalls converge, and the air is alive with the soft hum of ancient enchantments, creating an ethereal realm untouched by time.', None, None, 25)
glade_grasslands = Room('Glade Grasslands', 'Glade Grasslands unfurl as an endless expanse of rolling meadows, their emerald blades swaying in harmonious rhythm with the breeze, where wildflowers bloom in a symphony of color, inviting wanderers to bask in the serenity of natures embrace.', None, None, 25)
luminara_falls = Room('Luminara Falls', 'Luminara Falls cascades down a majestic cliffside, its crystalline waters refracting the sunlight into a kaleidoscope of colors, while ethereal wisps of mist dance around the falls, creating a breathtaking, almost otherworldly spectacle.', None, None, 25)
mistral_bay = Room('Mistral Bay', 'Mistral Bay is a picturesque coastal retreat where azure waves gently lap against the shore, kissed by the refreshing caress of a perpetual sea breeze, while rugged cliffs and lush vegetation frame this idyllic sanctuary.', None, None, 25)
thunderpeak_summit = Room('Thunderpeak Summit', 'Thunderpeak Summit looms as the highest pinnacle in a range of ancient, mist-shrouded mountains, its jagged spires seeming to touch the very heavens, where thunderstorms and crackling energy fill the air with an electric charge, creating an awe-inspiring yet perilous realm.', None, None, 25)
shadowfen_swamp = Room('Shadowfen Swamp', 'Shadowfen Swamp sprawls in mysterious gloom, its tangled, moss-draped trees and murky waters shrouded in a perpetual twilight, where haunting cries of unseen creatures echo through the mist, and twisted roots conceal secrets of ages past.', None, None, 25)
shadow_peak = Room('Shadow Peak', 'Shadow Peak stands as a towering monolith amidst a desolate, moonlit wasteland, its jagged spires casting long, eerie silhouettes across the barren expanse, where the air is heavy with an unsettling stillness, harboring the whispers of forgotten legends.', None, None, 25)
crimsonreach_fortress = Room('Crimsonreach Fortress', 'Crimsonreach Fortress is a formidable citadel perched atop a blood-red cliff, its dark, stone walls looming over turbulent seas, while fiery torches light the way through labyrinthine corridors echoing with the history of battles long past.', None, None, 25)
phoenixreach_city = Room('Pheonixreach City', 'Phoenixreach City sprawls as a bustling metropolis of gleaming spires and arched bridges, its streets alive with a vibrant tapestry of cultures, where the air hums with the energy of innovation and the spirit of rebirth.', None, None, 25)
serpents_labrynth = Room("Serpent's Labrynth", 'Serpents Labyrinth winds through an ancient subterranean maze, its shadowy passages illuminated by bioluminescent flora, where the hiss of unseen creatures and the echo of forgotten whispers create an eerie, enigmatic atmosphere.', None, None, 25)
obsidian_abyss = Room('Obsidian Abyss', 'Obsidian Abyss plunges into the depths of the earth, a chasm of smooth, jet-black stone walls that seem to absorb all light, where the air is heavy with a sense of ancient, foreboding power.', None, None, 25)
wynhaven_lair = Room('Wynvern Lair', 'Wynvern Lair is a hidden sanctuary nestled within the craggy heart of a mist-shrouded mountain, its caverns adorned with glistening crystals and echoing with the occasional stirring of slumbering wyverns, guarding their ancient treasures.', None, None, 25)
zukos_stronghold = Room("Zuko's Stronghold", 'Zukos Stronghold, hewn from the living rock of a volcanic peak, stands as a formidable bastion overlooking a fiery landscape, where molten streams cascade down the slopes, and the air resonates with the presence of the majestic dragon, Zuko, guardian of this fiery domain.', None, None, 25)

current_room = misthaven_vale 


def main():
    name = input("What is your name? ")
    player_name = Player(name)
    print(f'''
Once upon a time, in the mystical realm of Eldoria, there was a fallen king named {player_name.name}. He had once ruled over a prosperous kingdom, but his reign had been marred by a black dragon. 
The Black Dragon took control of the entire kingdom and took his people into captivity. 
He must now adventure through the land of Elda, battling monsters and foes, and eventually defeating the Black Dragon, Zuko to free his people and reclaim his kingdom.''')
    ## LOCATIONS
      
    
    def directions(current_room):
        if current_room == phoenixreach_city:
            phoenixreach_city.room_directions(shadow_peak, obsidian_abyss, crimsonreach_fortress, serpents_labrynth)
        elif current_room == moonshadow_grove:  
            moonshadow_grove.room_directions(misthaven_vale, shadow_peak, thunderpeak_summit, shadowfen_swamp)
        elif current_room == misthaven_vale:      
            misthaven_vale.room_directions(eldemoor_forest, moonshadow_grove, moonlit_cove, glade_grasslands)
        elif current_room == whispering_woods:      
            whispering_woods.room_directions(None, moonlit_cove, None, eldemoor_forest)
        elif current_room == eldemoor_forest:      
            eldemoor_forest.room_directions(None, misthaven_vale, whispering_woods, frostfall_glacier)
        elif current_room == frostfall_glacier:      
            frostfall_glacier.room_directions(None, None, eldemoor_forest, None)
        elif current_room == silverstrand_beach:      
            silverstrand_beach.room_directions(None, mistral_bay, None, moonlit_cove)
        elif current_room == moonlit_cove:      
            moonlit_cove.room_directions(whispering_woods, thunderpeak_summit, silverstrand_beach, misthaven_vale)
        elif current_room == glade_grasslands:      
            glade_grasslands.room_directions(None, shadowfen_swamp, misthaven_vale, luminara_falls)
        elif current_room == luminara_falls:      
            luminara_falls.room_directions(None, None, glade_grasslands, None)
        elif current_room == mistral_bay:      
            mistral_bay.room_directions(silverstrand_beach, None, None, None)
        elif current_room == thunderpeak_summit:     
            thunderpeak_summit.room_directions(moonlit_cove, glade_grasslands, None, moonshadow_grove)
        elif current_room == shadowfen_swamp:      
            shadowfen_swamp.room_directions(glade_grasslands, None, moonshadow_grove, None)
        elif current_room == shadow_peak:      
            shadow_peak.room_directions(moonshadow_grove, phoenixreach_city, None, None)
        elif current_room == crimsonreach_fortress:      
            crimsonreach_fortress.room_directions(glade_grasslands, None, None, phoenixreach_city)
        elif current_room == serpents_labrynth:      
            serpents_labrynth.room_directions(None, wynhaven_lair, phoenixreach_city, None)
        elif current_room == obsidian_abyss:      
            obsidian_abyss.room_directions(phoenixreach_city, None, None, wynhaven_lair)
        elif current_room == wynhaven_lair:      
            wynhaven_lair.room_directions(serpents_labrynth, None, obsidian_abyss, zukos_stronghold)
        elif current_room == zukos_stronghold:      
            zukos_stronghold.room_directions(None, None, wynhaven_lair, None)


    # global current_room
    


    #MONSTERS
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


    ## WEAPONS
    # excalibur = Item("Excalibur", "Legendary Sword", 10, None, None, 15)
    # mjolnir = Item("Mjolnir", "Thunderous Hammer", 20, None, None, 25)
    # dragonbone_bow = Item("Dragonbone Bow", "Wyrmstring Bow", 27, None, None, 32)
    # shadowblade = Item("Shadow Blade", "Stealthy Dagger", 15, None, None, 20)
    # soul_reaver = Item("Soul Reaver", "Cursed Sword", 30, None, None, 35)
    # moonlit_dagger = Item("Moonlit Dagger", "Silvered Blade", 13, None, None, 17)
    # serpents_fang = Item("Serpent's Fang", "Venomous Whip", 16, None, None, 21)
    # stormcaller = Item("Stormcaller", "Lightning Sword", 27, None, None, 32)
    # dwarven_crossbow = Item("Dwarvan Crossbow", "Stour Crossbow", 12, None, None, 17)
    # warhammer_of_the_titans = Item("Warhammer of the Titans", "Colossal Warhammer", 35, None, None, 40)

    # ## ARMOR
    # knight_armor_set = Item("Knights Armor Set", None, 25, None, 35)
    # noble_lord_armor_set = Item("Noble Lord Armor Set", None, 50, None, 60)
    # commander_armor_set = Item("Commander Armor Set", None, 75, None, 85)
    # king_armor_set = Item("King Armor Set", None, 100, None, 110)

    # ## POTION
    # health = Item("Increase Max Health", None, None, 25, 50)
    
    
    
    def go_direction(user_input, current_room):
        NoneType = type(None)

        prev_room = current_room
        directions(current_room)
        direction = user_input[3:]
        current_room = current_room.dict[direction]
        if isinstance(current_room, NoneType):
            print("Cannot go that direction!")
            change_direction(prev_room)
        else:
            print(current_room.name)
            change_direction(current_room)
            
        

    def change_direction(current_room):
        while True:
            user_input = input(">> ")

            if user_input == "go up":
                go_direction(user_input, current_room)
            elif user_input == "go down":
                go_direction(user_input, current_room)
            elif user_input == "go left":
                go_direction(user_input, current_room)
            elif user_input == "go right":
                go_direction(user_input, current_room)
            else:
                print("Choose a valid direction. ex. 'go left', 'go right'")
    
    change_direction(current_room)
        





main()