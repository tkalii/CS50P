def main():
    mass = int(input("Enter the mass: "))
    take = calculate(mass)
    print(take)

def calculate(prompt):
    E = prompt * pow(300000000, 2)
    return E

main()
