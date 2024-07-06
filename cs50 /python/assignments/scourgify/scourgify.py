import sys
import csv


def main():
    parent_file, child_file = get_input()


def get_input():
    if len(sys.argv) < 3 or len(sys.argv) > 3:
        sys.exit()
    else:
        parent_file = sys.argv[1]
        child_file = sys.argv[2]
        return parent_file, child_file


if __name__ == "__main__":
    main()
