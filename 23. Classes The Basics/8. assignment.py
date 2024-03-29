class Zombie():
    def __init__(self, healt = 100, brains_eaten = 5):
        self.healt = healt
        self.brain_eatens = brains_eaten
        

bob = Zombie(healt= 80)
print("Healt=", bob.healt, "\nBrains eaten=", bob.brain_eatens)

sally = Zombie(120, 3)
print("Healt=", sally.healt, "\nBrains eaten=", sally.brain_eatens)

benjamin = Zombie()
print("Healt=", benjamin.healt, "\nBrains eaten=", benjamin.brain_eatens)
