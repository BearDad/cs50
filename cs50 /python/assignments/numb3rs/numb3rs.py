import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^\d+\.\d+\.\d+\.\d+$", ip):
        a, b, c, d = ip.split(".")
        ip_list = [a, b, c, d]

        while True:
            for number in ip_list:
                if int(number) < 0 or int(number) > 255:
                    return False

            else:
                return True
                    
    else:
        return False


if __name__ == "__main__":
    main()
