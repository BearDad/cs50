import random


def main():
    level = get_level()
    generate_integer(level)


def get_level():
    while True:
        try:
            level = int(input("level: "))
            if level <= 3 and level >= 1:
                return level
                pass
            else:
                print("invalid input")
        except ValueError:
            continue


def generate_integer(level):
    score = 0
    for i in range(9):
        trials = 0
        if level == 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        elif level == 2:
            x = random.randint(10, 90)
            y = random.randint(10, 99)
        elif level == 3:
            x = random.randint(100, 999)
            y = random.randint(100, 999)
        while True:
            try:
                print(f"{x} + {y} = ", end="")
                answer = int(input())
                if answer != x + y and trials < 2:
                    print("EEE")
                    trials += 1
                    continue
                else:
                    print(f"{x} + {y} = {x+y}")
                    score += 1
                    break
            except ValueError:
                if trials != 2:
                    print("EEE")
                    trials += 1
                    continue

                else:
                    print(f"{x} + {y} = {x+y}")
                    break
    print(f"Score:{score}")


if __name__ == "__main__":
    main()
