class Employee:
    def __init__(self,empId, empName):
        self.empId = empId
        self.empName = empName

class Address(Employee):
    def __init__(self, empId, empName, city):
        Employee.__init__(self,empId, empName)
        self.city = city

class Coordinate(Employee):
    def __init__(self, empId, empName, lat, lng):
        Employee.__init__(self,empId, empName)
        self.lat = lat
        self.lng = lng

class Developer(Address, Coordinate):
    def __init__(self, empId, empName, city, lat, lng, techSkills):
        Address.__init__(self,empId, empName, city)
        Coordinate.__init__(self,empId, empName,lat, lng )
        self.techSkills = techSkills


dev = Developer(1, "Rahul", "Chennai", "12.232", "3.22", "Python")
print(dev.__dict__)
