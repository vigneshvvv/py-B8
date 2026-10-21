class Address:
    def __init__(self,state, city):
        self.state = state
        self.city = city

class Employee(Address):
    def __init__(self, state, city, empId,empName):
        super().__init__(state, city)
        self.empId = empId
        self.empName = empName

class Developer(Employee):
    def __init__(self, state, city, empId, empName,techSkills):
        super().__init__(state, city, empId, empName)
        self.techSkills = techSkills


dev = Developer("TN", "Chennai", 1, "Dev", "Java")
print(dev.__dict__)