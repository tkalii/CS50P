def main():
    answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
    answer = answer.lower()
    take = loop(answer)

def loop(answer):
    if answer == "forty two":
        print("Yes!")
    elif answer == "42":
        print("Yes!")
    elif answer == "forty-two":
        print("Yes!")
    else:
        print("No!")
main()