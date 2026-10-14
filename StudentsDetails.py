class Students:
    id = 0
    studentName = ""
    department = ""





student1 = Students()
student1.id = 1
student1.studentName = "Deva"
student1.department = "IT"

students2 = Students()
students2.id = 2
students2.studentName = "Arvind"
students2.department = "EEE"

print(student1.__dict__)
print(students2.__dict__)