def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            x, y = int(x), int(y)
            if x > y or y == 0:
                if y == 0:
                    raise ZeroDivisionError
                else:
                    raise ValueError
            elif x / y <= 1:
                percentage = x / y
                percentage = percentage * 100
                return percentage

            else:
                fraction = input("Fraction: ")
                continue
        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
