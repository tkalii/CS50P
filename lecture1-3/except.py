while True:
    try:
        x = int(input("what's x "))
        break
    except ValueError:
        print("you didn't typed int number")
    
print(f"x is {x}")
