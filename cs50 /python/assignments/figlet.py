from pyfiglet import Figlet
import sys
import random


def main():
    figlet = Figlet()
    fonts = figlet.getFonts()
    arguments = len(sys.argv)
    render(figlet, fonts, arguments)


def render(figlet, fonts, arguments):
    if arguments == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts:
        text = input("input: ")
        f = sys.argv[2]
        figlet.setFont(font=f)
        print(figlet.renderText(text))
        sys.exit(0)

    elif arguments == 1:
        text = input("input: ")
        f = random.choice(fonts)
        figlet.setFont(font=f)
        print(figlet.renderText(text))
        sys.exit(0)
    else:
        print("Invalid usage")
        sys.exit(1)


if __name__ == "__main__":
    main()
