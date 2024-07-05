# Finished 12 hour format to 24 hour format converter
# Date: 05/10/2024


import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    regex = r"(((0[1-9]|[1-9]|1[0-2]):([0-5][0-9])|([1-9]|1[0-2])) ([A-P]M)) to (((0[1-9]|[1-9]|1[0-2]):([0-5][0-9])|([1-9]|1[0-2])) ([A-P]M))"
    if re.search(regex, s):
        groups = re.match(regex, s)
        if groups is None:
            raise ValueError("could not parse")
        groups = groups.groups()
        return formating(groups)

    else:
        raise ValueError(f"could not parse {s}")


def formating(groups):
    left_side_period = groups[5]
    right_side_period = groups[11]
    single_digit_left = groups[4]
    single_digit_right = groups[10]
    double_digit_left_hours = groups[2]
    double_digit_left_mins = groups[3]
    double_digit_right_hours = groups[8]
    double_digit_right_mins = groups[9]
    if single_digit_left and int(single_digit_left) < 12:
        if left_side_period == "PM":
            left_hours = f"{int(single_digit_left) + 12}:00"
        else:
            left_hours = f"{int(single_digit_left):02}:00"

    if single_digit_left and int(single_digit_left) == 12:
        if left_side_period == "PM":
            left_hours = "12:00"
        else:
            left_hours = "00:00"

    if single_digit_right and int(single_digit_right) < 12:
        if right_side_period == "PM":
            right_hours = f"{int(single_digit_right) + 12}:00"
        else:
            right_hours = f"{int(single_digit_right):02}:00"
    if single_digit_right and int(single_digit_right) == 12:
        if right_side_period == "PM":
            right_hours = "12:00"
        else:
            right_hours = "00:00"

    if double_digit_left_hours and int(double_digit_left_hours) < 12:
        if left_side_period == "PM":
            left_hours = f"{int(double_digit_left_hours) + 12}:{double_digit_left_mins}"
        else:
            left_hours = f"{int(double_digit_left_hours):02}:{double_digit_left_mins}"

    if double_digit_left_hours and int(double_digit_left_hours) == 12:
        if left_side_period == "PM":
            left_hours = "12:00"
        else:
            left_hours = "00:00"

    if double_digit_right_hours and int(double_digit_right_hours) < 12:
        if right_side_period == "PM":
            right_hours = (
                f"{int(double_digit_right_hours) + 12}:{double_digit_right_mins}"
            )
        else:
            right_hours = (
                f"{int(double_digit_right_hours):02}:{double_digit_right_mins}"
            )

    if double_digit_right_hours and int(double_digit_right_hours) == 12:
        if right_side_period == "PM":
            right_hours = "12:00"
        else:
            right_hours = "00:00"

    output = f"{left_hours} to {right_hours}"

    return output


if __name__ == "__main__":
    main()
