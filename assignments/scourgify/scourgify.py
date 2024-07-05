import sys
import csv


def main():
    parent_file, child_file = get_input()
    parent_file = read_parent_file(parent_file)
    write_child_file(parent_file, child_file)


def get_input():
    if len(sys.argv) != 3:
        sys.exit("Invalid input")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("not a parent-csv file")
    elif not sys.argv[2].endswith(".csv"):
        sys.exit("not a child-csv file")
    else:
        parent_file = sys.argv[1]
        child_file = sys.argv[2]
        print(parent_file, child_file)
        return parent_file, child_file


def read_parent_file(parent_file):
    temp_parent = []
    with open(parent_file, "r") as file:
        parent = csv.DictReader(file)
        try:
            for row in parent:
                last, first = row["name"].split(",")
                temp_parent.append(
                    {"first": first.lstrip(), "last": last, "house": row["house"]}
                )
            return temp_parent
        except KeyError:
            sys.exit("There is no name key")


def write_child_file(parent_file, child_file):
    with open(child_file, "w") as file:
        fieldnames = ["first", "last", "house"]
        child_file = csv.DictWriter(file, fieldnames=fieldnames, lineterminator="\n")
        child_file.writeheader()
        child_file.writerows(parent_file)


if __name__ == "__main__":
    main()

