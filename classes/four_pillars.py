# # Four Pillars
#
# # Abstraction - use methods to make life easier
# # Encapsulation - hide away dangerous things
# # Inheritance
# # Polymorphism
#
class Animal:
    def __init__(self):
        self.alive = True

    def hunt(self):
        print("Searching for food")

    def move(self):
        print("Moving...")


class Mammal(Animal):
    def __init__(self):
        super().__init__()

    def breed(self):
        print("Giving birth to live young")

class Platypus(Mammal):
    def __init__(self):
        super().__init__()



perry = Platypus()
perry.breed()
m = Mammal()
m.breed()

class Platypus(Mammal):
    def __init__(self):
        super().__init__()

    def breed(self):
        print("Laying eggs")


perry = Platypus()
perry.breed()
m = Mammal()
m.breed()


# Scrabble Checker Object
# Initialise it with a string of 7 random letters
        # Option of providing some letters
# A method to check that a submitted word can be made from those tiles
# A method to return the score for a submitted word
# A method to use the methods above to check a word is valid
# and if it is, return the score for that word

