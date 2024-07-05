months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",   
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():
    prompt()


def prompt():
    while True:
        date = input("Date: ").capitalize()
        try:
            if "/" in date:
                month, day, year = date.split("/")
            elif "," in date:
                date = date.replace(",", "")
                month, day, year = date.split(" ")
                # .index() gets the dictionary and outputs a value if the keyword is in the list
                month = (months.index(month)) + 1
            if int(month) > 12 or int(day) > 31:
                raise ValueError
        # handles the errors and re-prompts the user

        except (EOFError, ValueError, NameError, KeyError):
            pass

        else:
            print(f"{int(year)}-{int(month):02}-{int(day):02}")
            break


if __name__ == "__main__":
    main()
