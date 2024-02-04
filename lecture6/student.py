import csv

name = input("what's your name? ")
home = input("where's your home? ")

with open("student.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])