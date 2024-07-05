from datetime import date
from datetime import datetime
import inflect
import sys

p = inflect.engine()


def main():
    birth = input("birth date: ").lstrip(" ")
    print(t_delta(get_birth(birth)))


def get_birth(s):
    format = "%Y-%m-%d"
    try:
        check_format = bool(datetime.strptime(s, format))
        if check_format is True:
            return datetime.strptime(s, format)
        else:
            raise ValueError
    except ValueError:
        sys.exit("Incorrect date format")


def t_delta(s):
    today = datetime.strptime(f"{date.today()}", "%Y-%m-%d")
    delta = p.number_to_words((int((today - s).total_seconds() / 60)), andword="")

    return f"{delta} minutes".capitalize()


if __name__ == "__main__":
    main()
