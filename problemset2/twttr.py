#TAKE INPUT AND OMMIT THE VOWEL

#take use input
string = str(input("Input: "))
# string = string.lower()
vowels = {'a','e','i','o','u','A','O','U','I','E'}
for letter in string:
    if not letter in vowels:
        print(letter, end="")