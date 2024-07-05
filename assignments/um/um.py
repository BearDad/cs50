import re


def main():
    print(count(input("Text: ")))


def count(s):
    regex = r"(?:^|\W)([uU]m)(?:$|\W)"
    if re.findall(regex, s):
        output = re.findall(regex, s)
        output = int(output.count("um")) + int(output.count("Um"))
        if output is None:
            output = 0
            return output
        else:
            return output


if __name__ == "__main__":
    main()
