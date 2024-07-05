import requests
import sys
import json


def main():
    bitcoin = api()
    multiplier = Usrinput()
    math(bitcoin, multiplier)


def api():
    Bitcoin = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    index = Bitcoin.json()
    bitcoin = index["bpi"]["USD"]["rate_float"]
    return bitcoin


def Usrinput():
    if len(sys.argv) == 2:
        try:
            multiplier = float(sys.argv[1])
            return multiplier

        except:
            print("Command-line is not a number")
            sys.exit(1)

    else:
        print("Missing command-line argument")
        sys.exit(1)


def math(bitcoin, multiplier):
    x = bitcoin
    y = multiplier
    print(f"${x * y:,}")


if __name__ == "__main__":
    main()
