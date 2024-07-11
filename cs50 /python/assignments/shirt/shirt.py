from PIL import Image, ImageOps
import sys
import os.path


def main():
    cli_input, cli_output = get_input()
    image_mod(cli_input, cli_output)

list 
def get_input():
    cli_input, cli_output = sys.argv[1], sys.argv[2]
    root, ext = os.path.splitext(cli_input)
    root1, ext1 = os.path.splitext(cli_output)
    ext, ext1 = ext.casefold(), ext1.casefold()
    if len(sys.argv) != 3:
        sys.exit("Too few arguments")
    elif ext in [".jpg", ".png", ".jpeg"] == False:
        sys.exit("Wrong formatted Input file")
    elif ext1 in [".jpg", ".png", ".jpeg"] == False:
        sys.exit("Wrong formatted Output file")
    elif ext != ext1:
        sys.exit("different format files")
    else:
        return (cli_input, cli_output)


def image_mod(cli_input, cli_output):
    print(cli_input, cli_output)
    try:
        shirt = Image.open(
            "/home/beardad23/vscode/cs50 /python/assignments/shirt/shirt.png"
        )
        with Image.open(cli_input) as file:
            cli_input_cropped = ImageOps.fit(file, shirt.size)
            cli_input_cropped.paste(shirt, mask=shirt)
            cli_input_cropped.save(cli_output)
    except FileNotFoundError:
        sys.exit("file not found")


if __name__ == "__main__":

    main()
