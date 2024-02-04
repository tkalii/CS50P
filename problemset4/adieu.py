import inflect

p = inflect.engine()
names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)    
    except EOFError:
        print()
        break

output = p.join(name)
print("Adieu, adieu,to ", output)
