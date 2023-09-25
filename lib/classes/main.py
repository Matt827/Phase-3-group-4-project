# Once upon a time, in the mystical realm of Eldoria, there was a fallen king named Mattonoman.
# He had once ruled over a prosperous kingdom, but his reign had been marred by a black dragon. 
# The Black Dragon took control of the entire kingdom and took his people into captivity. 
# He must now adventure through the land of Elda, battling monsters and foes, and eventually defeating the Black Dragon, Zuko to free his people and reclaim his kingdom.

# import pyfiglet
# from termcolor import cprint

from player import Player
from rooms import Room


# result = pyfiglet.figlet_format("Adventures of Mattanoman")




# cprint(result, "red")


def main():
    name = input("What is your name? ")
    player_name = Player(name)
    print(f'''
Once upon a time, in the mystical realm of Eldoria, there was a fallen king named {player_name.name}. He had once ruled over a prosperous kingdom, but his reign had been marred by a black dragon. 
The Black Dragon took control of the entire kingdom and took his people into captivity. 
He must now adventure through the land of Elda, battling monsters and foes, and eventually defeating the Black Dragon, Zuko to free his people and reclaim his kingdom.''')
    
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


while True:
        user_input = input(">> ")

        if user_input == "go up":
            print("You went up")
        elif user_input == "go down":
            print("You went down")
        elif user_input == "go left":
            print("You went left")
        elif user_input == "go right":
            print("You went right")
        else:
            print("Choose a valid direction. ex. 'go left', 'go right'")

        





main()