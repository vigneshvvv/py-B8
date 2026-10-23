from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self,amount):
        pass


class UPI(Payment):
    def pay(self, amount):
        print("Paid using UPI")


class CreditCard(Payment):
    def pay(self, amount):
        print("Paid using Credit card")


p1 = UPI()
p1.pay(10000)

p2 = CreditCard()
p2.pay(10000)

