# turn camel case into snake case
# examples| camel:firstName   snake:first_name
# get input and send it into snake_loop
# check for each character in the str and if upper then add _
def snake_loop(camel):
    snake = camel
    for capital in snake:
        if capital.isupper():
            print("_" + capital.lower(), end="")
        else:
            print(capital, end="")


def main():
    camel = input("input function name: ")
    print("snake_case: ", end="")
    snake_loop(camel)


main()
