import csv

emp = [
    [4, "Arun", 24, "Cloud"],
    [5, "Vignesh", 25, "Dev"]
]

emp1= {
    "id": 6,
    "name": "Deva",
    "age": 29,
    "department": "Devops"
}

with open("employee.csv", "a", newline="") as file:
    # writer = csv.writer(file)
    # writer.writerow([3, "Tamil", 29, "Dev"])
    # writer.writerows(emp)

    fieldNames = ["id", "name", "age", "department"]
    writer= csv.DictWriter(file, fieldnames=fieldNames)

    writer.writerow(emp1)


print("Data written")