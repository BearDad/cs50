import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    regex = r"(((0[1-9]|[1-9]|1[0-2]):([0-5][0-9])|([1-9]|1[0-2])) ([A-P]M)) to (((0[1-9]|[1-9]|1[0-2]):([0-5][0-9])|([1-9]|1[0-2])) ([A-P]M))"
    if re.search(regex, s):
        groups = re.match(regex, s)
        if groups is None:
            raise ValueError("Could not parse")
        groups = groups.groups()
        return formating(groups)

    else:
        raise ValueError(f"Could not parse {s}")


def formating(groups):
    single_digit = r"(([1-9]|1[0-2]) ([A-P]M))"
    left_side_period = groups[5]
    right_side_period = groups[11]
    left_hours = groups[2]
    left_mins = groups[3]
    single_digit_left = groups[1]
    single_digit_right = groups[10]
    right_hours = groups[8]
    right_mins = groups[9]
    if left_side_period == "PM" and not re.search(single_digit, groups[0]):
        if right_side_period == "PM" and not re.search(single_digit, groups[6]):
            output = f"{int(left_hours) + 12}:{left_mins} to {int(right_hours) + 12}:{right_mins}"
        elif right_side_period == "PM" and re.search(single_digit, groups[6]):
            output = f"{int(left_hours) + 12}:{left_mins} to {int(groups[10]) + 12}:00"
        elif right_side_period == "AM" and not re.search(single_digit, groups[6]):
            output = f"{int(left_hours) + 12}:{left_mins} to {int(right_hours):02}:{right_mins}"
        else:
            output = f"{int(left_hours) + 12}:{left_mins} to {single_digit_right}:00"
    elif left_side_period == "PM" and re.search(single_digit, groups[0]):
        if right_side_period == "PM" and not re.search(single_digit, groups[6]):
            output = f"{int(single_digit_left) + 12}:00 to {int(right_hours) + 12}:{right_mins}"
        elif right_side_period == "PM" and re.search(single_digit, groups[6]):
            output = (
                f"{int(single_digit_left) + 12}:00 to {int(single_digit_right) + 12}:00"
            )
        else:
            output = (
                f"{int(single_digit_left) + 12}:00 to {int(single_digit_right):02}:00"
            )
    if left_side_period == "AM" and not re.search(single_digit, groups[0]):
        if right_side_period == "AM" and not re.search(single_digit, groups[6]):
            output = f"{int(left_hours):02 }:{left_mins} to {int(right_hours) + 12}:{right_mins}"
        elif right_side_period == "AM" and re.search(single_digit, groups[6]):
            output = (
                f"{int(left_hours):02 }:{left_mins} to {int(single_digit_right):02}:00"
            )
        elif right_side_period == "PM" and not re.search(single_digit, groups[6]):
            output = (
                f"{int(left_hours)}:{left_mins} to {int(right_hours)+ 12}:{right_mins}"
            )
        else:
            output = (
                f"{int(left_hours):02}:{left_mins} to {int(single_digit_right)+12}:00"
            )
    elif left_side_period == "AM" and re.search(single_digit, groups[0]):
        if right_side_period == "AM" and not re.search(single_digit, groups[6]):
            output = f"{int(single_digit_left)}:00 to {int(right_hours)}:{right_mins}"
        elif right_side_period == "PM" and re.search(single_digit, groups[6]):
            output = (
                f"{int(single_digit_left):02}:00 to {int(single_digit_right) + 12 }:00"
            )
        else:
            output = f"{int(single_digit_left)}:00 to {int(single_digit_right):02}:00"
    else:
        sys.exit("was wrong")
    return output


if __name__ == "__main__":
    main()


# Footnotes
# I know this is overly complex and could be cleaned up but it works as intended i belive
