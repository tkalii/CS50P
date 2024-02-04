#get user input
fraction = str(input("Fraction: "))
fraction = fraction.replace(" ", "")
x, y = fraction.split('/')
#catch the error might happen
try:   
    x = int(x)
    y = int(y)
    compute = x / y
except ValueError:
    print("There is no integer to divide!")
except ZeroDivisionError:
    print("You can't divide by zero")
else:
    compute = compute * 100
    #round to nearest integer
    compute = round(compute)
    #if less than one print E and greater than 99 print F
    if (compute < 1):
        print("E")
    elif (compute > 99):
        print("F")
    else:
        print(f"{compute}%")