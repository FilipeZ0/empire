# Game Python Database

class GameState():
    def __init__(self):
        self.player = None
        self.characters = []
        self.villages = []

game = GameState()

class NavigationController():

    def __init__(self):
        self.current = None
        self.previous = None

    def back(self):
        self.current = self.previous

    def goto(self, menu):
        self.previous = self.current
        self.current = menu

class Menu():

    def __init__(self, name, *options):
        self.name = name
        self.options = options

    def DisplayOptions(self):
        while True:
            i = 1
            print(f"----------- {self.name} -----------")
            for option in self.options:
                
                print(f"{i}. {option}")
                i += 1
            
            if not self.name == townhall.name:
             
                print(f"{i}. Back")

            
            try:
                choice = int(input("- "))

                if choice <= i:
                    choice = self.options[choice-1]
                    break
                    
                else:
                    print(f"Oops! Your choice should be a number between {range(i)}.")
                    continue
                

            except:
                print("Oops! Your choice should be a number.")
                continue

townhall = Menu("Townhall", "My Empire", "Recruitment Center", "My LogBook")
empire = Menu("Townhall", game.villages)