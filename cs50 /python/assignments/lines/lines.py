import sys

#this good
def main():
    file_name = cli_argument()
    lines = file(file_name)
    line_count = Line_count(lines)
    print(line_count)


def cli_argument():
    while True:
        try:
            if len(sys.argv) == 1 or len(sys.argv) == 0:
                sys.exit("too few cli-args")
            elif len(sys.argv) > 2:
                sys.exit("too many cli-args")
            elif not sys.argv[1].endswith(".py"):
                sys.exit("incorrect input")
            else:
                file_name = sys.argv[1]
                return file_name
                break
        except IndexError, FileNotFoundError:
            sys.exit()


def file(file_name):

        try:
            with open(file_name, "r") as file:
                lines = file.readlines()
                return lines
        except (FileExistsError, FileNotFoundError):
            print("file not found or doesn't exitst")
            sys.exit()


def Line_count(lines):
    counter = 0
    for row in lines:
        if row == "\n" == True or row.lstrip().startswith("#") or len(row.strip()) < 1:
            continue
        else:
            counter += 1
    return counter


if __name__ == "__main__":
    main()
