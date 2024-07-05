import random


class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    # gets the name from outside of the class and uses the houses list to asign a house to a name
    @classmethod
    def sort(cls, name):
        house = random.choice(cls.houses)
        print(name, "is in", house)


# name gets sent to classmethod
Hat.sort("Harry")
