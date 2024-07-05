def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6 and s.isalnum():
        if s.isalpha():
            return True
        else:
            if s[:2].isalpha() and s[-2:].isdigit():
                for char in s:
                    if char.isdigit():
                        index = s.index(char)
                        if s[index:].isdigit() and char != "0":
                            return True
                        else:
                            return False
            else:
                return False
    else:
        return False



if __name__ == "__main__":
    main()