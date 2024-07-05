# ask the user for a greeting
# as asked "if the greeting starts with “hello”, output $0"
# I use the .partition method to isolate the first word of the string and then
# check str with "in" operator for "hello" and give $0
# check str with "in"" operator for "h"(in start of string) and give $20
# Else give $100
# x = state
# states 1 = hello 2=h


def check(x):
    if "hello" in x:
        return 1
    elif "h" in x[0]:
        return 2


def main():
    text = input("Greetings ")
    text1 = text.lower().strip()
    x = text1.partition(" ")[0]

    if check(x) == 1:
        print("$0")

    elif check(x) == 2:
        print("$20")

    else:
        print("$100")


main()
