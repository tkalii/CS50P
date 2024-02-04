def main():
    greeting = input("Greeting: ")
    greeting = greeting.lower()
    customer = sayit(greeting)
    

def sayit(prompt):
    if (prompt == "hello"):
        print("$",0)
    elif (prompt.find("hello") == 0):
        print("$",0)
    elif (prompt != "hello" and prompt[0] == "h"):
        print("$",20)
    else:
        print("$",100)

main()