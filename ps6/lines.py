#a program that counts line of code
import sys
def main():
    argument()
    #check if it's a python file
    #open the file
    try:
        if not sys.argv[1].endswith(".py"):
            sys.exit("Not a python file")
        with open(sys.argv[1]) as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("The file is not accesible or not found!")
    else:
        count = 0
        for line in lines:
            line = line.lstrip()
            line = line.rstrip()
            #check if it is a comment
            if not line.startswith('#') and line != '':
                    #cont the lines
                    count += 1
            
        print(count)
def argument():
    if len(sys.argv) != 2:
        sys.exit("Too many arguments!")
if __name__ == "__main__":
    main()