from pyfiglet import Figlet
import sys
import random


def main():
    figlet = Figlet()
    fonts = figlet.getFonts()
    arguments = len(sys.argv)
    text = input("input: ")
    render(figlet, fonts, arguments, text)


def render(figlet, fonts, arguments, text):
    if arguments == 1 or arguments == 3:
        if arguments == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts:
            f = sys.argv[2]
            figlet.setFont(font=f)
            print(figlet.renderText(text))
            sys.exit(0)
        elif arguments == 1:
            f = random.choice(fonts)
            figlet.setFont(font=f)
            print(figlet.renderText(text))
            sys.exit(0)
        else:
            print("Invalid usage")
            sys.exit(1)


if __name__ == "__main__":
    main()
