# def main():
#     tipPercent = input("And how much is your tip? ")
#     price = input("How much is the price of the meal? ")
#     tipCalc(tipPercent)
#     tip = (tipPercent / 100) * price

# def tipCalc(tip):
#     return tip


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = (dollars / 100) * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    return float(d)

def percent_to_float(p):
    return float(p)

main()