def main():
    percentage()


def percentage():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
            x, y = int(x), int(y)
            fraction = x / y * 100
            percentage = round(fraction)
            if x > y:
                continue

            elif percentage >= 99:
                print(f"F")

            elif percentage <= 1:
                print(f"E")

            else:
                print(f"{percentage}%")

        except (ValueError, ZeroDivisionError):
            pass

        else:
            break


if __name__ == "__main__":
    main()
