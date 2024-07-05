# ask for input and assigns it to a variable
message = input("Input: ")
# Dictionary with all the vocals and their replacement values
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
# for loop that will take the keywords of the dictionary and replace it with it's value
for char, vocal in vocals.items():
    if char in message:
        message = message.replace(char, vocal)


print(message)