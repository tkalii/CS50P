def main():
    filename = input("what's the file name? ")
    grab = application(filename)

def application(yourfile):
    if yourfile.endswith(".jpg") == True:
        print("image/jpeg")
    elif yourfile.endswith(".jpeg") == True:
        print("image/jpeg")
    elif yourfile.endswith(".pdf") == True:
        print("application/pdf")
    else:
        print("application/octet-stream")

main()