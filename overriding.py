class Employee:
    def calculate_bonus(self):
        print("General employee bonus 5000")

class Manager(Employee):
    def calculate_bonus(self):
        print("Manager bonus 15000")


em1 = Employee()
em1.calculate_bonus()
em2 = Manager()
em2.calculate_bonus()

emp = [Employee(), Manager()]

for em in emp:
    em.calculate_bonus()