import emoji


def main():
    alias = input("Input: ")
    check(alias)


def check(alias):
    print(emoji.emojize(alias, language="alias"))


if __name__ == "__main__":
    main()
