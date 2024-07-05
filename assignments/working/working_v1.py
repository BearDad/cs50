import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    regex = r"((((([1-9])|(1[0-2])):([0-5][0-9]))|([1-9]|1[0-2])) ((A|P)M)) to ((((([1-9])|(1[0-2])):([0-5][0-9]))|([1-9]|1[0-2])) ((A|P)M))"
    if re.search(regex, s):
        hours1, hours2 = s.split("to")
        return parse_hour(hours1, hours2)
    else:
        return ValueError(f"Could not parse {s} ")


def parse_hour(h1, h2):
    h1, h2 = h1.strip().split(" "), h2.strip().split(" ")
    full1, full2 = h1[0], h2[0]
    format1, format2 = h1[1], h2[1]
    reg_dots = r"((([1-9])|(1[0-2])):([0-5][0-9]))"
    parsed1 = full1.split(":")
    parsed2 = full2.split(":")
    if re.search(reg_dots, full1) or re.search(reg_dots, full2):
        if re.search(reg_dots, full1):
            if re.search(reg_dots, full2):
                return convert_to_24(
                    parsed1, parsed2, format1, format2, full1, full2, reg_dots
                )
            else:
                return convert_to_24(
                    parsed1, parsed2, format1, format2, full1, full2, reg_dots
                )

        else:
            parsed2 = full2.split(":")
            return convert_to_24(
                parsed1, parsed2, format1, format2, full1, full2, reg_dots
            )
    else:
        return convert_to_24(parsed1, parsed2, format1, format2, full1, full2, reg_dots)


def convert_to_24(h1, h2, format1, format2, full1, full2, reg_dots):
    print(h1, h2, full1, full2)
    if "PM" in format1 and re.search(reg_dots, full1):
        if "PM" in format2 and re.search(reg_dots, full2):
            output = f"{int(h1[0]) + 12}:{h1[1]} to {int(h2[0]) + 12}:{h2[1]}"
            return output
        else:
            output = f"{int(h1[0]) + 12}:{h1[1]} to {h2[0]}:{h2[1]}"
            return output
    elif "PM" in format1 and not re.search(reg_dots, full1):
        if "PM" in format2 and not re.search(reg_dots, full2):
            output = f"{int(h1[0]) + 12}:00 to {int(h2[0]) + 12}:00"
            return output
        elif "AM" in format2 and not re.search(reg_dots, full2):
            output = f"{int(h1[0]) + 12}:{h1[1]} to {h2[0]}:00"
            return output

        elif "PM" in format2 and re.search(reg_dots, full2):
            output = f"{int(h1[0]) + 12}:00 to {int(h2[0]) + 12}:{h2[1]}"
            return output
    elif "AM" in format1 and re.search(reg_dots, full1):
        if "AM" in format2 and re.search(reg_dots, full2):
            if format2 is None:
                ...
            else:
                output = f"{full1} to {h2[0]}:{h2[1]}"
            return output
        elif "PM" in format2 and re.search(reg_dots, full2):
            output = f"{h1[0]}:00 to {int(h2[0]) + 12}:{h2[1]}"
            return output
        else:
            output = f"{h1[0]}:{h1[1]} to {int(h2[0] ) + 12}:00"
            return output
    elif "AM" in format1 and not re.search(reg_dots, full1):
        if "AM" in format2 and not re.search(reg_dots, full2):
            output = f"{h1[0]}:00 to {h2[0]}:00"
            return output
        elif re.search(reg_dots, full2) and "PM" in format2:
            if int(full1) < 10:
                output = f"0{full1}:00 to {int(h2[0]) + 12}:{h2[1]}"
            else:
                output = f"{h1[0]}:00 to {int(h2[0]) + 12}:00"
            return output

        else:
            output = f"{h1[0]}:00 to {int(h2[0]) + 12}:{h2[1]}"
            return output

    else:
        output = f"{h1[0]}:{h1[1]} to {int(h2[0]) + 12}:{h2[1]}"
        return output


if __name__ == "__main__":
    main()
