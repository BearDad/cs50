import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(.)+><\/iframe>", s):
        m = re.search(
            r"(http:\/\/|https:\/\/)(www\.)*(youtube\.com\/embed\/)([a-z_A-Z_0-9]+)", s
        )
        if m:
            link = m.group()
            return parsing(link)
        else:
            return None


def parsing(link):
    dict = link.split("/")
    dict[0] = "https://"
    dict[2] = "youtu.be"
    return f"{dict[0]}{dict[2]}/{dict[4]}"


if __name__ == "__main__":
    main()
