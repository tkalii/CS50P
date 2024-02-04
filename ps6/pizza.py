#A program to change csv file into tabular format
import csv
import sys
from tabulate import tabulate

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments ")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments ")
elif not sys.argv[1].endswith('.csv'):
    sys.exit("Not a csv file")
table =[]
try:
    with open(sys.argv[1]) as file:       
        reader = csv.reader(file)
        for row in reader:
            table.append(row)
    print(tabulate(table[1:], headers=table[0], tablefmt="grid"))
except FileNotFoundError:   
    print("File does not exist!")