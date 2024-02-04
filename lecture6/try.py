from PIL import Image

class InvalidFactor(Exception):
    pass
def main(): 
    with Image.open("py.jpg") as im:
        factored = scaled_by_size(im, 2)
        factored.save("C:\E\cs50\Python\lecture6\ factored.jpg")
    
def scaled_by_size(im, factor):
    if (factor <= 0):
        raise InvalidFactor("OH NO NO NO NO NO NO")
    return im.resize((round(im.width * factor), round(im.height * factor)))

if __name__ == "__main__":
    main()