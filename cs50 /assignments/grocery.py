dict = {}


def main():
    prompt()


def prompt():
    while True:
        try:
            grocery = input().lower()

            if grocery in dict:
                dict[grocery] += 1

            elif grocery not in dict:
                dict[grocery] = 1

        except EOFError:
            for key in sorted(dict.keys()):
                print(dict[key], key.upper())

            break


if __name__ == "__main__":
    main()
