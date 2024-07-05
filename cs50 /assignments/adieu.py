import inflect


def main():
    p = inflect.engine()
    main_txt = []
    add(main_txt, p)
    output = p.join(main_txt)
    print(f"Adieu, adieu, to {output}")


def add(main_txt, p):
    while True:
        try:
            txt = input("Input: ").strip()

        except EOFError:
            print()
            break
        main_txt.append(txt)
    output = p.join(main_txt)


if __name__ == "__main__":
    main()
