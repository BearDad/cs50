

# dictionary with fruits and calories of each fruit
fruits = {
    "apple": "130",
    "avocado": "50",
    "banana": "110",
    "cantaloupe": "50",
    "grapefruit": "60",
    "grapes": "90",
    "honeydew melon": "50",
    "Kiwifruit": "90",
    "lemon": "15",
    "lime": "20",
    "nectarine": "60",
    "orange": "80",
    "peach": "60",
    "pear": "100",
    "pineapple": "50",
    "plums": "70",
    "strawberries": "50",
    "sweet cherries": "100",
    "tangerine": "50",
    "watermelon": "60",
}


# input of the fruit
def main():
    message = input("Fruit: ").lower()
    # for loop that checks for the corresponding keyword in the input from the dictionary and replaces it with its value
    for key, value in fruits.items():
        if key in message:
            message = message.replace(key, value)
            print("Calories:", message)


main()