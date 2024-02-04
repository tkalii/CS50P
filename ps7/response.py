from validators import validator
def main():
    email = input("what's your email? ")
    try:
        valid = validator.emali(email)
        print("valid")
    except:
        print("Invalid")    
