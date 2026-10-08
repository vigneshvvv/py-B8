student = {
    "name": "Arun",
    "age": 25,
    "course": "Python",
    "marks": 85
}

print(student["name"])
student["name"] = "Arjun"
print(student)
student["isActive"] = True
print(student)

# print(student["firstName"])

print(student.get("firstName"))


student.update({
    "firstName": "Arjun",
    "lastName": "Kumar"
})
print(student)

x = student.pop("lastName")
print(x)
print(student)

print(student.keys())
print(student.values())
print(student.items())

print(len(student))

for key,value in student.items():
    print(key, "=", value)