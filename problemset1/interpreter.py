# Get the expression
expression = input("Expression: ")
x , y , z = expression.strip().split()
# Change type of variable x and z
x = float(x)
z = float(z)

# Perform the operations
match y:
    case "+":
        print(round(x + z, 2))
    case "-":
        print(round(x - z, 2))
    case "/":
        print(round(x / z, 2))
    case "*":
        print(round(x * z, 2))
    case _:
        print("What? ")