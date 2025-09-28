# Where all classes are stored

if not __name__ == "__main__":
# Character's Attributes Constructor
    class Character():

        # Sets All Character's Default Stats
        default_stats = ("name", "role", "Village", "strength", "intelligence", "speed")

        def __init__(self, **stats):

            # Sets all stats to unkown
            for stat in self.default_stats:
                setattr(self, stat, "Unkown")

            # Sets known stats to their respective values
            for stat, value in stats.items():
                setattr(self, stat, value)

        # Displays the character's stats
        def statdisplay(self):
            
            print("---------- Character Stats ----------")
            for stat, value in self.__dict__.items():
                print(f"{stat.capitalize()}: {value}")

    class Village():

        # Sets All Village's Default Stats
        default_stats = ("name", "population", "leader", "relashionship")

        
        def __init__(self, **stats):

            # Sets all stats to unkown
            for stat in self.default_stats:
                setattr(self, stat, "Unkown")

            # Sets known stats to their respective values
            for stat, value in stats.items():
                setattr(self, stat, value)

        # Displays Village's Stats
        def info(self):
            print("---------- Village Stats ----------")
            for stat, value in self.__dict__.items():
                print(f"{stat.capitalize()}: {value}")