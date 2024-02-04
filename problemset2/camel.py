#ask for user input in camelCase
camelCase = input("Enter your input: ")

print("snake_case: ",end="")
#change the user input into snake_case & print the output

for letter in camelCase:
    if letter.isupper():
        print("_" + letter.lower(), end="")
    else:
        print(letter, end="")