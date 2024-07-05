students = [
    {"name": "harry", "house": "gryffindor"},
    {"name": "ron", "house": "gryffindor"},
    {"name": "hermione", "house": "gryffindor"},
    {"name": "draco", "house": "slytherin"},
    {"name": "padma", "house": "ravenclaw"},
]


houses = []
for _ in students:
    if _["house"] not in houses:
        houses.append(_["house"])
for house in sorted(houses):
    print(house)

print(houses)
