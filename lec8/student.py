class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old!"
        
def main():
    student = Student("Harry", 8)
    print(student)
    
if __name__ == "__main__":
    main()