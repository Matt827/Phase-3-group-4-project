# Once upon a time, in the mystical realm of Eldoria, there was a fallen king named Mattonoman.
# He had once ruled over a prosperous kingdom, but his reign had been marred by a black dragon. 
# The Black Dragon took control of the entire kingdom and took his people into captivity. 
# He must now adventure through the land of Elda, battling monsters and foes, and eventually defeating the Black Dragon, Zuko to free his people and reclaim his kingdom.

# import pyfiglet
# from termcolor import cprint

from player import Player



# result = pyfiglet.figlet_format("Adventures of Mattanoman")




# cprint(result, "red")


def main():
    name = input("What is your name? ")
    player_name = Player(name)
    print(f'''
Once upon a time, in the mystical realm of Eldoria, there was a fallen king named {player_name.name}. He had once ruled over a prosperous kingdom, but his reign had been marred by a black dragon. 
The Black Dragon took control of the entire kingdom and took his people into captivity. 
He must now adventure through the land of Elda, battling monsters and foes, and eventually defeating the Black Dragon, Zuko to free his people and reclaim his kingdom.''')

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