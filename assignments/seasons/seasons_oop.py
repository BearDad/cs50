from datetime import date
from datetime import datetime
import sys
import inflect

p = inflect.engine()


def main():
    times = Parse.get()
    print(times)


class Birthday:
    def __init__(self, birth):
        format = "%Y-%m-%d"
        try:
            check_format = bool(datetime.strptime(birth, format))
        except ValueError:
            sys.exit("incorrect date format")

        birth = datetime.strptime(birth, format)
        self.birth = birth


class Parse(Birthday):
    date_t = datetime.strptime(f"{date.today()}", "%Y-%m-%d")

    def __init__(self, birth):
        super().__init__(birth)

    def __str__(self):
        t_delta = self.date_t - self.birth
        t_delta = int(t_delta.total_seconds() / 60)
        minutes = p.number_to_words(t_delta, andword="")
        return f"{minutes} minutes".capitalize()

    @classmethod
    def get(cls):
        birth_date = input("birth date: ").lstrip(" ")
        return cls(birth_date)


if __name__ == "__main__":
    main()
