import sys
import csv
from tabulate import tabulate


def main():
    file_name = cli_argument()
    table = file(file_name)
    print(tabulate(table, headers="firstrow", tablefmt="grid"))


def cli_argument():
    try:
        if len(sys.argv) < 2:
            sys.exit("Too few cli-args")
        elif len(sys.argv) > 2:
            sys.exit("Too many cli-args")
        elif not sys.argv[1].endswith(".csv"):
            sys.exit("Incorrect input")
        else:
            file_name = sys.argv[1]
            return file_name

    except IndexError:
        sys.exit()


def file(file_name):
    try:
        x = []
        with open(file_name, "r") as file:
            pizza = csv.reader(file)
            for row in pizza:
                x.append(row)
            return x
    except FileNotFoundError:
        sys.exit("file not found or doesn't exist ")


if __name__ == "__main__":
    main()
