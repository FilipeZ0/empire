
char_types = ["Mage", "Knight"]

# User's Attributes Constructor
class Character():

    # Sets All Character's Default Stats
    default_stats = ("name", "role", "Village", "strength", "intelligence", "speed")

    def __init__(self, **stats):

        for stat in self.default_stats:
            setattr(self, stat, "Unkown")


        for stat, value in stats.items():
            setattr(self, stat, value)

    def statdisplay(self):
        
        print("---------- Character Stats ----------")
        for stat, value in self.__dict__.items():
            print(f"{stat.capitalize()}: {value}")

class Village():

    # Sets All Village's Default Stats
    default_stats = ("name", "population", "leader")

    def __init__(self, **stats):

        for stat in self.default_stats:
            setattr(self, stat, "Unkown")

        for stat, value in stats.items():
            setattr(self, stat, value)

    def statdisplay(self):
        print("---------- Village Stats ----------")
        for stat, value in self.__dict__.items():
            print(f"{stat.capitalize()}: {value}")

def main():

    def welcome():
        print("Please help us!")
        name = input("What is your name? ")
        print()
        print(f"Welcome, {name}!")
        print()
        hero = Character(name=name, strength=0, intelligence=0, speed=0)
        hero.statdisplay()
        print()
        print("We are a small village, but we will be big one day! We will receive you as our Leader!")
        village_name = input("What do you want to call our village? ")
        print()
        village = Village(name=village_name)
        village.statdisplay()

    welcome()



if __name__ == "__main__":
    main()