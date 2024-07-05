def main():
    text = input("Greetings: ")
    print("$" + str(value(text)))


def value(greeting):
    greeting = greeting.lower().strip().partition(" ")[0]
    if "hello" in greeting:
        return 0
    elif "h" in greeting[0]:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
