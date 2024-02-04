import csv
import sys
if len(sys.argv) == 3:
    if sys.argv[1][-3:] == "csv":
        try:
            with open("before.csv") as file:
                reader = csv.DictReader(file)
                with open("after.csv", "w", newline="") as file2:
                    writer = csv.DictWriter(file2, fieldnames=["first", "last", "house"])
                    writer.writeheader()
                    for row in reader:
                        row["first"] = row.pop("name")
                        last_name, first_name = row["first"].split(", ")
                        row["first"] = first_name
                        row["last"] = last_name
                        writer.writerow(row)
        except FileNotFoundError:
            sys.exit("File is not accessible!")           
else:
    sys.exit("Too many or too few arguments!")