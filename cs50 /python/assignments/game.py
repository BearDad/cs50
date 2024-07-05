import random


def main():
    # level loop
    while True:
        try:
            x = int(input("Level: "))
        except ValueError:
            continue
        if x <= 0:
            continue

        level = random.randint(1, x)
        break

    # guess loop
    while True:
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                continue
        except ValueError:
            continue

        if guess > level:
            print("Too big!")
        elif guess < level:
            print("Too small!")
        elif guess == level:
            print("Just right!")
            break


if __name__ == "__main__":
    main()
