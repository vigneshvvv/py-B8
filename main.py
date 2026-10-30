# from methods import add, sub

from methods import *

from StudentsDetails import Students

print(add(11,13))

student1 = Students()
student1.id = 1
student1.studentName = "Deva"
student1.department = "IT"

print(student1.__dict__)


