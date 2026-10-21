class Address:
    def __init__(self, state, city):
        self.state = state
        self.city = city

class Employee:
    def __init__(self,name, id):
        self.name = name
        self.id = id



class Manager(Employee, Address):
    def __init__(self, name, id, state, city,teams):
        Employee.__init__(self,name, id)
        Address.__init__(self,state, city)
        self.teams = teams


manager = Manager("John", 1, "TN", "Chennai", 5)
print(manager.__dict__)