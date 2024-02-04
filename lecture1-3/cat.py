#A program to print meow n times
def main():
    number = get_number()
    meow(number)
#get n
def get_number():
    while True:
        n = int(input("what's n? "))
        if n > 0:
            break
    return n
 #say meow       
def meow(n):
    for _ in range(n):
        print ("meow")

main()