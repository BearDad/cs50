
import sys
import os.path
def main():
    cli_input, cli_output = get_input()
def get_input():
    cli_input , cli_output = sys.argv[1], sys.argv[2]
    root, ext = os.path.splitext(cli_input)    
    root1, ext1 = os.path.splitext(cli_output)
    ext, ext1 = ext.casefold(), ext1.casefold()
    print(ext, ext1)
    if len(sys.argv) != 3:
        sys.exit("Too few arguments")
    elif  ext != ".jpg" or ext != ".png" or ext != ".jpeg":
        sys.exit("Wrong formatted Input file")
    elif  ext1 != ".jpg" or ext1 != ".png" or ext1 != ".jpeg":
        sys.exit("Wrong formatted Output file")
    elif ext != ext1:
        sys.exit("different format files")
    else: 
        print(cli_input, cli_output)
        return(cli_input, cli_output)

if __name__ == "__main__":
    
    main()