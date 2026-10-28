import csv

with open("employee.csv", "r", newline="") as file:
    # reader = csv.reader(file)

    # for row in reader:
    #     print(row)
    reader = csv.DictReader(file)
    for row in reader:
        print(row)