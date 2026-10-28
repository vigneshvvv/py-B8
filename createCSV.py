import csv

with open("employee.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["id", "name", "age", "department"])
    writer.writerow([1,"Ravi", 25, "Dev"])
    writer.writerow([2, "Mohan", 27, "Testing"])

print("Data written")