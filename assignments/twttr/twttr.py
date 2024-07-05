def main():
    message = input("Input: ")
    message = str(message)
    print(shorten(message))

vocals = {
    "U": "",
    "u": "",
    "O": "",
    "o": "",
    "i": "",
    "I": "",
    "E": "",
    "e": "",
    "A": "",
    "a": "",
}


def shorten(word):
    while True:
        for char, vocal in vocals.items():
            if char in word:
                word = word.replace(char, vocal)
        return word        


if __name__ == "__main__":
    main()
