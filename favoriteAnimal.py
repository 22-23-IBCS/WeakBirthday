class Lizard:

    def __init__(self, b, m, col):
        self.numLegs = 4
        self.diet = m
        self.species = b
        self.color = col


    def getSpecies(self):
        return self.species

    def getDiet(self):
        return self.diet

    def getColor(self):
        return self.color

    def setDiet(self, m):
        self.diet = m

    def setSpecies(self, b):
        self.species = b

def main():

    print("These are my favorite animals and they are: ")

    liz1 = Lizard("Komodo:", "Carnivorous,", "Gray")
    liz2 = Lizard("Iguana:", "Omnivorous,", "Green")
    b = liz1.getSpecies()
    m = liz1.getDiet()
    col = liz1.getColor()
    print(b, m, col)
    liz1.setSpecies("Iguana:")
    print(liz1.getSpecies(), liz2.getDiet(), liz2.getColor())


if __name__ == "__main__":
    main()
