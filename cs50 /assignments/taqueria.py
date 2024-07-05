menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}


def main():
    tab()


def tab():
    tab = 0
    while True:
        try:
            item = input("Item: ").strip().title()
            for order in menu:
                if order == item:
                    tab = tab + (menu[order])
                    Total = str(tab)
                    tab = round(tab, 2)
                    print("${:.2f}".format(tab))
        except (EOFError, KeyError):
            break


if __name__ == "__main__":
    main()
