from classes import *
from databases import *

def Welcome():
    print("While wandering on the most remote regions of this vast world, you find a small village, and notice an old man, who shouts:")
    print("- Please help us!")
    print("You accept the despaired call for help.")
    print("- What is your name?")

    # Sets the player name and appends it to the character list
    game.player = Character(name=input("- My name is "), strength=0, intelligence=0, speed=0)
    game.characters.append(game.player) 

    print(f"- Welcome to the village, {game.player.name}!")
    print("- This is a small village, but it will be big one day! We are happy to receive you as our leader! What should we call it?")

    # Sets the villages's name and appends it to the village list
    game.villages.append(Village(name=input("- "), leader=game.player))

def Empire():
    i = 1
    options = {}

    # Defines the options available
    for village in game.villages: # O(n) time (Big O Notation)
        
        if village.leader == game.player:
            
            options[i] = village.name

        i += 1

        menu_handler("Villages", options)

def main():
    Welcome()
    menu = NavigationController()
    townhall.DisplayOptions()

if __name__ == "__main__":
    main()