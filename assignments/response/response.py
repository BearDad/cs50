from validator_collection import validators, errors


def main():
    print(validate(input("Email: ")))


def validate(s):
    try:
        validators.email(s, allow_empty=False)
        return "Valid"

    except (errors.InvalidEmailError, errors.EmptyValueError, errors.CannotCoerceError):
        return "Invalid"


if __name__ == "__main__":
    main()
