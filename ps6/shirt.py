import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    check_command_line_arg()
    try:
        imagefile = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input not exists")
    shirtfile = Image.open("shirt.png")
    size = shirtfile.size
    muppet = ImageOps.fit(imagefile, size)
    muppet.paste(shirtfile, shirtfile)
    muppet.save(sys.argv[2])
    
def check_command_line_arg():
    if len(sys.argv) != 3:
        sys.exit("Command line argument no  problem!")
    
    file1= splitext(sys.argv[1])
    file2= splitext(sys.argv[2])
    if check_extension(file1[1]) == False:
        sys.exit("Invalid input")
    if check_extension(file2[1]) == False:
        sys.exit("Invalid output")
    if file1[1].lower() == file2[1].lower():
        sys.exit("Input and output are defferent extension")
def check_extension(file):
    if file in [".jpg", ".png", ".jpeg"]:
        return True
    return False

if __name__ == "__main__":
    main()
