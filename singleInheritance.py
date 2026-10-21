class Employee:
    def __init__(self,empName,state,city):
        self.empName = empName
        self.city = city
        self.state = state

class Developer(Employee):
    def __init__(self, empName, state, city, techSkills):
        super().__init__(empName, state, city)
        self.techSkills  = techSkills

class Manager(Employee):
    def __init__(self, empName, state, city, teamSize):
        super().__init__(empName, state, city)
        self.teamSize = teamSize

dev = Developer("Sathish", "TN", "Chennai", "Python")

print(dev.__dict__)
manager = Manager("john", "TN", "Chennai", 5)
print(manager.__dict__)

