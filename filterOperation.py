employees = [
    {"id": 101, "name": "Robert", "age": 22, "salary":40000},
    {"id": 102, "name": "Alwin", "age": 24, "salary":60000},
    {"id": 103, "name": "Jim", "age": 26, "salary":80000},
    {"id": 104, "name": "Wasnik", "age": 29, "salary":75000}
]

result = list()
for emp in employees:
    if emp["salary"] > 50000:
        result.append(emp)


# print(result)


resultN = filter(lambda emp: emp["salary"] > 50000, employees)
# print(list(resultN))

result1 = map(lambda emp: emp["name"], employees)
print(list(result1))

result2 = map(lambda emp: {**emp, "bonus": emp["salary"]*1.50}, employees)
print(list(result2))


# def filtering(emp):
#     return emp["salary"] > 50000


# def mapping(emp):
#     return {
#         **emp,
#         "Bonus": emp["Salary"]*1.50
#     }

# for e in employees:
#     filtering(e)


# filter(lambdaFunction , listOfdict)
# filter(lambdaFunction , listOfdict)