def main():
    y = takeInput()
    x = tolower(y)

def takeInput():
    word = str(input("What's your input? "))
    return word

def tolower(name):
    print(name.upper())

main()